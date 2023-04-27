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
from utils.dataset import *
import torch.nn.functional as F
import matplotlib.pyplot as plt
from torch.autograd import Variable
import torchvision.transforms.functional as tf


def get_roi_mask(h, n_channels):
    img = torch.zeros([1,h,h])
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
    # cv2.imwrite('roi_mask.png',roi_mask.squeeze().numpy()*250)
    img_inverse_roi  = torch.cat([inverse_roi_mask*255]*n_channels, dim=1)
    return roi_mask, inverse_roi_mask, img_inverse_roi


def gen_img_gt(dataset):

    save_imgs = '/scratch/yy3u19/DataSets/'+dataset+'/evaulate-imgs/'
    save_gts = '/scratch/yy3u19/DataSets/'+dataset+'/evaulate-gts/'
    save_masks = '/scratch/yy3u19/DataSets/'+dataset+'/evaulate-masks/'


    if not os.path.exists(save_imgs):
        os.makedirs(save_imgs)
    if not os.path.exists(save_gts):
        os.makedirs(save_gts)
    if not os.path.exists(save_masks):
        os.makedirs(save_masks)

    factors=np.load("/scratch/yy3u19/DataSets/factors.npy", allow_pickle=True).flat[0]

    if dataset=='CRAG':
        img_name_list  = glob.glob('/scratch/yy3u19/DataSets/CRAG/TEST/img/*')
        gt_name_list  = glob.glob('/scratch/yy3u19/DataSets/CRAG/TEST/labelcol/*')
        scales = factors.get('CRAG').get('scales')
        orientations = factors.get('CRAG').get('angles')
        n_channels=3
        classes=2
    if dataset=='GlaS':
        img_name_list  = glob.glob('/scratch/yy3u19/DataSets/GlaS/Test_patch/*')
        gt_name_list  = glob.glob('/scratch/yy3u19/DataSets/GlaS/Test_patch_mask/*')
        scales = factors.get('GlaS').get('scales')
        orientations = factors.get('GlaS').get('angles')
        n_channels=3
        classes=2
    elif dataset=='Mosaics':
        img_name_list  = glob.glob('/scratch/yy3u19/DataSets/Mosaics/test-imgs/*')
        gt_name_list  = glob.glob('/scratch/yy3u19/DataSets/Mosaics/test-gts/*')
        scales = factors.get('Texture').get('scales')
        orientations = factors.get('Texture').get('angles')
        n_channels=1
        classes=5

    print('scales:', scales.shape, scales[:,0].mean(), 'angles:', orientations.shape, orientations[:,0].mean())
    for img_name,gt_name,scale, orientation in zip(img_name_list,gt_name_list,scales, orientations):
        print('generating', img_name)
        if dataset=='Mosaics':
            img = cv2.imread(img_name, flags=0) 
            img = torch.tensor(img).unsqueeze(0).unsqueeze(0)
            mask = cv2.imread(gt_name, flags=0).astype(np.uint8)
        else:
            img = cv2.imread(img_name)
            img = torch.tensor(img).permute(2,0,1).unsqueeze(0)
            mask = (cv2.imread(gt_name, flags=0)>=1).astype(np.uint8)
        mask = torch.tensor(mask).unsqueeze(0).unsqueeze(0)
        roi_mask, inverse_roi_mask, img_inverse_roi = get_roi_mask(img.shape[-1]+1, n_channels)
        inverse_roi_mask = classes*inverse_roi_mask

        name = img_name.split('/')[-1]
        # s = scales[idx]
        # r = orientations[idx]
        # print('scaling factors:', scale)
        # print('rotation factors:', orientation)
        idx=0
        for fs,fr in zip(scale, orientation):
            TEMP_img  = tf.rotate(img, int(fr), fill=[1]*n_channels)*roi_mask+img_inverse_roi
            if dataset=='Mosaics':
                TEMP_img = TEMP_img.squeeze().numpy()
            else:
                TEMP_img = TEMP_img.squeeze().permute(1,2,0).numpy()
            fr = int(fr)
            fs = round(fs,2)
            TEMP_mask = tf.rotate(mask, fr, fill=[classes])*roi_mask+inverse_roi_mask
            TEMP_mask = TEMP_mask.squeeze().numpy()
            # print('unique:', np.unique(mask), np.unique(TEMP_mask))
            w = int(fs*512)

            TEMP_img  = cv2.resize(TEMP_img, (w,w), interpolation=cv2.INTER_LINEAR)
            TEMP_mask = cv2.resize(TEMP_mask, (w,w), interpolation=cv2.INTER_NEAREST)
            print(TEMP_img.shape, TEMP_mask.shape)

            heatmap = (TEMP_mask*255.0/(classes+1)).astype(np.uint8)
            heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)

            cv2.imwrite(save_imgs+name[:-1]+'_'+str(idx)+'_s_'+str(fs)+'_r_'+str(fr)+'.png', TEMP_img)
            cv2.imwrite(save_gts+name[:-1]+'_'+str(idx)+'_s_'+str(fs)+'_r_'+str(fr)+'.png', TEMP_mask)
            cv2.imwrite(save_masks+name[:-1]+'_'+str(idx)+'_s_'+str(fs)+'_r_'+str(fr)+'.png', heatmap)
            idx+=1
            break

