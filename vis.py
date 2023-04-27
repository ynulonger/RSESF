import matplotlib.pyplot as plt
import numpy as np
import torch
import math
import torchvision.transforms.functional as tf
import torchvision.transforms as tv
import os
import cv2
from utils.metrics import *
from utils.dataset import *
from torch.autograd import Variable
from models.unet_model import UNet_CNN
from torch.utils.data import DataLoader


def get_roi_mask(h):
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
    img_inverse_roi  = torch.cat([inverse_roi_mask]*3, dim=1)
    return roi_mask, inverse_roi_mask, img_inverse_roi


# img = cv2.imread('hist_img.png')
# gt = cv2.imread('hist_mask.png',flags=0)

# print(img.shape)
# preprocess = tv.Compose([
#    tv.ToTensor(),
# ])

# x = preprocess(img).unsqueeze(0)
# gt = preprocess(gt).unsqueeze(0)


# roi_mask, inverse_roi_mask, img_inverse_roi = get_roi_mask(img.shape[1]+1)

# masked_img = x*roi_mask
# masked_gt = gt*roi_mask


# plt.figure(dpi=400)
# n_rota = 6
# for i in range(n_rota):
#     plt.subplot(1,n_rota,i+1)
#     rotated_img = tf.rotate(x, angle=-60*i, fill=[1,1,1])*roi_mask+img_inverse_roi
#     plt.imshow(rotated_img[0].permute(1,2,0))
#     plt.axis('off')
# plt.savefig('rotate_img.png',bbox_inches='tight')

# for i in range(n_rota):
#     plt.subplot(1,n_rota,i+1)
#     rotated_img = tf.rotate(gt, angle=-60*i, fill=[1])*roi_mask+inverse_roi_mask
#     plt.imshow(rotated_img[0].permute(1,2,0),cmap='gray')
#     plt.axis('off')
# plt.savefig('rotate_gt.png',bbox_inches='tight')

def save_image_patches(dataset, angle):
    save_patches = 'data/'+dataset+'/'+str(angle)+'/'
    if not os.path.exists(save_patches):
        os.makedirs(save_patches)

    if dataset=='BCSS':
        test_dataset  = BCSS(image_set='test', factor=1,  angle=angle, visualisation=True)
        classes = 5

    elif dataset=='Kumar':
        test_dataset  = Kumar(image_set='test', mask_channel=2, factor=1, angle=angle, visualisation=True)
        classes =2

    val_loader = DataLoader(test_dataset, batch_size=8, shuffle=False, num_workers=2, pin_memory=True)

    count=0
    img_count = 0
    miou_averaged = 0

    for batch in val_loader:
        with torch.no_grad():
            imgs = batch['image']
            names = batch['name']

            roi_mask, inverse_roi_mask, img_inverse_roi = get_roi_mask(imgs.shape[-1]+1)
            inverse_roi_mask = classes*inverse_roi_mask

            imgs  = tf.rotate(imgs, angle, fill=[1,1,1])*roi_mask+img_inverse_roi
            imgs  = imgs.squeeze()


            for x in range(imgs.shape[0]):
                temp_name = names[x].split('/')[-1]
                temp_img_name = save_patches+temp_name[:-4]+'.png'
                cv2.imwrite(temp_img_name, imgs[x].permute(1,2,0).numpy()*255)


            img_count+=imgs.shape[0]
        if img_count==8:
            break

for angle in [int(i*45) for i in range(8)]:
    save_image_patches('Kumar', angle)
