import os
import cv2
import glob
import torch
import time
import logging
import argparse
import datetime
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
from sklearn.metrics import confusion_matrix
import torchvision.transforms.functional as tf

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
    img_inverse_roi  = torch.cat([inverse_roi_mask*255]*n_channels, dim=1)
    return roi_mask, inverse_roi_mask, img_inverse_roi

def predict_img(model, net, device,classes, dataset, n_channels=1, subset='test'):
    # save_patches = 'evaluate_data/'+dataset+'/'+model+'/'+subset+'/'
    save_patches = 'evaluate_data/'+model+'_'+subset+'_'

    if not os.path.exists(save_patches):
        os.makedirs(save_patches)
    net.eval()

    if dataset=='CRAG':
        if subset=='test':
            test_dataset  = CRAG(image_set=subset, mask_channel=classes, factor=1)
        else:
            test_dataset  = CRAG(image_set=subset, mask_channel=classes+1, factor=1)

    elif dataset=='GlaS':
        if subset=='test':
            test_dataset  = GlaS(image_set=subset, mask_channel=classes, factor=1)
        else:
            test_dataset  = GlaS(image_set=subset, mask_channel=classes+1, factor=1)

    elif 'Mosaics' in dataset:
        if subset=='test':
            test_dataset  = CustomImageSet(subset, mask_channel=classes, factor=1, visualisation=False)
        else:
            test_dataset  = CustomImageSet(subset, mask_channel=classes+1, factor=1, visualisation=False)



    print('--------'*20)
    print('Num of images for evaulation:',test_dataset.__len__())
    batch_size=1

    val_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False, num_workers=2, pin_memory=True)
    IMG_Metrics=Metrics(classes+1, ignore_index=[classes])
    metrics = Metrics(classes+1, ignore_index=[classes])
    count=0
    img_count = 0
    miou_averaged = 0
    out_feats = []
    mIoU_list = []


    for batch in val_loader:
        with torch.no_grad():
            imgs = batch['image'].cuda()
            true_masks = batch['mask'].cuda()
            names = batch['name']

            roi_mask, inverse_roi_mask, img_inverse_roi = get_roi_mask(imgs.shape[-1]+1, n_channels)
            inverse_roi_mask = classes*inverse_roi_mask


            # pooling over R&S 
            true_masks = torch.argmax(true_masks,dim=1,  keepdim=True)
            # true_masks = true_masks*roi_mask+inverse_roi_mask
            true_masks = true_masks.squeeze(1).type(torch.int8)

            # F_out = net(imgs)
            # Final_y_hat = F.softmax(F_out ,dim=1)
            # Final_y_hat = torch.argmax(Final_y_hat,dim=1)
            
            '''
            # pixel ensemble alone scales
            print('scale ens')
            pred_list = net(imgs)
            pred_list = [pred_list[i].unsqueeze(1) for i in range(1, len(pred_list))] 
            F_out  = torch.cat(pred_list, dim=1)                                 # shape of [B, S, C, H, W]
            F_pred = F.softmax(F_out,dim=2)                                      # shape of [B, S, C, H, W]
            F_pred_temp = F_pred.clone()
            F_max = F_pred_temp.max(dim=2, keepdim=True)[0]                           # shape of [B, S, 1, H, W]
            F_pred_temp[F_pred_temp==F_max] =-1                                   # shape of [B, S, C, H, W]
            
            F_second_Max = F_pred_temp.max(dim=2, keepdim=True)[0]     # shape of [B, S, 1, H, W]
            F_distance  = (F_max-F_second_Max)                         # shape of [B, S, 1, H, W]
            F_distance  = F.softmax(F_distance,dim=1)                  # shape of [B, S, 1, H, W]
            Ensembled_prob= (F_pred*F_distance).sum(dim=1)             # shape of [B, C, H, W]
            Final_y_hat= torch.argmax(Ensembled_prob,dim=1)            # shape of [B, H, W]
            '''

            # '''
            # pixel distance-based selection alone scales
            pred_list = net(imgs)
            print('scale select:', len(pred_list))
            pred_list = [pred_list[i].unsqueeze(1) for i in range(len(pred_list))] 
            F_out  = torch.cat(pred_list, dim=1)                                 # shape of [B, S, C, H, W]
            F_pred = F.softmax(F_out,dim=2)                                      # shape of [B, S, C, H, W]
            F_pred_temp = F_pred.clone()
            F_max = F_pred_temp.max(dim=2, keepdim=True)[0]                           # shape of [B, S, 1, H, W]
            F_pred_temp[F_pred_temp==F_max] =-1                                   # shape of [B, S, C, H, W]
            
            F_second_Max = F_pred_temp.max(dim=2, keepdim=True)[0]     # shape of [B, S, 1, H, W]
            F_distance  = (F_max-F_second_Max)                         # shape of [B, S, 1, H, W]
            # prinr('difference:',F_distance)
            Max_d_idx = F_distance.argmax(1)                                 # shape of [B, 1, H, W]
            F_y_hat= torch.argmax(F_pred,dim=2)                                  # shape of [B, S, H, W]
            Final_y_hat = torch.gather(F_y_hat, 1, Max_d_idx)
            # '''
            
            # Final_y_hat = Final_y_hat*roi_mask+inverse_roi_mask
            Final_y_hat = Final_y_hat.squeeze(1).type(torch.int8)
            
            # print('labels:',torch.unique(true_masks), torch.unique(Final_y_hat))

            metrics.add(Final_y_hat.view(-1), true_masks.view(-1)) 
            
            # '''
            for x in range(Final_y_hat.shape[0]):
                miou,_,iou = metrics.get_img_iou(Final_y_hat[x],true_masks[x])
                k = 255//(classes+1)
                k = 255//(classes-1)
                temp_name = names[x].split('/')[-1]
                temp_name_1 = save_patches+temp_name[:-4]+'_'+str(round(miou,4))+'.png'
                heatmap = (Final_y_hat[x].cpu().numpy()*k).astype(np.uint8)
                heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
                
                # roi_mask = roi_mask.squeeze(0).permute(1,2,0).cpu().numpy()
                # img_inverse_roi = torch.permute(img_inverse_roi.squeeze(0), [1,2,0]).cpu().numpy()
                # heatmap = heatmap*roi_mask+img_inverse_roi
                cv2.imwrite(temp_name_1, heatmap)
                print('img:', img_count ,temp_name_1)
                # fs = round(float(temp_name.split('_')[5]),2)
                # fr = int(temp_name.split('_')[7].split('.')[0])
                # pred_record = [fs, fr, miou]
                # mIoU_list.append(pred_record)
            # '''
                img_count+=imgs.shape[0]
        # if img_count%50==0:
        #     print(f'{datetime.datetime.now()}, {img_count} images evaluated!')
        # if img_count%20==0:
        #     print(f'{datetime.datetime.now()}, {img_count} images evaluated!')
        #     break
    cm = metrics._confusion_matrix
    print('iou list:')
    print(mIoU_list)
    # print('cm_sum', cm.sum())
    # print('num of images tested:', img_count)
    if classes==2:
        print(f'{datetime.datetime.now()}, iou: {metrics.iou(average=False)}, {round(metrics.iou(average=True), 4)}')
        return round(metrics.iou(average=False)[1].item()*100, 2), out_feats
    else:
        print(f'{datetime.datetime.now()}, iou: {metrics.iou(average=False)}, {round(metrics.iou(average=True), 4)}')
        return round(metrics.iou(average=True)*100, 2), out_feats