# gen_img_gt('GlaS')
# gen_img_gt('CRAG')
# gen_img_gt('Mosaics')


def gen_vis_img_gt(dataset):

    save_imgs = '/scratch/yy3u19/DataSets/'+dataset+'/vis-imgs/'
    save_gts = '/scratch/yy3u19/DataSets/'+dataset+'/vis-gts/'
    save_masks = '/scratch/yy3u19/DataSets/'+dataset+'/vis-masks/'

    if not os.path.exists(save_imgs):
        os.makedirs(save_imgs)
    if not os.path.exists(save_gts):
        os.makedirs(save_gts)
    if not os.path.exists(save_masks):
        os.makedirs(save_masks)

    factors=np.load("/scratch/yy3u19/DataSets/Texture_2000_copies_of_1_img.npy", allow_pickle=True).flat[0]

    if dataset=='CRAG':
        img_name_list  = glob.glob('/scratch/yy3u19/DataSets/CRAG/TEST/img/*')
        gt_name_list  = glob.glob('/scratch/yy3u19/DataSets/CRAG/TEST/labelcol/*')
        # scales = factors.get('CRAG').get('scales')
        # orientations = factors.get('CRAG').get('angles')
        scales = factors.get('scales')
        orientations = factors.get('angles')
        n_channels=3
        classes=2
    if dataset=='GlaS':
        img_name_list  = glob.glob('/scratch/yy3u19/DataSets/GlaS/Test_patch/*')
        gt_name_list  = glob.glob('/scratch/yy3u19/DataSets/GlaS/Test_patch_mask/*')
        scales = factors.get('scales')
        orientations = factors.get('angles')
        n_channels=3
        classes=2
    elif dataset=='Mosaics':
        img_name_list  = glob.glob('/scratch/yy3u19/DataSets/Mosaics/test-imgs/*')
        img_name_list.sort()
        gt_name_list  = glob.glob('/scratch/yy3u19/DataSets/Mosaics/test-gts/*')
        gt_name_list.sort()
        scales = factors.get('scales')
        orientations = factors.get('angles')
        n_channels=1
        classes=5

    # img_name = img_name_list[0]
    # gt_name = gt_name_list[0]
    img_name = '/scratch/yy3u19/DataSets/CRAG/TEST/img/test_40_0_1.png'
    gt_name  = '/scratch/yy3u19/DataSets/CRAG/TEST/labelcol/test_40_0_1.png'
    if dataset=='Mosaics':
        img = cv2.imread(img_name, flags=0) 
        img = torch.tensor(img).unsqueeze(0).unsqueeze(0)
        mask = cv2.imread(gt_name, flags=0).astype(np.uint8)
    else:
        img = cv2.imread(img_name)
        img = torch.tensor(img).permute(2,0,1).unsqueeze(0)
        mask = (cv2.imread(gt_name, flags=0)>=1).astype(np.uint8)
    mask = torch.tensor(mask).unsqueeze(0).unsqueeze(0)
    roi_mask, inverse_roi_mask, img_inverse_roi = get_roi_mask(img.shape[-1]+1, n_channels)
    inverse_roi_mask = classes*inverse_roi_mask

    name = img_name.split('/')[-1]
    # s = scales[idx]
    # r = orientations[idx]
    # print('scaling factors:', scale)
    # print('rotation factors:', orientation)
    print(scales.shape, orientations.shape)
    idx=0
    for fs,fr in zip(scales, orientations):
        fr = int(fr)
        fs = round(fs,2)
        TEMP_img  = tf.rotate(img, fr, fill=[1]*n_channels)*roi_mask+img_inverse_roi
        if dataset=='Mosaics':
            TEMP_img = TEMP_img.squeeze().numpy()
        else:
            TEMP_img = TEMP_img.squeeze().permute(1,2,0).numpy()

        TEMP_mask = tf.rotate(mask, fr, fill=[classes])*roi_mask+inverse_roi_mask
        TEMP_mask = TEMP_mask.squeeze().numpy()
        # print('unique:', np.unique(mask), np.unique(TEMP_mask))
        w = int(fs*512)

        TEMP_img  = cv2.resize(TEMP_img, (w,w), interpolation=cv2.INTER_LINEAR)
        TEMP_mask = cv2.resize(TEMP_mask, (w,w), interpolation=cv2.INTER_NEAREST)
        print(TEMP_img.shape, TEMP_mask.shape)

        heatmap = (TEMP_mask*255.0/(classes+1)).astype(np.uint8)
        heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)

        cv2.imwrite(save_imgs+name[:-1]+'_id_'+str(idx)+'_s_'+str(fs)+'_r_'+str(fr)+'.png', TEMP_img)
        cv2.imwrite(save_gts+name[:-1]+'_id_'+str(idx)+'_s_'+str(fs)+'_r_'+str(fr)+'.png', TEMP_mask)
        cv2.imwrite(save_masks+name[:-1]+'_id_'+str(idx)+'_s_'+str(fs)+'_r_'+str(fr)+'.png', heatmap)
        idx+=1

gen_vis_img_gt('CRAG')