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
from torch.autograd import Variable
from models.unet_model import *
from torch.utils.data import DataLoader
import torchvision.transforms.functional as tf
from sklearn.metrics import confusion_matrix


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
    # cv2.imwrite('roi_mask.png',roi_mask.squeeze().numpy()*250)
    img_inverse_roi  = torch.cat([inverse_roi_mask*255]*n_channels, dim=1)
    return roi_mask, inverse_roi_mask, img_inverse_roi

def predict_img(model, net, device, classes, dataset, n_channels=1, subset='test'):

    save_patches = 'evaluate_data/'+dataset+'/'+model+'/'+subset+'/'
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
            imgs = batch['image'].to(device=device, dtype=torch.float32)
            masks = batch['mask'].to(device=device, dtype=torch.float32)
            names = batch['name']

            roi_mask, inverse_roi_mask, img_inverse_roi = get_roi_mask(imgs.shape[-1]+1, n_channels)
            inverse_roi_mask = classes*inverse_roi_mask

            # masks = masks.squeeze()
            # imgs  = imgs.squeeze()


            output = F.softmax(net(imgs), dim=1)

            # roi_mask_f, inverse_roi_mask_f, img_inverse_roi_f = get_roi_mask(imgs.shape[-1]+1, classes)
            # out_f = tf.rotate(output, -angle, fill=[1]*classes)*roi_mask_f+img_inverse_roi_f
            # out_f = out_f.unsqueeze(dim=1)
            # out_feats.append(out_f)

            torch_masks = torch.argmax(masks,dim=1,  keepdim=True)
            torch_preds = torch.argmax(output,dim=1, keepdim=True)

            torch_preds = torch_preds*roi_mask+inverse_roi_mask
            torch_preds = torch_preds.squeeze(1).type(torch.int8)

            torch_masks = torch_masks*roi_mask+inverse_roi_mask
            torch_masks = torch_masks.squeeze(1).type(torch.int8)

            # print('labels:',torch.unique(torch_masks), torch.unique(torch_preds))

            metrics.add(torch_preds.squeeze(1).view(-1), torch_masks.squeeze(1).view(-1))
            # '''
            for x in range(torch_preds.shape[0]):
                _,_,miou = metrics.get_img_iou(torch_preds[x],torch_masks[x])
                if dataset=='Kumar':
                    k = 255/(classes+1)
                    iou = round(miou[1].item(),4)    
                else:
                    # k = 255/(classes+1)
                    k = 255/(classes-1)
                    iou = round(miou.mean().item(),4)
                temp_name = names[x].split('/')[-1]
                temp_pred_name = save_patches+temp_name[:-4]+'_'+str(round(iou,4))+'.png'
                print('img:', img_count ,temp_pred_name)
                # fs = round(float(temp_name.split('_')[5]),2)
                # fr = int(temp_name.split('_')[7].split('.')[0])
                # pred_record = [fs, fr, round(iou,4)]
                # mIoU_list.append(pred_record)
            '''
                
                heatmap = (torch_preds[x].cpu().numpy()*k).astype(np.uint8)
                heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
                roi_mask = roi_mask.squeeze(0).permute(1,2,0).cpu().numpy()
                img_inverse_roi = torch.permute(img_inverse_roi.squeeze(0), [1,2,0]).cpu().numpy()
                # heatmap = heatmap*roi_mask+img_inverse_roi
                cv2.imwrite(temp_pred_name, heatmap)

                # temp_name_2 = save_patches+temp_name[:-4]+'_'+'_mask.png'
                # heatmap = (k*torch_masks[x].cpu().numpy()).astype(np.uint8)
                # heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
                # cv2.imwrite(temp_name_2, heatmap)
            '''
            img_count+=torch_preds.shape[0]
        # if img_count%50==0:
        #     print(f'{datetime.datetime.now()}, {img_count} images evaluated!')
        # if img_count%20==0:
        #     print(f'{datetime.datetime.now()}, {img_count} images evaluated!')
        #     break
    # out_feats = torch.cat(out_feats, dim=0)
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
    parser.add_argument('-n', '--name', dest='name', type=str, default='E2CNN',
                        help='name')
    parser.add_argument('-m', '--mode', dest='mode', type=str, default='predict',
                        help='name')
    parser.add_argument('-f', '--n_filters', dest='n_filters', type=int, default=8,
                        help='num of filters')
    parser.add_argument('-k', '--k_size', dest='k_size', type=int, default=5,
                        help='k_size')
    parser.add_argument('-r', '--n_rotation', dest='n_rotation', type=int, default=8,
                        help='num of rotations')
    parser.add_argument('-s', '--subset', dest='subset', type=str, default='test',
                        help='dataset')
    parser.add_argument('-g', '--k_factor', dest='k_factor', type=float, default=2,
                        help='order')
    parser.add_argument('-a', '--lower_bound', dest='lower_bound', type=float, default=0.5,
                        help='order')
    return parser.parse_args()

def count_your_model(model, x, y):
        # your rule here
        pass

