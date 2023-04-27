import torch
import scipy
import math
import numpy as np
import matplotlib.pyplot as plt

import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.nn.functional as F
import torch.optim as optim

import sys
sys.path.append("../") 
sys.path.append("../../") 
from gaussian_basis_filters import *
from structured_conv_layer import *
import argparse


""" Plot the pretrained filters and their approximation.
Input:
    - normal: the pretrained filters
    - structured: the N-Jet approximated filters 
    - errors: the errors per filter 
    - scales: the learned N-Jet scale 
    - alphas: the learned N-Jet coefficients 
    - cols: maximum suplots columns 
    - lattice_size: default 1.0
"""
def plot_comparison(
        normal, 
        structured, 
        errors, 
        scales, 
        alphas, 
        cols=12, 
        lattice_size=1.0):

    # [K, C, H, W] --> [H W C K] 
    structured = np.transpose(structured, (2, 3, 1, 0))

    N = normal.shape[3]
    C = normal.shape[2] 
    assert(C == 3) # Compute always have 3 channels as input 
    if not cols:
        cols = int(np.ceil(np.sqrt(N)))
    cols = min(cols, N)
    rows = int(np.ceil(N / cols))

    """ Define the plotting grid """
    fig, axes = plt.subplots(2*rows, cols, squeeze=False)
    fig.suptitle('Average L2 approximation error '+str(errors.mean()))    
    i = 0
    for row in range(rows):
        for col in range(cols):
            axes[2*row, col].axis('off')
            axes[2*row+1, col].axis('off')

            if i >= N: continue;

            """ Rescale pixel intensities for visualization"""
            image = (normal[:, :, :, i] - normal[:, :, :, i].min())\
                    /(normal[:, :, :, i].max() - normal[:, :, :, i].min())
            axes[2*row, col].imshow(image)

            """ Rescale pixel intensities for visualization"""
            image = (structured[:, :, :, i] - structured[:, :, :, i].min())\
                    /(structured[:, :, :, i].max() - structured[:, :, :, i].min())
            axes[2*row+1, col].imshow(image)

            print("Filter {:3d} - error = {:.5f}, \
                mean sigma = {:.3f}, std sigma = {:.3f}, \
                mean alphas = {:+.3f}, std alphas = {:.3f}".format(i, \
                errors[i], scales[i].mean(), scales[i].std(), \
                alphas[i, :, :].mean(), alphas[i, :, :].std()))
            i += 1
    return fig


""" MSE loss between the pretrained filter and the N-Jet approximation.
Input:
    - normal: pretrained filters (1 channel)
    - structured: the N-Jet filter
"""
def compute_mse(normal, structured):
    structured_filters = []
    for i in range(0, structured.shape[0]):
        """ Crop to have the same size """
        size_diff = structured.shape[2] - normal.shape[2]
        if size_diff>0:
            cropping = int(size_diff/2)
            afilter = structured[i:i+1,:,cropping:structured.shape[2]\
                            -cropping,cropping:structured.shape[2]\
                            -cropping]
            structured_filters.append(afilter)
        elif size_diff<0:
            padding = int(abs(size_diff)/2)
            afilter = F.pad(structured[i:i+1,:,:,:], \
                            (padding,padding,padding,padding,0,0), \
                            'constant',0)
            structured_filters.append(afilter)
        else:
            structured_filters.append(structured[i:i+1,:,:,:])
    
    """ Now the resized prediction should match the normal filter"""
    structured_tensor = torch.squeeze(torch.stack(structured_filters,dim=1),dim=0)

    """ Compute the MSE loss """
    loss_fn = nn.MSELoss(reduction='mean')
    loss = loss_fn(normal, structured_tensor)
    return loss, structured_tensor