def get_args():
    parser = argparse.ArgumentParser(description='Predict masks from input images',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--weight', '-w', type=str, metavar='FILE',
                        help="Specify the file in which the model is stored")
    parser.add_argument('-d', '--data', dest='data', type=str, default='Mosaics',
                        help='dataset')
    parser.add_argument('-s', '--subset', dest='subset', type=str, default='test',
                        help='dataset')
    parser.add_argument('-o', '--order', dest='order', type=int, default=2,
                        help='order')
    parser.add_argument('-a', '--name', dest='name', type=str, default='RST-NJet',
                        help='name')
    parser.add_argument('-r', '--n_rotation', dest='n_rotation', type=int, default=8,
                        help='num of filters')
    parser.add_argument('-k', '--n_scales', dest='n_scales', type=int, default=4,
                        help='num of filters')
    parser.add_argument('-n', '--n_filters', dest='n_filters', type=int, default=16,
                        help='num of filters')
    parser.add_argument('-c', '--selection', dest='selection', type=int, default=2,
                        help='srf')
    return parser.parse_args()

def count_your_model(model, x, y):
        # your rule here
        pass

if __name__ == "__main__":
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"
    args = get_args()
    torch.cuda.set_device(0)
    if 'Mosaic' in args.data:
        classes=5
        n_channels=1

    else:
        classes=2
        n_channels=3
    # scale_offset = [0,1,2,3,4,5]
    scale_offset = [0,1,1,2,2,3]
    
    k_factor=2.5
    net = UNet_R(n_channels=n_channels, n_classes=classes, filters=args.n_filters, init_order=args.order, \
                    bilinear=True, init_scale=0.99, \
                    angles=[torch.tensor(0+i*math.pi/(args.n_rotation/2)) for i in range(args.n_rotation)],\
                    n_scales=args.n_scales, rotation_size=1, learn_sigma=True, k=k_factor, \
                    scale_offset=scale_offset, selection=args.selection).cuda()

    print('-'*10, 'model name:', args.name, 'Nr:', args.n_rotation,\
            'Ns:', args.n_scales, '-'*10, 'dataset:', args.data, '-', \
            args.subset, '--factor:', k_factor, '-'*5,'selection:', args.selection)

    # summary(net, (3, 512, 512))

    params = [p.nelement() for p in net.parameters() if p.requires_grad]
    num = sum(params)
    print(f'num of trainable parameters:{num}')
    
    print("Loading model {}".format(args.weight), 'num of rotations of filters:', args.n_rotation)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f'Using device {device}')
    net.to(device=device)

    checkpoint = torch.load(args.weight, map_location=device)
    net.load_state_dict(checkpoint)

    '''    
    state_dict = []
    for n, p in checkpoint.items():
        if 'scale' in n:
            print(n, p.shape, p)
            p = p[2].view(1)
            state_dict.append((n, p))
        elif 'eta' in n:
            print(n, p.shape, p)
            p = p[:,2].view(1,1)
            state_dict.append((n, p))
        else:
            state_dict.append((n, p))
    state_dict = dict(state_dict)
    print('---'*20)
    net.load_state_dict(state_dict)
    '''

    mIoU_list = []
    feat_list = []
    mIoU, feats = predict_img(args.name, net, device, classes, args.data, n_channels, args.subset)


