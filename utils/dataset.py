import cv2
import glob
import torch
import random
import logging
import numpy as np
import os.path as osp
from PIL import Image
from os import listdir
from os.path import splitext
from torch.utils.data import Dataset
from torchvision import transforms
from torch.utils.data import DataLoader
import torchvision.transforms.functional as F

HOME_DIR = '/scratch/yy3u19/DataSets/'
# HOME_DIR = '/ECSssd/user_data/yy3u19/'
# HOME_DIR = '/ssdfs/users/yy3u19/'


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


def DataAug(img, target, size):
    i, j, h, w = transforms.RandomCrop.get_params(img, (size, size))
    img = F.crop(img, i, j, h, w)
    target = F.crop(target, i, j, h, w)
    if random.random() > 0.5:
        img = F.hflip(img)
        target = F.hflip(target)
    if random.random() > 0.5:
        img = F.vflip(img)
        target = F.vflip(target)
    return img, target

def KumarDataAug(img, target):
    if random.random() > 0.5:
        img = F.hflip(img)
        target = F.hflip(target)
    if random.random() > 0.5:
        img = F.vflip(img)
        target = F.vflip(target)
    return img, target

class CustomImageSet(Dataset):
    def __init__(self, image_set='train', sample_weight=None, mask_channel=5, factor=1, angle=0, visualisation=False, d_name='Mosaics'):   # initial logic happens like transform
        self.sample_weight=sample_weight
        self.mask_channel = mask_channel
        self.visualisation = visualisation
        self.factor = factor
        self.angle = angle
        self._image_set = image_set
        if self._image_set == 'train':
            self._image_names = glob.glob(HOME_DIR + d_name + '/train-imgs/*')
            self._mask_names = glob.glob(HOME_DIR + d_name + '/train-gts/*')

        elif self._image_set == 'test':
            # self._image_names = [img for img in glob.iglob(image_fp) if os.path.basename(img) in valids]
            self._image_names= glob.glob(HOME_DIR + 'Mosaics/test-imgs/*')
            self._mask_names= glob.glob(HOME_DIR + 'Mosaics/test-gts/*')
        elif self._image_set == 'test_r':
            # self._image_names = [img for img in glob.iglob(image_fp) if os.path.basename(img) in valids]
            self._image_names= glob.glob(HOME_DIR + 'Mosaics/same_scale_(s=1)/test-imgs/*')
            self._mask_names= glob.glob(HOME_DIR + 'Mosaics/same_scale_(s=1)/test-gts/*')
        elif self._image_set == 'test_s':
            # self._image_names = [img for img in glob.iglob(image_fp) if os.path.basename(img) in valids]
            self._image_names= glob.glob(HOME_DIR + 'Mosaics/same_angle_(r=0)/test-imgs/*')
            self._mask_names= glob.glob(HOME_DIR + 'Mosaics/same_angle_(r=0)/test-gts/*')
        elif self._image_set == 'test_rs':
            # self._image_names = [img for img in glob.iglob(image_fp) if os.path.basename(img) in valids]
            self._image_names= glob.glob(HOME_DIR + 'Mosaics/r=(0-360)_s=(0.5-2)/test-imgs/*')
            self._mask_names= glob.glob(HOME_DIR + 'Mosaics/r=(0-360)_s=(0.5-2)/test-gts/*')
        elif self._image_set == 'original':
            # self._image_names = [img for img in glob.iglob(image_fp) if os.path.basename(img) in valids]
            self._image_names= glob.glob(HOME_DIR + 'Mosaics/r=0_s=1/test-imgs/*')
            self._mask_names= glob.glob(HOME_DIR + 'Mosaics/r=0_s=1/test-gts/*')
        elif self._image_set == 'evaluate':
            # self._image_names = [img for img in glob.iglob(image_fp) if os.path.basename(img) in valids]
            self._image_names= glob.glob(HOME_DIR + 'Mosaics/evaluate-imgs/*')
            self._mask_names= glob.glob(HOME_DIR + 'Mosaics/evaluate-gts/*')
        elif self._image_set == 'vis':
            # self._image_names = [img for img in glob.iglob(image_fp) if os.path.basename(img) in valids]
            self._image_names= glob.glob(HOME_DIR + 'Mosaics/vis-imgs-2/*')
            self._mask_names= glob.glob(HOME_DIR + 'Mosaics/vis-gts-2/*')
        elif self._image_set == 'eg':
            # self._image_names = [img for img in glob.iglob(image_fp) if os.path.basename(img) in valids]
            self._image_names= glob.glob(HOME_DIR + 'Mosaics/Mosaics_eg_img/*')
            self._mask_names= glob.glob(HOME_DIR + 'Mosaics/Mosaics_eg_gt/*')
        
        else:
            raise RuntimeError('image set should only be train or set')
        # print('--'*20, self._image_names[0], self._mask_names[0], '--'*20)
        self._image_names.sort()
        self._mask_names.sort()
        if self.sample_weight == 'mean':
            self.sample_weight = torch.ones(len(self._image_names),1,512,512)/(512**2*len(self._image_names))
        elif self.sample_weight=='sample_mean':
            self.sample_weight = torch.ones(len(self._image_names),1)/len(self._image_names)

    def __getitem__(self, index):
        # print(self._mask_names, self._image_names)
        assert(self._image_names[index].split('/')[-1]==self._mask_names[index].split('/')[-1]), 'img name is not the same as the mask name'
        image = cv2.imread((self._image_names[index]),flags=0)  # image BGR
        mask  = cv2.imread(self._mask_names[index],flags=0)
        
        if self.visualisation:
            pass
        else:
            image = (image-127)/127.0

        if self.factor != 1:
            if isinstance(self.factor, list):
                rand = torch.rand(1).item()
                if rand  <= 0.25:
                    w = 128
                elif rand <= 0.5:
                    w = 256
                elif rand <= 0.75:
                    w = 384
                else:
                    w = 512
                image = cv2.resize(image, (w,w), interpolation=cv2.INTER_LINEAR)
                mask  = cv2.resize(mask, (w, w), interpolation=cv2.INTER_NEAREST)     
            else:
                image = cv2.resize(image, (0,0), fx=self.factor, fy=self.factor, interpolation=cv2.INTER_LINEAR)
                mask  = cv2.resize(mask, (0,0), fx=self.factor, fy=self.factor, interpolation=cv2.INTER_NEAREST)

        image = np.expand_dims(image,axis=0)
        mask  = mapping(mask, self.mask_channel)

        if self.sample_weight==None:
            return {
                'image': torch.from_numpy(image).type(torch.FloatTensor),
                'mask': torch.from_numpy(mask).type(torch.FloatTensor),
                'name': self._image_names[index].split('/')[-1],
            }
        else:
            return {
                'image': torch.from_numpy(image).type(torch.FloatTensor),
                'mask': torch.from_numpy(mask).type(torch.FloatTensor),
                'name': self._image_names[index].split('/')[-1],
                'weight': self.sample_weight[index].view(-1,1)
            }

    def __len__(self):  # return count of sample we have
        return len(self._image_names)

