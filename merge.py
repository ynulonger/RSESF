import os
import cv2
import glob
import torch
import logging
import argparse
import numpy as np
import torch.nn as nn
from utils.metrics import *
from utils.dataset import *
import torch.nn.functional as F
import matplotlib.pyplot as plt
from torchsummary import summary
from models.unet_model import UNet
from torch.autograd import Variable
from torch.utils.data import DataLoader
from sklearn.metrics import confusion_matrix

def predict_img(model, net, device,classes, dataset, scale):
    save_patches = 'data/'+dataset+'/'+model+'/'
    if not os.path.exists(save_patches):
        os.makedirs(save_patches)
    net.eval()

    if dataset=='BCSS':
        test_dataset  = BCSS(image_set='test', factor=scale)

    elif dataset=='CRAG':
        test_dataset  = CRAG(image_set='test',  mask_channel=2)

    elif dataset=='Kumar':
        test_dataset  = Kumar(image_set='test',  mask_channel=2)

    val_loader = DataLoader(test_dataset, batch_size=1, shuffle=False, num_workers=2, pin_memory=True)

    IMG_Metrics=Metrics(classes)
    metrics = Metrics(classes)
    count=0
    miou_averaged = 0
    for batch in val_loader:
        with torch.no_grad():
            imgs = Variable(batch['image'].to(device=device, dtype=torch.float32))
            masks = batch['mask'].to(device=device, dtype=torch.float32)
            names = batch['name']
            output = F.softmax(net(imgs), dim=1)
            # print('img size:', imgs.size())
            # print('output size:', output.size())

            torch_masks = torch.argmax(masks,dim=1)
            torch_preds = torch.argmax(output,dim=1)
            metrics.add(torch_preds.squeeze(1).view(-1), torch_masks.squeeze(1).view(-1))

            output = output.cpu().numpy()
            masks = masks.cpu().numpy()
            masks = np.argmax(masks, axis=1).squeeze()
            preds = np.argmax(output, axis=1).squeeze()

            if len(masks.shape)==2: 
                masks=np.expand_dims(masks,axis=0)
                preds=np.expand_dims(preds,axis=0)

            # for i in range(preds.shape[0]):
            #     img_iou = metrics.get_img_iou(torch_preds[i], torch_masks[i]).item()
            #     heatmap = (preds[i]*(255/4)).astype(np.uint8)
            #     heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_RAINBOW)
            #     cv2.imwrite(save_patches+'/'+names[i].split('.')[0]+'_'+str(img_iou)[:5]+'.png', heatmap)
            #     count+=1

    # miou_list = metrics._iou_list
    cm = metrics._confusion_matrix
    print(f'iou: {metrics.iou(average=True)}, {metrics.iou(average=False)}')
    # miou = metrics.iou(average=False)
    # print(f'mean: {miou.mean()}, {miou}')

def get_args():
    parser = argparse.ArgumentParser(description='Predict masks from input images',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-d', '--data', dest='data', type=str, default='BCSS',
                        help='dataset')
    parser.add_argument('-s', '--srf', dest='srf', type=str, default='True',
                        help='srf')
    parser.add_argument('-f', '--factor', dest='factor', type=float, default=1,
                        help='factor')

    return parser.parse_args()

def count_your_model(model, x, y):
        # your rule here
        pass

if __name__ == "__main__":
    filters=64
    n_channels=3
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"
    args = get_args()
    torch.cuda.set_device(0)
    if args.data=='BCSS':
        classes=5
    else:
        classes=2

    if args.srf=='False' or args.srf=='false':
        args.srf=False
    print(args.srf)

    net_1 = UNet(n_channels=n_channels, n_classes=classes, filters=filters, bilinear=True, srf=args.srf).cuda()
    net_2 = UNet(n_channels=n_channels, n_classes=classes, filters=filters, bilinear=True, srf=args.srf).cuda()
    net_3 = UNet(n_channels=n_channels, n_classes=classes, filters=filters, bilinear=True, srf=args.srf).cuda()

    # summary(net, (3, 512, 512))
    

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    logging.info(f'Using device {device}')
    net_1.to(device=device)
    net_2.to(device=device)
    net_3.to(device=device)

    checkpoint_1 = torch.load("checkpoints/BCSS/0.001_ce_16_70_srf_0.25.pth", map_location=device)
    checkpoint_2 = torch.load("checkpoints/BCSS/0.001_ce_16_70_srf_0.5.pth", map_location=device)
    checkpoint_3 = torch.load("checkpoints/BCSS/0.001_ce_16_70_srf.pth", map_location=device)

    state_dict_1 = []
    state_dict_2 = []
    state_dict_3 = []

    sigma_1 = []
    sigma_2 = []
    sigma_3 = []

    for (n_1, p_1), (n_2, p_2), (n_3, p_3) in zip(checkpoint_1.items(),checkpoint_2.items(),checkpoint_3.items()):
        if "total_ops" not in n_1 and "total_params" not in n_1:
            state_dict_1.append((n_1, p_1))
            state_dict_2.append((n_2, p_2))
            state_dict_3.append((n_3, p_3))
            # print(n_1,p_1.shape,'---',n_2,p_2.shape,'---',n_3,p_3.shape)
        if 'scale' in n_1:
            print(n_1,2**p_1.item(),'---',2**p_2.item(),'---',2**p_3.item())
            sigma_1.append(2**p_1.item())
            sigma_2.append(2**p_2.item())
            sigma_3.append(2**p_3.item())

    x_values = [i for i in range(1,19,1)]
    print(x_values)
    plt.plot(x_values, sigma_1, label='scale=0.25')
    plt.plot(x_values, sigma_2, label='scale=0.5')
    plt.plot(x_values, sigma_3, label='scale=1')
    plt.xticks(x_values)
    plt.xlabel('layer')
    plt.ylabel('sigma')
    plt.legend()
    plt.savefig('sigma.png')

    state_dict_1 = dict(state_dict_1)
    state_dict_2 = dict(state_dict_2)
    state_dict_3 = dict(state_dict_3)

    net_1.load_state_dict(state_dict_1)
    net_2.load_state_dict(state_dict_2)
    net_3.load_state_dict(state_dict_3)

    # for name,parameters in net_1.named_parameters():
	   #  print(name,':',parameters.size())
    # print(net_1..named_parameters('inc.double_conv.0')
    # print(net_2.inc.double_conv.0.filters.size())
    # print(net_3.inc.double_conv.0.filters.size())

    # predict_img('unet', net, device, classes, args.data, args.factor)