"""
Performs pretrained filter approximation using N-Jet filters.
Input:
    - normal_filters: the filter to approximate (1 channel)
    - init_order: the N-Jet order 
    - init_scale: the N-Jet scale initialization (default: 0)
    - init_k: the N-Jet filter spatial extent (default: 2) 
    - learn_sigma: default True
    - max_steps: training steps to take
    - lr: learning rate used
    - weight_decay: weights regularization 
    - use_cuda: on the GPU or not
Output:
        structured_filters [H W C K]
        errors [N]
        scales [C, N]
        alphas [C, F, N]
"""
def approximate_normal_filters(
        normal_filters,
        init_order,
        init_scale,
        init_k,
        learn_sigma,
        max_steps,
        lr,
        weight_decay,
        use_cuda):

    """ Define N-Jet layer. """
    model = Srf_layer_shared(
                inC=normal_filters.shape[2], 
                outC=normal_filters.shape[3],
                init_k=init_k, 
                init_order=init_order, 
                init_scale=init_scale, 
                learn_sigma=learn_sigma,
                use_cuda=use_cuda)
    if use_cuda: model = model.cuda()
        
    """ Define the optimizer """
    optimizer = optim.Adam(
                    model.parameters(), 
                    lr=lr, 
                    weight_decay=weight_decay)

    """ Rearrange the filter dimensions to match the N-Jet dimensions """
    device = torch.device("cuda" if use_cuda else "cpu")
    normal_filters = torch.tensor(np.transpose(normal_filters,(3,2,0,1)),\
                                dtype=torch.float32, device=device)

    """ Standardize the filter """
    normal_filters = (normal_filters - normal_filters.mean())\
                    /(normal_filters.std())

    """ Start the training loop """ 
    for epoch in range(1, max_steps):
        structured_filters = model.forward_no_input()
        loss, _ = compute_mse(normal_filters, structured_filters)
        optimizer.zero_grad()
        loss.backward() 
        optimizer.step()
    
    """ Get the final filters """    
    structured_filters = model.forward_no_input()
    loss, structured_tensor = compute_mse(normal_filters,structured_filters)

    return structured_tensor, loss, model.scales, model.alphas 

""" The script implementing the test: selects a few channels of an alexnet pretrained 
filter and approximates it with the N-Jet filters.
Inputs:
    - args: the optimizer arguments
    - use_cuda: if on the GPU or not
    - channelNo: the input channel number
    - rangeStart: the selected starting channel
    - rangeEnd: the select end channel
""" 
def run_test(args, use_cuda, channelNo=0, rangeStart=0, \
            rangeEnd=5):

    
    """ Firt layer has size: 11x11x3x96 """
    weights = np.load(open("alexnet_conv1.npy", "rb"),encoding="latin1",\
                        allow_pickle=True)

    normal_l = []
    structured_l = []
    errors_l = []
    scales_l = []
    alphas_l = []

    """ Loop over the channel range """
    for i in range(rangeStart, rangeEnd):
        normal = weights[0][:, :, channelNo:channelNo+3, i:i+1]

        """ Approximate each channel with an N-Jet filter. """
        structured_i, errors_i, scales_i, alphas_i = approximate_normal_filters(
                normal_filters=normal,
                init_order=args.init_order, 
                init_scale=args.init_scale, 
                init_k=args.init_k,
                learn_sigma=args.learn_sigma,
                lr=args.lr,
                weight_decay=args.weight_decay,
                max_steps=args.epochs,
                use_cuda=use_cuda)
        
        normal_l.append(weights[0][:, :, :, i:i+1]) 
        structured_l.append(structured_i.detach().cpu().numpy()) 
        errors_l.append(errors_i.detach().cpu().numpy())
        scales_l.append(scales_i.detach().cpu().numpy())
        alphas_l.append(alphas_i.detach().cpu().numpy())

    """ Plot the filter channels and their approximations """ 
    normal = np.stack(normal_l, axis=3)
    structured = np.squeeze(np.stack(structured_l, axis=0), axis=1)
    errors = np.stack(errors_l, axis=0)
    scales = np.stack(scales_l, axis=0)
    alphas = np.stack(alphas_l, axis=0)
    fig = plot_comparison(
                    weights[0][:, :, :, rangeStart:rangeEnd], \
                    structured, \
                    errors, \
                    scales, \
                    alphas)
    fig.savefig('conv1-order-'+str(args.init_order)+'.pdf', \
                bbox_inches='tight', pad_inches=0)
    plt.show()

""" Main loop calling the test. """
def main():
    # Training settings
    parser = argparse.ArgumentParser()
    parser.add_argument('--no-cuda', action='store_true', default=False,
                        help='disables CUDA training')
    parser.add_argument('--seed', type=int, default=0, metavar='S',
                        help='random seed (default: 1)')
    parser.add_argument('--init_order', type=int, default=3, \
                        help='Derivatives order')
    parser.add_argument('--init_scale', type=float, default=0.0, \
                        help='If not lernable')
    parser.add_argument('--init_k', type=float, default=2.0, \
                        help='Spatial extent')
    parser.add_argument('--learn_sigma', action='store_true', default=True,
                        help='If we learn of fix sigma')
    parser.add_argument('--epochs', type=int, default=1000, metavar='N',
                        help='number of epochs to train (default: 10)')
    parser.add_argument('--optim', type=str, default="adam", metavar='O',
                        help='the optimizer choice')
    parser.add_argument('--lr', type=float, default=1.0e-1, metavar='LR',
                        help='learning rate')
    parser.add_argument('--weight-decay', type=float, default=0.0,
                        metavar='W', help='the weight decay')
    args = parser.parse_args()
    torch.manual_seed(args.seed)
    
    use_cuda = not args.no_cuda and torch.cuda.is_available()
    run_test(args, use_cuda)

if __name__ == '__main__':
    main()