class Digest(Dataset):
    def __init__(self, img_pth, mask_pth, sample_weight=None, mask_channel=1):   # initial logic happens like transform
        self._image_names = img_pth
        self.mask_paths = mask_pth
        self.mask_channel = mask_channel
        self.sample_weight =sample_weight
        if self.sample_weight == 'mean':
            self.sample_weight = torch.ones(len(self.image_paths),1,512,512)/(512**2*len(self.image_paths))
        elif self.sample_weight=='sample_mean':
            self.sample_weight = torch.ones(len(self.image_paths),1)/len(self.image_paths)
        self.transforms = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize((0.6633, 0.3966, 0.6155), (0.1400, 0.2150, 0.1947))
        ])
    def __getitem__(self, index):
        # print('image:',self.image_paths[index],'mask:',self.mask_paths[index])
        assert(self.image_paths[index].split('/')[-1]==self.mask_paths[index].split('/')[-1]), 'img name is not the same as the mask name'
        image = cv2.imread((self.image_paths[index]),flags=1)
        # image = cv2.imread((self.image_paths[index]))
        mask  = cv2.imread(self.mask_paths[index],flags=0)//255
        mask = np.expand_dims(mask,axis=0)

        if self.sample_weight==None:
            return {
                'image': self.transforms(image),
                'mask': torch.from_numpy(mask).type(torch.FloatTensor),
                'name': self.image_paths[index].split('/')[-1],
            }
        else:
            return {
                # 'image': torch.from_numpy(image).type(torch.FloatTensor),
                'image': self.transforms(image),
                'mask': torch.from_numpy(mask).type(torch.FloatTensor),
                'name': self.image_paths[index].split('/')[-1],
                'weight': self.sample_weight[index]
            }
    def __len__(self):  # return count of sample we have
        return len(self.image_paths)