def plot_filter(filters, name, n_rotation=8):
    filters = filters.squeeze()
    filters = np.reshape(filters,[-1, n_rotation,filters.shape[-2],filters.shape[-1]])
    print('name:',name,'filter shape:', filters.shape)
    plt.figure(dpi=300)
    row = filters.shape[0]
    col = filters.shape[1]
    i=1
    for r in range(row):
        for c in range(col):
            plt.subplot(row, col,i)
            plt.imshow(filters[r,c])
            plt.axis('off')
            i+=1
    plt.show()
    plt.savefig(name+'.png',  bbox_inches='tight',dpi=300,pad_inches=0.0)


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
    elif args.name=='E2CNN' or args.name=='HNets':
        if args.mode=='predict':
            net = e2UNet_Mini(n_channels=n_channels, n_classes=classes, filters=args.n_filters, rotations=args.n_rotation, kernel_size=args.k_size).cuda()
            net.eval()
            print(net)
            # i=0
            # for name, layer in net.named_modules():
            #     print(i, name)
            #     i+=1
            # filters = [net.inc.double_conv.export()[0].eval().weight.detach().cpu().numpy(),
            #            net.inc.double_conv.export()[3].eval().weight.detach().cpu().numpy()[:8,:8,:,:],
            #            net.down1.conv.double_conv.export()[0].eval().weight.detach().cpu().numpy()[:8,:8,:,:],
            #            net.down1.conv.double_conv.export()[3].eval().weight.detach().cpu().numpy()[:8,:8,:,:],
            #            net.up1.squeeze.double_conv.export()[0].eval().weight.detach().cpu().numpy()[:8,:8,:,:],
            #            net.up1.squeeze.double_conv.export()[3].eval().weight.detach().cpu().numpy()[:8,:8:,:,:],
            #         ]
            # names = ['1_1','1_2','2_1','2_2','3_1','3_2']
            # for f,n in zip(filters, names):
            #     plot_filter(f, n)
            # print('----'*20, net.inc.double_conv.export()[0].eval().weight.shape)
    elif args.name=='RST':
        if args.mode=='predict':
            net = UNet_R_Mini(n_channels=n_channels, n_classes=classes, filters=args.n_filters, init_order=2, bilinear=True, \
                     init_scale=0.99, angles=[torch.tensor(0+i*2*math.pi/args.n_rotation) for i in range(args.n_rotation)],\
                     n_scales=1, rotation_size=1, learn_sigma=True, k=args.k_factor, selection=0, \
                     lower_bound=args.lower_bound).cuda()
            net.eval()
            print(net)

    print('-'*10, 'kernel_size:', args.k_size, '-'*10, 'classes:', classes, '-'*10, 'model:', args.name, '-'*10,'rotations:', args.n_rotation, '-'*10, 'dataset:', args.data, '-', args.subset, '-'*10)
    for n,p in net.named_parameters():
        print(n, p.shape)
    # summary(net, (n_channels, 512, 512))

    params = [p.nelement() for p in net.parameters() if p.requires_grad]
    num = sum(params)
    print(f'num of trainable parameters:{num}')
    
    print("Loading model {}".format(args.weight), 'num of rotations of filters:', args.n_rotation)

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

        '''
        # RSESF filter
        filters = [net.inc.double_conv[0].export().detach().cpu().numpy().squeeze(),
                   net.inc.double_conv[3].export().detach().cpu().numpy().squeeze()[:8,0,:,:,:],
                   net.down1.maxpool_conv[1].double_conv[0].export().detach().cpu().numpy().squeeze()[:8,0,:,:,:],
                   net.down1.maxpool_conv[1].double_conv[3].export().detach().cpu().numpy().squeeze()[:8,0,:,:,:],
                   net.up1.conv.double_conv[0].export().detach().cpu().numpy().squeeze()[:8,0,:,:,:],
                   net.up1.conv.double_conv[3].export().detach().cpu().numpy().squeeze()[:8,0,:,:,:],
                ]
        names = ['1_1','1_2','2_1','2_2','3_1','3_2']
        for f,n in zip(filters, names):
            plot_filter(f, str(args.k_factor)+'_'+n)
        '''

        # HNets or E2CNN
        filters = [net.inc.double_conv.export()[0].eval().weight.detach().cpu().numpy(),
                       net.inc.double_conv.export()[3].eval().weight.detach().cpu().numpy()[:8,:8,:,:],
                       net.down1.conv.double_conv.export()[0].eval().weight.detach().cpu().numpy()[:8,:8,:,:],
                       net.down1.conv.double_conv.export()[3].eval().weight.detach().cpu().numpy()[:8,:8,:,:],
                       net.up1.squeeze.double_conv.export()[0].eval().weight.detach().cpu().numpy()[:8,:8,:,:],
                       net.up1.squeeze.double_conv.export()[3].eval().weight.detach().cpu().numpy()[:8,:8:,:,:],
                    ]
        names = ['1_1','1_2','2_1','2_2','3_1','3_2']
        for f,n in zip(filters, names):
            plot_filter(f, args.name+'_'+n)

        mIoU_list = []
        feat_list = []
        mIoU, feats = predict_img(args.name, net, device, classes, args.data, n_channels, args.subset)


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