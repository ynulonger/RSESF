import os
import cv2
import glob
import math
import torch
import logging
import datetime
import argparse
import numpy as np
import torch.nn as nn
from utils.metrics import *
from utils.dataset import *
import torch.nn.functional as F
import matplotlib.pyplot as plt
from torchsummary import summary
from models.unet_model import *
from torch.autograd import Variable
from torch.utils.data import DataLoader
import torchvision.transforms.functional as tf
from sklearn.metrics import confusion_matrix

import matplotlib.lines as lines
import glob

def get_roi_mask_np(h, n_channels):
    img = np.zeros([h,h,1])
    x = [i for i in np.arange(-h//2,h//2,1)]
    y = [i for i in np.arange(-h//2,h//2,1)]

    for i in x:
        for j in y:
            if i**2+j**2<(h/2)**2:
                img[i+h//2,j+h//2,0]=1
            else:
                img[i+h//2,j+h//2,0]=0

    roi_mask = img[:h-1,:h-1]
    inverse_roi_mask = 1-roi_mask
    img_inverse_roi  = np.concatenate([inverse_roi_mask*255]*n_channels, axis=2)
    return roi_mask, inverse_roi_mask, img_inverse_roi

def vis_pred(mask_name, model, dataset, x_pos=-35):
    masks = [cv2.imread(mask_name[i], flags=1) for i in range(len(mask_name))]
    fig = plt.figure(dpi=150)
    print(mask_name[0].split('_'), masks[0].shape)
    mIoU = [mask_name[i].split('_')[-1][:-4] for i in range(len(mask_name))]
    count = 1
    for row in range(2):
        for col in range(2):
            plt.subplot(2,2,count)
            m = masks[count-1]
            roi_mask, inverse_roi_mask, img_inverse_roi = get_roi_mask_np(m.shape[0]+1,3)
            m = m*roi_mask+img_inverse_roi
            m = m.astype(np.uint8)
            plt.imshow(m)
            plt.axis('off')
            count+=1

    plt.subplots_adjust(left=0.,
                bottom=0.,
                right=1,
                top=1,
                wspace=-0.5,
                hspace=0)
    plt.text(x_pos,-280, model, size=13)
    plt.text(-80, -8, f' {round(float(mIoU[0])*100,2)} {round(float(mIoU[1])*100,2)}', size=11)
    plt.text(-80,22, f' {round(float(mIoU[2])*100,2)} {round(float(mIoU[3])*100,2)}', size=11)

    fig.add_artist(lines.Line2D([0.42, 0.58], [0.5, 0.5], linewidth=1))
    fig.add_artist(lines.Line2D([0.498, 0.498], [0.448, 0.54], linewidth=1))
    # plt.text(0.5,0, 'mask', horizontalalignment='center', verticalalignment='top')

    plt.savefig(f'{model}_{dataset}_block.png', bbox_inches = 'tight', pad_inches = 0)
    plt.show()
        



def get_roi_mask(h, n_channels):
    img = torch.zeros([1,h,h]).cuda()
    x = [i for i in np.arange(-h//2,h//2,1)]
    y = [i for i in np.arange(-h//2,h//2,1)]

    for i in x:
        for j in y:
            if i**2+j**2<(h/2)**2:
                img[:,i+h//2,j+h//2]=1
            else:
                img[:,i+h//2,j+h//2]=0

    roi_mask = img[:,:h-1,:h-1]
    roi_mask = roi_mask.unsqueeze(0)

    inverse_roi_mask = 1-roi_mask
    # inverse_roi_mask = -inverse_roi_mask
    img_inverse_roi  = torch.cat([inverse_roi_mask]*n_channels, dim=1)
    return roi_mask, inverse_roi_mask, img_inverse_roi

def predict_img(model, net, device, classes, dataset, scale, angle, n_channels=1):
    # save_patches = 'data/'+dataset+'/'+model+'/'+str(scale)+'_'+str(angle)+'/'
    # save_patches = 'data/'+dataset+'/'+model+'/eg/'
    save_patches = 'evaluate_data/'+model+'_'
    if not os.path.exists(save_patches):
        os.makedirs(save_patches)
    net.eval()

    if dataset=='CRAG':
        test_dataset  = CRAG(image_set='test', mask_channel=2, factor=scale)

    elif dataset=='GlaS':
        test_dataset  = GlaS(image_set='test', mask_channel=2,  factor=scale)

    elif dataset=='Kumar':
        test_dataset  = Kumar(image_set='test', mask_channel=2, factor=scale, angle=angle)

    elif 'Mosaics' in dataset:
        test_dataset  = CustomImageSet('eg', sample_weight=None, mask_channel=6,  factor=scale, visualisation=False)

    print('Num of images:',test_dataset.__len__())
    if scale<1.4:
        batch_size=12
    else:
        batch_size=4
    val_loader = DataLoader(test_dataset, batch_size=1, shuffle=False, num_workers=4, pin_memory=True)

    IMG_Metrics=Metrics(classes+1, ignore_index=[classes])
    metrics = Metrics(classes+1, ignore_index=[classes])
    count=0
    img_count = 0
    miou_averaged = 0

    out_feats = []
    k = 255//(classes+1)    
    for batch in val_loader:
        with torch.no_grad():
            imgs = batch['image'].to(device=device, dtype=torch.float32)
            masks = batch['mask'].to(device=device, dtype=torch.float32)
            names = batch['name']

            roi_mask, inverse_roi_mask, img_inverse_roi = get_roi_mask(imgs.shape[-1]+1, n_channels)
            inverse_roi_mask = classes*inverse_roi_mask

            imgs  = tf.rotate(imgs, angle, fill=[1]*n_channels)*roi_mask+img_inverse_roi
            masks = tf.rotate(masks,angle, fill=[classes])

            output = F.softmax(net(imgs), dim=1)

            torch_masks = torch.argmax(masks,dim=1,  keepdim=True)
            torch_preds = torch.argmax(output,dim=1, keepdim=True)

            torch_preds = torch_preds*roi_mask+inverse_roi_mask
            torch_preds = torch_preds.squeeze(1).type(torch.int8)

            torch_masks = torch_masks*roi_mask+inverse_roi_mask
            torch_masks = torch_masks.squeeze(1).type(torch.int8)

            for x in range(torch_preds.shape[0]):
                _,_,iou = metrics.get_img_iou(torch_preds[x],torch_masks[x])
                iou = round(iou.mean().item(),4)
                temp_name = names[x].split('/')[-1]
                temp_pred_name = save_patches+temp_name[:-4]+'_'+str(iou)+'.png'
                print(temp_pred_name)
                heatmap = (torch_preds[x].cpu().numpy()*k).astype(np.uint8)
                heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
                cv2.imwrite(temp_pred_name, heatmap)
            img_count+=torch_preds.shape[0]


def equ_err(net, dataset, scale_1, scale_2):
    err_mat = torch.empty(1,0).cuda()
    net.eval()
    channels = 12
    if dataset=='BCSS':
        test_dataset_1  = BCSS(image_set='test', factor=scale_1)
        test_dataset_2  = BCSS(image_set='test', factor=scale_2)
    elif dataset=='Kumar':
        test_dataset_1  = Kumar(image_set='test', factor=scale_1)
        test_dataset_2  = Kumar(image_set='test', factor=scale_2)

    if scale_2>3.4:
            batch_size=1
    else:
        batch_size=40
    val_loader_1 = DataLoader(test_dataset_1, batch_size=batch_size, shuffle=False, num_workers=2, pin_memory=True)
    val_loader_2 = DataLoader(test_dataset_2, batch_size=batch_size, shuffle=False, num_workers=2, pin_memory=True)
    count = 0
    for batch_1, batch_2 in zip(val_loader_1, val_loader_2):
        with torch.no_grad():
            imgs_1 = batch_1['image'].cuda() #to(device=device, dtype=torch.float32))
            imgs_2 = batch_2['image'].cuda() #to(device=device, dtype=torch.float32))
            pred_list_1  = net(imgs_1)
            pred_list_2  = net(imgs_2)
            err = measure_error(pred_list_1, pred_list_2, dataset)
            # err = measure_error_ours(pred_list_1, pred_list_2)
            err_mat = torch.cat([err_mat,err], dim=1)
            count+=imgs_1.shape[0]
            # if count>=300:
            #     break
    
    print('err_mat size:',err_mat.size())
    mean = err_mat.mean(dim=1).cpu().numpy()
    mean = np.around(mean, decimals=4)
    # std = err_mat.std(dim=1).cpu().numpy()
    # print('scale:', scale_2)
    # print('mean err:', mean)
    # print('std:', std)
    # print(scale_2, mean)
    # return mean
    return err_mat.cpu().numpy()

def measure_error(f_1, f_2, dataset):
    '''
    args:
        f_1: phi(f), Dictionary of Dictionary
        f_2: phi(Ls[f]), Dictionary of Dictionary
    '''
    num_datapoints = f_1[0].shape[0]
    # print(type(f_1))
    # for i in range(5):
    #     f_1[i] = F.softmax(f_1[i], dim=1)
    #     f_2[i] = F.softmax(f_2[i], dim=1)

    if dataset=='BCSS':
        if f_1[0].shape[2]==512:
            pass
        else:
            f_3 = f_1
            f_1 = f_2
            f_2 = f_3
    if dataset=='Kumar':
        if f_1[0].shape[2]==400:
            pass
        else:
            f_3 = f_1
            f_1 = f_2
            f_2 = f_3
            
    err_mat = torch.empty(0, num_datapoints).cuda()
    i = -1
    err = torch.norm(f_1[i]-F.interpolate(f_2[i],size=(f_1[i].shape[2],f_1[i].shape[3]), mode='bilinear', align_corners=True), p=2, dim=(1,2,3))/\
                    torch.norm(f_1[i], p=2,dim=(1,2,3))
    err = err.view(-1, num_datapoints)
    return err


def measure_error_ours(f_1, f_2):
    '''
    args:
        f_1: phi(f), Dictionary of Dictionary
        f_2: phi(Ls[f]), Dictionary of Dictionary
    '''
    channels = 12
    num_datapoints = f_1[0].shape[0]
    if f_1[0].shape[2]>f_2[0].shape[2]:
        pass
    else:
        f_3 = f_1
        f_1 = f_2
        f_2 = f_3
    err_mat = torch.empty(0, num_datapoints).cuda()
    for f1, f2 in zip(f_1,f_2):
        print(f1.shape, f2.shape)
    for f1, f2 in zip(f_1,f_2):
        for j in range(5):
            f_2_b = f2[:,j*channels:(j+1)*channels,:,:]
            for k in range(5):
                f_1_b = f1[:,k*channels:(k+1)*channels,:,:]
                err = torch.norm(f_2_b-F.interpolate(f_1_b,size=(f_2_b.shape[2],f_2_b.shape[3]), mode='bilinear', align_corners=True), p=2, dim=(1,2,3))/\
                      torch.norm(F.interpolate(f_1_b,size=(f_2_b.shape[2],f_2_b.shape[3]), mode='bilinear', align_corners=True), p=2,dim=(1,2,3))
                err = err.view(-1, num_datapoints)
                print('err:',err, err.size())
                err_mat = torch.cat([err_mat, err], dim=0)
        print('layer:', err_mat.shape)
    return err_mat

def get_args():
    parser = argparse.ArgumentParser(description='Predict masks from input images',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--weight', '-w', type=str, metavar='FILE',
                        help="Specify the file in which the model is stored")
    parser.add_argument('-d', '--data', dest='data', type=str, default='Mosaics',
                        help='dataset')
    parser.add_argument('-n', '--name', dest='name', type=str, default='CNN',
                        help='name')
    parser.add_argument('-m', '--mode', dest='mode', type=str, default='predict',
                        help='name')
    parser.add_argument('-f', '--n_filters', dest='n_filters', type=int, default=12,
                        help='num of filters')
    parser.add_argument('-k', '--k_size', dest='k_size', type=int, default=3,
                        help='k_size')
    parser.add_argument('-r', '--n_rotation', dest='n_rotation', type=int, default=None,
                        help='num of rotations')
    
    return parser.parse_args()

def count_your_model(model, x, y):
        # your rule here
        pass

if __name__ == "__main__":
    n_channels=3
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"
    args = get_args()
    torch.cuda.set_device(0)
    if args.data=='BCSS' or 'Mosaic' in args.data:
        classes=5
    else:
        classes=2
        
    if 'Mosaic' in args.data:
        n_channels=1

    if args.name=='CNN':
        if args.mode=='predict':
            net = UNet_CNN(n_channels=n_channels, n_classes=classes, filters=args.n_filters, \
                            bilinear=True, flag=False, kernel_size=args.k_size).cuda()
        else:
            net = UNet_CNN(n_channels=n_channels, n_classes=classes, filters=args.n_filters, \
                            bilinear=True, flag=True, kernel_size=args.k_size).cuda()
    elif args.name=='E(2)CNN' or args.name=='H-Nets':
        if args.mode=='predict':
            net = e2UNet(n_channels=n_channels, n_classes=classes, filters=args.n_filters, rotations=args.n_rotation, kernel_size=args.k_size).cuda()

    print('--'*10, 'kernel_size:', args.k_size, '--'*10, 'classes:', classes, '--'*10, 'model:', args.name, '--'*10, 'dataset:', args.data, '--'*10)

    # summary(net, (3, 512, 512))

    params = [p.nelement() for p in net.parameters() if p.requires_grad]
    num = sum(params)
    print(f'num of trainable parameters:{num}')
    
    print("Loading model {}".format(args.weight), 'num of angles of filters:', args.n_rotation)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f'Using device {device}')
    net.to(device=device)

    if args.mode=='predict':
        checkpoint = torch.load(args.weight, map_location=device)
        state_dict = []
        # for n, p in checkpoint.items():
            # if "total_ops" not in n and "total_params" not in n:
            # state_dict.append((n[7:], p))
            # if 'out' in n:
        #     print(n, p.shape)
        # state_dict = dict(state_dict)
        # net.load_state_dict(state_dict)
        net.load_state_dict(checkpoint)
        mIoU_list = []
        feat_list = []
        r = 2**0.25
        # scales = [round(0.25*r**i,2) for i in range(15,17)]
        # scales = [0.25, 0.5 , 1, 2, 4]
        # print('testing scales:', scales)
        # for factor in scales:
        #     mIoU = predict_img('unet', net, device, classes, args.data, factor)
        #     mIoU_list.append(mIoU)
        # print(mIoU_list)

        # scales = [round(0.25*r**i,2) for i in range(4,13)]
        scales = [1]
        angles = [0]
        # angles = [10*i for i in range(0, 36)]
        print('testing angle:', angles, 'testing scales:', scales)
        mIoU_array = np.zeros([len(scales), len(angles)])
        for factor, i in zip(scales,[idx for idx in range(len(scales))]):
            for angle,j in zip(angles, [idx for idx in range(len(angles))]):
                predict_img(args.name, net, device, classes, args.data, factor, angle, n_channels)
                # pred_name = glob.glob(f'data/{args.data}/{args.name}/eg/*png')
                # pred_name.sort()
                # order = [1,3,0,2]
                # reordered = [pred_name[i] for i in order]
                # print(reordered)
                # vis_pred(reordered, args.name, args.data)

        #     feat_list.append(feats)
        #     print('angle:', angle, 'feats shape:', feats.shape)
        # feat_list = torch.cat(feat_list,dim=1)
        # print('feat_list shape:', feat_list.shape)
        # std_per_class = feat_list.std(dim=1)
        # print('std shape:', feat_list.shape)
        # std_all_class = std_per_class.mean(dim=1).cpu().numpy()
        # print('std mean shape:', std_all_class.shape)
        # np.save(f'{args.name}_feat.npy', std_all_class)
        # for i in range(std_all_class.shape[0]):
        #     cv2.imwrite(f'{args.name}_std_{str(i)}.png', std_all_class[i]*255)

        # print(mIoU_list, np.array(mIoU_list).mean())
        print(mIoU_array, mIoU_array.mean())


    else:
        checkpoint = torch.load(args.weight, map_location=device)
        # state_dict = []
        # for n, p in checkpoint.items():
        #     if "total_ops" not in n and "total_params" not in n:
        #     state_dict.append((n[7:], p))
        #     if 'out' in n:
        #     print(n, p.shape)
        # state_dict = dict(state_dict)
        # net.load_state_dict(state_dict)
        net.load_state_dict(checkpoint)
        if args.data=='BCSS':
            N = 1200
            err_all = np.empty([0,1222])
        elif args.data=='Kumar':
            N = 224
            err_all = np.empty([0,224])

        r = 2**0.25
        scales = [round(0.25*r**i,2) for i in range(0,17)]
        # scales = [2]
        print('testing scales:', scales)
        for factor in scales:
            if factor==1:
                continue
            else:
                err = equ_err(net, args.data, 1, factor)
                err_all = np.vstack([err_all, err])
                print(err_all.shape)
        err_all=np.around(err_all[:,:N], decimals=3)
        print(err_all.mean())