def my_transforms(img, mask, patch_size):
    height = img.shape[0]
    width = img.shape[1]
    top  = np.random.randint(1, height-patch_size)
    left = np.random.randint(1, width-patch_size)
    img_croped = img[top:top+patch_size, left: left+patch_size,:]
    mask_croped = mask[top:top+patch_size, left:left+patch_size]
    return img_croped, mask_croped

def mapping(gt, channels):
    size = gt.shape
    mask = np.zeros([channels, size[0], size[1]])
    gt[gt==6] = 5
    labels = np.unique(gt)
    # print('labels:', labels, mask.shape)
    for label in labels:
        mask[label, :,:] = (gt==label).astype(np.uint8)
    return mask

class Kumar(Dataset):
    def __init__(self, image_set='train', sample_weight=None, mask_channel=2, factor=1, angle=0, visualisation=False):
        self.sample_weight=sample_weight
        self.mask_channel = mask_channel
        self.factor = factor
        self.angle = angle
        self._image_set = image_set
        if self._image_set == 'train':
            self._image_names = glob.glob(HOME_DIR + 'Kumar/Train_patch/*')
            self._mask_names = glob.glob(HOME_DIR + 'Kumar/Train_patch_mask/*')

        elif self._image_set == 'test':
            # self._image_names = [img for img in glob.iglob(image_fp) if os.path.basename(img) in valids]
            self._image_names= glob.glob(HOME_DIR + 'Kumar/Test_patch/*png')
            self._mask_names= glob.glob(HOME_DIR + 'Kumar/Test_patch_mask/*png')

        else:
            raise RuntimeError('image set should only be train or set')
        self._image_names.sort()
        self._mask_names.sort()
        self.MEAN = (0.6519, 0.5859, 0.7658)
        self.STD = (0.1911, 0.2308, 0.2018)

        self.transforms  = transforms.Compose([transforms.ToTensor()]) if visualisation else transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize(self.MEAN, self.STD)
        ])
        if self.sample_weight == 'mean':
            self.sample_weight = torch.ones(len(self._image_names),1,400,400)/(400**2*len(self._image_names))
        elif self.sample_weight=='sample_mean':
            self.sample_weight = torch.ones(len(self._image_names),1)/len(self._image_names)

    def __len__(self):
        return len(self._image_names)

    def __getitem__(self, index):
        # print(self._image_names[index], self._mask_names[index])
        assert(self._image_names[index].split('/')[-1]==self._mask_names[index].split('/')[-1]), self._image_names[index].split('/')[-1]+'--'+self._mask_names[index].split('/')[-1]

        image = cv2.imread(self._image_names[index], flags=1)
        mask  = (cv2.imread(self._mask_names[index], flags=0)>1).astype(np.uint8)
        if self.factor != 1:
            if isinstance(self.factor, list):
                rand = torch.rand(1).item()
                if rand  <= 0.25:
                    w = 128
                elif rand <= 0.5:
                    w = 256
                elif rand <= 0.75:
                    w = 384
                else:
                    w = 512
                image = cv2.resize(image, (w,w), interpolation=cv2.INTER_LINEAR)
                mask  = cv2.resize(mask, (w, w), interpolation=cv2.INTER_NEAREST)     
        
            else:
                image = cv2.resize(image, (0,0), fx=self.factor, fy=self.factor, interpolation=cv2.INTER_LINEAR)
                mask  = cv2.resize(mask, (0,0), fx=self.factor, fy=self.factor, interpolation=cv2.INTER_NEAREST)

        img  = self.transforms(image)
        mask  = mapping(mask, self.mask_channel)
        mask = torch.from_numpy(mask).type(torch.float32)

        if isinstance(self.factor, list):
            img = F.center_crop(img,(384,384))
            mask  = F.center_crop(mask, (384,384)) 

        if self._image_set == 'train':
            img, mask = KumarDataAug(img, mask)

        if self.sample_weight==None:
            return {
                'image': img,
                'mask': mask,
                'name': self._image_names[index].split('/')[-1],
            }
        else:
            return {
                # 'image': torch.from_numpy(image).type(torch.FloatTensor),
                'image': img,
                'mask': mask,
                'name': self._image_names[index].split('/')[-1],
                'weight': self.sample_weight[index]
            }

class GlaS(Dataset):
    def __init__(self, image_set='train', sample_weight=None, mask_channel=2, factor=1):
        self.sample_weight=sample_weight
        self._image_set = image_set
        self.mask_channel = mask_channel
        self.factor = factor
        
        if self._image_set == 'train':
            self._image_names = glob.glob(HOME_DIR + 'GlaS/Train_patch/*')
            self._mask_names = glob.glob(HOME_DIR + 'GlaS/Train_patch_mask/*')

        elif self._image_set == 'test':
            # self._image_names = [img for img in glob.iglob(image_fp) if os.path.basename(img) in valids]
            self._image_names= glob.glob(HOME_DIR + 'GlaS/Test_patch/*png')
            self._mask_names= glob.glob(HOME_DIR + 'GlaS/Test_patch_mask/*png')        
        elif self._image_set == 'evaluate':
            # self._image_names = [img for img in glob.iglob(image_fp) if os.path.basename(img) in valids]
            self._image_names= glob.glob(HOME_DIR + 'GlaS/evaluate-imgs/*')
            self._mask_names= glob.glob(HOME_DIR + 'GlaS/evaluate-gts/*')
        elif self._image_set == 'vis':
            # self._image_names = [img for img in glob.iglob(image_fp) if os.path.basename(img) in valids]
            self._image_names= glob.glob(HOME_DIR + 'GlaS/vis-imgs/*')
            self._mask_names= glob.glob(HOME_DIR + 'GlaS/vis-gts/*')
        else:
            raise RuntimeError('image set should only be train, test, evaluate, or vis set')
        self._image_names.sort()
        self._mask_names.sort()
        self.MEAN = (0.6535, 0.5831, 0.7515)
        self.STD = (0.1994, 0.2388, 0.2010)

        self.transforms  = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize(self.MEAN, self.STD)
        ])
        if self.sample_weight == 'mean':
            self.sample_weight = torch.ones(len(self._image_names),1,448,448)/(448**2*len(self._image_names))
        elif self.sample_weight=='sample_mean':
            self.sample_weight = torch.ones(len(self._image_names),1)/len(self._image_names)

    def __len__(self):
        return len(self._image_names)

    def __getitem__(self, index):
        # print(self._image_names[index], self._mask_names[index])
        assert(self._image_names[index].split('/')[-1]==self._mask_names[index].split('/')[-1]), self._image_names[index].split('/')[-1]+'--'+self._mask_names[index].split('/')[-1]

        image = cv2.imread(self._image_names[index], flags=1)
        # mask  = (cv2.imread(self._mask_names[index], flags=0)>1).astype(np.uint8)

        if self._image_set=='evaluate' or self._image_set=='vis':
            mask  = cv2.imread(self._mask_names[index], flags=0).astype(np.uint8)
            # print('mask',np.unique(mask))
        else:
            mask  = (cv2.imread(self._mask_names[index], flags=0)>1).astype(np.uint8)
        if self.factor != 1:
            if isinstance(self.factor, list):
                rand = torch.rand(1).item()
                if rand  <= 0.25:
                    w = 128
                elif rand <= 0.5:
                    w = 256
                elif rand <= 0.75:
                    w = 384
                else:
                    w = 512
                image = cv2.resize(image, (w,w), interpolation=cv2.INTER_LINEAR)
                mask  = cv2.resize(mask, (w, w), interpolation=cv2.INTER_NEAREST)     
        
            else:
                image = cv2.resize(image, (0,0), fx=self.factor, fy=self.factor, interpolation=cv2.INTER_LINEAR)
                mask  = cv2.resize(mask, (0,0), fx=self.factor, fy=self.factor, interpolation=cv2.INTER_NEAREST)

        img  = self.transforms(image)
        mask  = mapping(mask, self.mask_channel)
        # mask  = mapping(mask, self.mask_channel)
        mask = torch.from_numpy(mask).type(torch.float32)

        if isinstance(self.factor, list):
            img = F.center_crop(img,(384,384))
            mask  = F.center_crop(mask, (384,384)) 

        if self._image_set == 'train':
            img, mask = KumarDataAug(img, mask)

        if self.sample_weight==None:
            return {
                'image': img,
                'mask': mask,
                'name': self._image_names[index].split('/')[-1],
            }
        else:
            return {
                # 'image': torch.from_numpy(image).type(torch.FloatTensor),
                'image': img,
                'mask': mask,
                'name': self._image_names[index].split('/')[-1],
                'weight': self.sample_weight[index]
            }

class BCSS(Dataset):
    def __init__(self, image_set='train', sample_weight=None, mask_channel=5, factor=1, angle=0, visualisation=False):
        if isinstance(factor, list):      
            self.crop_size = 384
        else:
            self.crop_size = int(512*factor)
        self.angle = angle
        self.sample_weight=sample_weight
        self._image_set = image_set
        self.mask_channel = mask_channel
        self.factor = factor
        if self._image_set == 'train':
            self._image_names = glob.glob(HOME_DIR + 'BCSS/train_imgs/*png')
            self._mask_names = glob.glob(HOME_DIR + 'BCSS/train_gts/*png')

        elif self._image_set == 'test':
            # self._image_names = [img for img in glob.iglob(image_fp) if os.path.basename(img) in valids]
            self._image_names= glob.glob(HOME_DIR + 'BCSS/final/test_imgs/*png')#[:30]
            self._mask_names= glob.glob(HOME_DIR + 'BCSS/final/test_gts/*png')#[:30]

        elif self._image_set == 'evaluate':
            # self._image_names = [img for img in glob.iglob(image_fp) if os.path.basename(img) in valids]
            self._image_names= glob.glob(HOME_DIR + 'BCSS/new_imgs/test/*png')
            self._mask_names= glob.glob(HOME_DIR + 'BCSS/new_gts/test/*png')
        else:
            raise RuntimeError('image set should only be train or set')
        self._image_names.sort()
        self._mask_names.sort()
        self.MEAN = (0.7258, 0.6042, 0.8183)
        self.STD  = (0.1708, 0.2302, 0.1744)

        self.transforms  = transforms.Compose([transforms.ToTensor()]) if visualisation else transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize(self.MEAN, self.STD)
        ])

        if self.sample_weight=='sample_mean':
            self.sample_weight = torch.ones(len(self._image_names),1)/len(self._image_names)

    def __len__(self):
        return len(self._image_names)

    def __getitem__(self, index):
        assert(self._image_names[index].split('/')[-1]==self._mask_names[index].split('/')[-1]), self._image_names[index].split('/')[-1]+'--'+self._mask_names[index].split('/')[-1]

        image = cv2.imread(self._image_names[index], flags=1)
        mask  = cv2.imread(self._mask_names[index], flags=0)
        if self.factor != 1:
            if isinstance(self.factor, list):
                rand = torch.rand(1).item()
                if rand  <= 0.25:
                    w = 128
                elif rand <= 0.5:
                    w = 256
                elif rand <= 0.75:
                    w = 384
                else:
                    w = 512
                image = cv2.resize(image, (w,w), interpolation=cv2.INTER_LINEAR)
                mask  = cv2.resize(mask, (w, w), interpolation=cv2.INTER_NEAREST)     
        
            else:
                image = cv2.resize(image, (0,0), fx=self.factor, fy=self.factor, interpolation=cv2.INTER_LINEAR)
                mask  = cv2.resize(mask, (0,0), fx=self.factor, fy=self.factor, interpolation=cv2.INTER_NEAREST)

        img  = self.transforms(image)
        mask  = mapping(mask, self.mask_channel)
        mask = torch.from_numpy(mask).type(torch.float32)

        if isinstance(self.factor, list):
            img = F.center_crop(img,(384,384))
            mask  = F.center_crop(mask, (384,384)) 

        if self._image_set == 'train':
            img, mask = DataAug(img, mask, self.crop_size)

        # if self._image_set == 'test':
        #     roi_mask, inverse_roi_mask, img_inverse_roi = get_roi_mask(img.shape[-1]+1)

        #     img  = F.rotate(img,  self.angle, fill=[1,1,1])*roi_mask+img_inverse_roi
        #     mask = F.rotate(mask, self.angle, fill=[self.mask_channel])*roi_mask+inverse_roi_mask*self.mask_channel

        #     mask = mask.squeeze()
        #     img  = img.squeeze()

        if self.sample_weight==None:
            return {
                'image': img,
                'mask': mask,
                'name': self._image_names[index].split('/')[-1],
            }
        else:
            return {
                # 'image': torch.from_numpy(image).type(torch.FloatTensor),
                'image': img,
                'mask': mask,
                'name': self._image_names[index].split('/')[-1],
                'weight': self.sample_weight[index]
            }

class CRAG(Dataset):
    def __init__(self, image_set='train', sample_weight=None, mask_channel=2, factor=1):
        self.sample_weight=sample_weight
        self._image_set = image_set
        self.mask_channel = mask_channel
        self.factor = factor

        if self._image_set == 'train':
            self._image_names = glob.glob(HOME_DIR + 'CRAG/TRAIN/img/*png')
            self._mask_names = glob.glob(HOME_DIR + 'CRAG/TRAIN/labelcol/*png')

        elif self._image_set == 'test':
            self._image_names= glob.glob(HOME_DIR + 'CRAG/TEST/img/*png')
            self._mask_names= glob.glob(HOME_DIR + 'CRAG/TEST/labelcol/*png')

        elif self._image_set == 'evaluate':
            # self._image_names = [img for img in glob.iglob(image_fp) if os.path.basename(img) in valids]
            self._image_names= glob.glob(HOME_DIR + 'CRAG/evaluate-imgs/*')
            self._mask_names= glob.glob(HOME_DIR + 'CRAG/evaluate-gts/*')
        elif self._image_set == 'vis':
            # self._image_names = [img for img in glob.iglob(image_fp) if os.path.basename(img) in valids]
            self._image_names= glob.glob(HOME_DIR + 'CRAG/vis-imgs/*')
            self._mask_names= glob.glob(HOME_DIR + 'CRAG/vis-gts/*')
        else:
            raise RuntimeError('image set should only be train or set')
        self._image_names.sort()
        self._mask_names.sort()
        self.MEAN = (0.8568, 0.7219, 0.8302)
        self.STD  = (0.0935, 0.1676, 0.1277)

        self.transforms  = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize(self.MEAN, self.STD)
        ])
        if self.sample_weight=='sample_mean':
            self.sample_weight = torch.ones(len(self._image_names),1)/len(self._image_names)

    def __len__(self):
        return len(self._image_names)

    def __getitem__(self, index):
        # print(self._image_names[index], self._mask_names[index])
        assert(self._image_names[index].split('/')[-1]==self._mask_names[index].split('/')[-1]), self._image_names[index].split('/')[-1]+'--'+self._mask_names[index].split('/')[-1]

        image = cv2.imread(self._image_names[index], flags=1)
        if self._image_set=='evaluate':
            mask  = cv2.imread(self._mask_names[index], flags=0).astype(np.uint8)
        else:
            mask  = (cv2.imread(self._mask_names[index], flags=0)>0.5).astype(np.uint8)
        if self.factor != 1:
            if isinstance(self.factor, list):
                rand = torch.rand(1).item()
                if rand  <= 0.25:
                    w = 128
                elif rand <= 0.5:
                    w = 256
                elif rand <= 0.75:
                    w = 384
                else:
                    w = 512
                image = cv2.resize(image, (w,w), interpolation=cv2.INTER_LINEAR)
                mask  = cv2.resize(mask, (w, w), interpolation=cv2.INTER_NEAREST)     
        
            else:
                image = cv2.resize(image, (0,0), fx=self.factor, fy=self.factor, interpolation=cv2.INTER_LINEAR)
                mask  = cv2.resize(mask, (0,0), fx=self.factor, fy=self.factor, interpolation=cv2.INTER_NEAREST)

        img  = self.transforms(image)

        mask  = mapping(mask, self.mask_channel)
        mask = torch.from_numpy(mask).type(torch.float32)

        if isinstance(self.factor, list):
            img = F.center_crop(img,(384,384))
            mask  = F.center_crop(mask, (384,384)) 

        if self._image_set == 'train':
            img, mask = KumarDataAug(img, mask)

        if self.sample_weight==None:
            return {
                'image': img,
                'mask': mask,
                'name': self._image_names[index].split('/')[-1],
            }
        else:
            return {
                # 'image': torch.from_numpy(image).type(torch.FloatTensor),
                'image': img,
                'mask': mask,
                'name': self._image_names[index].split('/')[-1],
                'weight': self.sample_weight[index]
            }

def get_mean_std(loader):
    channels_sum, channels_squares_sum, num_batches = 0,0,0
    for data in loader:
        data = data['image']
        channels_sum += torch.mean(data, dim=[0,2,3])
        channels_squares_sum += torch.mean(data**2, dim=[0,2,3])
        num_batches +=1
    mean = channels_sum/num_batches
    std = (channels_squares_sum/num_batches-mean**2)**0.5
    return mean, std

if __name__ == '__main__':
    print(train_dataset.__len__())
    train_loader = DataLoader(train_dataset, batch_size=4)
    mean, std = get_mean_std(train_loader)
    print(mean)
    print(std)




