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
    img_inverse_roi  = torch.cat([inverse_roi_mask]*n_channels, dim=1)
    return roi_mask, inverse_roi_mask, img_inverse_roi

def predict_img(model, net, device,classes, dataset, scale, ensemble, angle=0):
    # save_patches = 'data/'+dataset+'/'+model+'_'+str(scale)+'_'+str(angle)+'_'+ensemble+'/'
    save_patches = 'evaluate_data/'+model+'_'
    if not os.path.exists(save_patches):
        os.makedirs(save_patches)
    net.eval()

    if dataset=='BCSS':
        test_dataset  = BCSS(image_set='test', factor=scale)

    elif dataset=='CRAG':
        test_dataset  = CRAG(image_set='test',  mask_channel=2, factor=scale)
    elif dataset=='GlaS':
        test_dataset  = GlaS(image_set='test', mask_channel=2,  factor=scale)
    elif dataset=='Kumar':
        test_dataset  = Kumar('test', sample_weight=None, mask_channel=2, factor=scale)
    elif 'Mosaic' in dataset:
        test_dataset  = CustomImageSet('eg', sample_weight=None, mask_channel=6)

    # print('Num of images:',test_dataset.__len__())
    if scale<1:
        batch_size=4
    elif scale<2:
        batch_size=1
    else:
        batch_size=1

    val_loader = DataLoader(test_dataset, batch_size=1, shuffle=False, num_workers=4, pin_memory=True)
    metrics_list, mIoU_list = evaluate(net, val_loader, classes, ensemble, save_patches, angle)
    i = 0
    # print(scale, mIoU_list)
    if classes==2:
        # print(f'scale:{scale}, iou: {metrics_list[-1].iou(average=False)[1]}')
        print(f'{datetime.datetime.now()}, scale:{scale}, rotation:{angle}, iou: {metrics_list[-1].iou(average=False)[1]}, {mIoU_list}')

        # print(f'scale:{scale}, iou: {metrics_list[i].iou(average=False)[-1] for i in range(6)}')
        # return metrics.iou(average=False)[-1].item()
    else:
        print(f'{datetime.datetime.now()}, scale:{scale}, rotation:{angle}, iou: {metrics_list[-1].iou(average=True)}, {mIoU_list}')
        # for i in range(6):
        #     print(f'head {i}: scale:{scale}, iou: {metrics_list[i].iou(average=True)}')
        # return metrics.iou(average=True)

    return np.array(mIoU_list).reshape(1, -1)[0,-1]

def equ_err(net, dataset, scale_1, scale_2, branch_1, branch_2, pool_size):
    err_mat = torch.empty(9,0).cuda()
    net.eval()
    channels = 12
    if dataset=='BCSS':
        test_dataset_1  = BCSS(image_set='test', factor=scale_1)
        test_dataset_2  = BCSS(image_set='test', factor=scale_2)

    val_loader_1 = DataLoader(test_dataset_1, batch_size=4, shuffle=False, num_workers=2, pin_memory=True)
    val_loader_2 = DataLoader(test_dataset_2, batch_size=4, shuffle=False, num_workers=2, pin_memory=True)
    count=0
    for batch_1, batch_2 in zip(val_loader_1, val_loader_2):
        with torch.no_grad():
            imgs_1 = batch_1['image'].cuda() #to(device=device, dtype=torch.float32))
            imgs_2 = batch_2['image'].cuda() #to(device=device, dtype=torch.float32))
            pred_list_1  = net(imgs_1)
            pred_list_2  = net(imgs_2)
            count += imgs_1.shape[0]
            if count%10 ==0:
                print('count:',count)
            for i in range(len(pred_list_1)):
                pred_list_1[i] = pred_list_1[i][:,branch_1*channels:(branch_1+1)*channels,:,:]
                pred_list_2[i] = pred_list_2[i][:,branch_2*channels:(branch_2+1)*channels,:,:]

            err = measure_error(pred_list_1, pred_list_2, pool_size)
            err_mat = torch.cat([err_mat,err], dim=1)
            # print('err_mat size:',err_mat.size())

    mean = err_mat.mean(dim=1).cpu().numpy()
    std = err_mat.std(dim=1).cpu().numpy()

    print('scale:', scale_2)
    print('mean err:', mean)
    print('std:', std)

def measure_error(f_1, f_2, pool_size):
    '''
    args:
        f_1: phi(f), Dictionary of Dictionary
        f_2: phi(Ls[f]), Dictionary of Dictionary
    '''
    count = 0
    num_datapoints = f_1[0].shape[0]
    if f_1[0].shape[2]>f_2[0].shape[2]:
        pass
    else:
        f_3 = f_1
        f_1 = f_2
        f_2 = f_3
    err_mat = torch.empty(0, num_datapoints).cuda()
    for i in range(len(f_1)):
        err = torch.norm(f_2[i]-F.avg_pool2d(f_1[i],kernel_size=pool_size), p=2, dim=(1,2,3))**2/\
                        torch.norm(F.avg_pool2d(f_1[i],kernel_size=pool_size), p=2,dim=(1,2,3))**2
        err = err.view(-1, num_datapoints)
        # print('err:',err, err.size())
        err_mat = torch.cat([err_mat, err], dim=0)
    return err_mat

def measure_error_branch(f_1, f_2):
    '''
    args:
        f_1: phi(f), Dictionary of Dictionary
        f_2: phi(Ls[f]), Dictionary of Dictionary
    '''
    print(f_1.shape,f_2.shape)
    num_datapoints = f_1.shape[0]
    if f_1.shape[-1]>f_2.shape[-1]:
        pass
    else:
        f_3 = f_1
        f_1 = f_2
        f_2 = f_3
    err_mat = torch.empty(0,1)
    for i in range(f_2.shape[0]):
        for j in range(f_1.shape[0]):
            temp =F.interpolate(f_1[j],size=(f_2[i].shape[2],f_2[i].shape[2]))
            err = torch.norm(f_2[i]-F.interpolate(f_1[j],size=(f_2[i].shape[2],f_2[i].shape[2]), mode='bilinear', align_corners=True), p=2, dim=(0,1,2,3))/\
                            torch.norm(F.interpolate(f_1[j],size=(f_2[i].shape[2],f_2[i].shape[2]), mode='bilinear', align_corners=True), p=2,dim=(0,1,2,3))
            err_mat = torch.cat([err_mat, err.view(1,1).cpu()], dim=0)
            # print('err_mat shape:', err_mat.shape)
    err_mat=err_mat.view(1,5,5)
    # print(err_mat)
    return err_mat


def evaluate(net, loader, classes, ensemble, save_patches, angle):
    n_scales = len(net.eta.view(-1))
    eta = F.softmax(net.eta.view(-1), dim=0)+1/n_scales
    eta = eta/eta.sum()
    # print(eta)
    net.eval()
    metrics = [Metrics(classes+1, ignore_index=[classes]) for _ in range(n_scales+1)]

    # mult = 255/(classes+1)
    mult = 255/4   

    mIoU_Per_Scale_Per_Branch = []
    count=0
    # channels = 12
    img_count = 0
    IMG_shape = 0
    for batch in loader:
        IMG_shape = batch['image'].shape
        break
    n_channels = IMG_shape[1]
    roi_mask, inverse_roi_mask, img_inverse_roi = get_roi_mask(IMG_shape[-1]+1, n_channels)
    inverse_roi_mask = classes*inverse_roi_mask

    for batch in loader:
        e_start=time.time()
        if ensemble=='arithmetric':
        ############# arithmetric mean ###############################################
            with torch.no_grad():
                # masks = masks.squeeze()
                # imgs  = imgs.squeeze()
                imgs = batch['image'].cuda()
                true_masks = batch['mask'].cuda()
                names = batch['name']

                # IMG_shape = imgs.shape
                # n_channels = IMG_shape[1]
                # roi_mask, inverse_roi_mask, img_inverse_roi = get_roi_mask(IMG_shape[-1]+1, n_channels)
                # inverse_roi_mask = classes*inverse_roi_mask

                # imgs  = tf.rotate(imgs, angle, fill=[1]*n_channels)*roi_mask+img_inverse_roi
                # true_masks = tf.rotate(true_masks,angle, fill=[classes])

                true_masks = torch.argmax(true_masks,dim=1,  keepdim=True)
                # true_masks = true_masks*roi_mask+inverse_roi_mask
                true_masks = true_masks.squeeze(1).type(torch.int8)

                pred_list = net(imgs)
                summed_pred=0
                count += imgs.shape[0]
                temp = torch.empty(2,0,2048,2048).cuda()
                for m,i in zip(metrics,[j for j in range(n_scales)]):
                    prob = F.softmax(pred_list[i],dim=1)

                    summed_pred += prob
                    # preds = torch.argmax(prob, dim=1).squeeze(1)
                    preds = torch.argmax(prob,dim=1).squeeze(1)
                    # preds = preds*roi_mask+inverse_roi_mask
                    preds = preds.squeeze(1).type(torch.int8)
                    print('pred shape:',preds.shape, true_masks.shape)

                    for x in range(preds.shape[0]):
                        miou,_,iou = m.get_img_iou(preds[x],true_masks[x])
                        miou = round(miou,4)
                        temp_name = names[x].split('/')[-1]
                        mask_name = save_patches+'MaxR_'+str(i)+'_'+temp_name[:-4]+'_'+str(miou)+'.png'
                        prob_name = save_patches+'H_'+str(i)+'_prob'+temp_name[:-4]+'_'+str(miou)+'.png'
                        print(mask_name, 'pred shape:',preds[x].shape, )
                        temp_pred = preds[x].cpu().numpy()*mult
                        heatmap = temp_pred.astype(np.uint8)
                        heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
                        cv2.imwrite(mask_name, heatmap)
                        # temp_prob = prob[x,1].cpu().numpy()*255
                        # heatmap = temp_prob.astype(np.uint8)
                        # heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
                        # cv2.imwrite(prob_name, heatmap)
                    preds = preds.view(-1)
                    m.add(preds, true_masks.view(-1))
                
                summed_pred = torch.argmax(summed_pred, dim=1).squeeze(1)
                summed_pred = summed_pred*roi_mask+inverse_roi_mask
                summed_pred = summed_pred.squeeze(1).type(torch.int8)

                metrics[-1].add(summed_pred.view(-1), true_masks.view(-1))
                # for x in range(summed_pred.shape[0]):
                #     miou,_,iou = metrics[-1].get_img_iou(summed_pred[x],true_masks[x])
                #     iou = round(iou[-1].item(),4)
                #     temp_name = names[x].split('/')[-1]
                #     temp_name_1 = save_patches+'arith_'+temp_name[:-4]+'_'+str(miou)+'.png'
                #     heatmap = summed_pred[x].cpu().numpy()*mult
                #     heatmap = heatmap.astype(np.uint8)
                #     heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
                #     cv2.imwrite(temp_name_1, heatmap)

                #     gt = true_masks[x].cpu().numpy()*mult
                #     heatmap = gt.astype(np.uint8)
                #     heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
                #     cv2.imwrite(save_patches+'gt_'+temp_name[:-4]+'.png', heatmap)

                img_count+=imgs.shape[0]
                # if img_count>=8:
                #     break

        elif ensemble=='R':
            with torch.no_grad():
                # masks = masks.squeeze()
                # imgs  = imgs.squeeze()
                imgs = batch['image'].cuda()
                true_masks = batch['mask'].cuda()
                names = batch['name']
                mult = 255/4
                bn = torch.nn.BatchNorm2d(classes).cuda()
                true_masks = torch.argmax(true_masks,dim=1,  keepdim=True)
                true_masks = true_masks.squeeze(1).type(torch.int8)
                pred_list = net(imgs)
                for x in range(len(pred_list)):
                    # p = bn(pred_list[x])
                    # print(x,'--', names)
                    m = Metrics(classes+1, ignore_index=[classes])
                    prob = F.softmax(pred_list[x],dim=1)
                    preds = torch.argmax(prob,dim=1).squeeze()
                    miou,_,iou = m.get_img_iou(preds,true_masks)
                    miou = round(miou,4)
                    temp_name = names[0].split('/')[-1]
                    mask_name = save_patches+str(x//4)+'_'+str(x%4)+'_'+temp_name[:-4]+'_'+str(miou)+'.png'                    
                    temp_pred = preds.cpu().numpy()
                    heatmap = (temp_pred*mult).astype(np.uint8)
                    print(mask_name, 'pred shape:',preds.shape, np.unique(heatmap))
                    heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
                    cv2.imwrite(mask_name, heatmap)

        elif ensemble=='geometric':
        ############# geometric mean ###############################################
            with torch.no_grad():
                imgs = batch['image'].cuda()
                true_masks = batch['mask'].cuda()
                true_masks = torch.argmax(true_masks, dim=1)
                pred_list = net(imgs)
                summed_pred=1
                count += imgs.shape[0]
                for m,i in zip(metrics,[j for j in range(n_scales+1)]):
                    preds = F.softmax(pred_list[i].squeeze(1),dim=1)
                    summed_pred *= preds
                    preds = torch.argmax(preds, dim=1).squeeze(1)
                    preds = preds.view(-1)
                    m.add(preds, true_masks.view(-1))
                summed_pred = torch.argmax(summed_pred**5, dim=1).squeeze(1).view(-1)
                metrics[-1].add(summed_pred, true_masks.view(-1))
        elif ensemble=='img_std':
        ############# mean img std ###############################################
            with torch.no_grad():
                imgs = batch['image'].cuda() #to(device=device, dtype=torch.float32))
                true_masks = batch['mask'].cuda() #to(device=device, dtype=torch.long))
                names = batch['name']
                true_masks = torch.argmax(true_masks, dim=1)
                pred_list = net(imgs)
                summed_pred=0
                head_idx = torch.empty(0,5)
                F_out = torch.cat(pred_list, dim=1)
                F_out = F.softmax(F_out, dim=2)
                argmax_idx = F_out.std(dim=2).mean(dim=[2,3])
                argmax_idx = argmax_idx.argmax(1)
                for k in range(F_out.shape[0]):
                    count += 1
                    for m,i in zip(metrics,[j for j in range(n_scales+1)]):
                        preds = F.softmax(pred_list[i].squeeze(1)[k],dim=0)
                        pred = torch.argmax(preds, dim=0).squeeze(1)
                        preds = pred.view(-1)
                        m.add(preds, true_masks[k].view(-1))
                        if argmax_idx[k] == i:
                            best_pred = pred
                    metrics[-1].add(best_pred.view(-1), true_masks[k].view(-1))
                    # _,_,iou = m.get_img_iou(best_pred.view(-1),true_masks[k].view(-1))
                    # iou = round(iou[-1].item(),4)
                    # temp_name = names[k].split('/')[-1]
                    # temp_name = save_patches+'I_Std_'+temp_name[:-4]+'_'+str(iou)+'.png'
                    # cv2.imwrite(temp_name, best_pred.cpu().numpy()*255)

        elif ensemble=='pixel_std':
        # ################# per-pixel std ###############################################
            with torch.no_grad():
                imgs = batch['image'].cuda()
                true_masks = batch['mask'].cuda()
                names = batch['name']
                true_masks = torch.argmax(true_masks, dim=1)
                pred_list = net(imgs)
                F_out  = torch.cat(pred_list, dim=1)    # shape of [B, S, C, H, W]
                F_pred = F.softmax(F_out,dim=2)         # shape of [B, S, C, H, W]
                F_std  = F_pred.std(dim=2)               # shape of [B, S, H, W]
                Max_Std_idx = F_std.argmax(1)           # shape of [B, H, W]
                Max_Std_idx = Max_Std_idx.unsqueeze(1)  # shape of [B, 1, H, W]
                F_y_hat= torch.argmax(F_pred,dim=2)     # shape of [B, S, H, W]
                Final_y_hat = torch.gather(F_y_hat, 1, Max_Std_idx).squeeze()
                metrics[-1].add(Final_y_hat.view(-1), true_masks.view(-1)) 
                # for x in range(Final_y_hat.shape[0]):
                #     _,_,iou = metrics[-1].get_img_iou(Final_y_hat[x],true_masks[x])
                #     iou = round(iou[-1].item(),4)
                #     temp_name = names[x].split('/')[-1]
                #     temp_name = save_patches+'P_Std_'+temp_name[:-4]+'_'+str(iou)+'.png'
                #     # print('saving to', temp_name, Final_y_hat.shape)
                #     cv2.imwrite(temp_name, Final_y_hat[x].cpu().numpy()*255)

        elif ensemble=='pixel_entropy':
        # ################# per-pixel std ###############################################
            with torch.no_grad():
                imgs = batch['image'].cuda()
                true_masks = batch['mask'].cuda()
                names = batch['name']
                true_masks = torch.argmax(true_masks, dim=1)
                pred_list = net(imgs)
                F_out  = torch.cat(pred_list, dim=1)    # shape of [B, S, C, H, W]
                F_pred = F.softmax(F_out,dim=2)         # shape of [B, S, C, H, W]
                F_entropy  = -(F_pred*torch.log(F_pred)).sum(dim=2)               # shape of [B, S, H, W]
                Max_Std_idx = F_entropy.argmax(1)           # shape of [B, H, W]
                Max_Std_idx = Max_Std_idx.unsqueeze(1)  # shape of [B, 1, H, W]
                F_y_hat= torch.argmax(F_pred,dim=2)     # shape of [B, S, H, W]
                Final_y_hat = torch.gather(F_y_hat, 1, Max_Std_idx).squeeze()
                metrics[-1].add(Final_y_hat.view(-1), true_masks.view(-1)) 
                for x in range(Final_y_hat.shape[0]):
                    _,_,iou = metrics[-1].get_img_iou(Final_y_hat[x],true_masks[x])
                    iou = round(iou[-1].item(),4)
                    temp_name = names[x].split('/')[-1]
                    temp_name = save_patches+'P_Entropy_'+temp_name[:-4]+'_'+str(iou)+'.png'
                    # print('saving to', temp_name, Final_y_hat.shape)
                    cv2.imwrite(temp_name, Final_y_hat[x].cpu().numpy()*255)
                img_count+=imgs.shape[0]

        elif ensemble=='img_ens':
        ############# mean img std weighted_ens ###############################################
            with torch.no_grad():
                imgs = batch['image'].cuda()
                true_masks = batch['mask'].cuda()
                names = batch['name']
                true_masks = torch.argmax(true_masks, dim=1)
                pred_list = net(imgs)
                F_out  = torch.cat(pred_list, dim=1)                    # shape of [B, S, C, H, W]
                F_pred = F.softmax(F_out,dim=2)                         # shape of [B, S, C, H, W]
                F_std  = F_pred.std(dim=2)                               # shape of [B, S, H, W]
                F_std  = F_std.mean(dim=(2,3))                          # shape of [B, S]
                F_std_weight  = F.softmax(F_std, dim=1)                 # shape of [B, S]
                F_std_weight=F_std_weight.unsqueeze(-1).unsqueeze(-1).unsqueeze(-1)
                # print(F_pred.size(), F_std_weight.size())
                Ensembled_prob= F_pred*F_std_weight                     # shape of [B, S, C, H, W]
                # print(Ensembled_prob.size())
                Ensembled_prob= Ensembled_prob.sum(dim=1)               # shape of [B, C, H, W]
                Final_y_hat= torch.argmax(Ensembled_prob,dim=1)         # shape of [B, H, W]
                metrics[-1].add(Final_y_hat.view(-1), true_masks.view(-1))  
                for x in range(Final_y_hat.shape[0]):
                    _,_,iou = metrics[-1].get_img_iou(Final_y_hat[x],true_masks[x])
                    iou = round(iou[-1].item(),4)
                    temp_name = names[x].split('/')[-1]
                    temp_name = save_patches+'I_Ens_'+temp_name[:-4]+'_'+str(iou)+'.png'
                    # print('saving to', temp_name, Final_y_hat.shape)
                    cv2.imwrite(temp_name, Final_y_hat[x].cpu().numpy()*255)
                img_count+=imgs.shape[0]

        elif ensemble=='pixel_ens':
        ################# per-pixel std weight_ensemble ##################################
            with torch.no_grad():
                imgs = batch['image'].cuda()
                true_masks = batch['mask'].cuda()
                names = batch['name']

                IMG_shape = imgs.shape
                n_channels = IMG_shape[1]
                roi_mask, inverse_roi_mask, img_inverse_roi = get_roi_mask(IMG_shape[-1]+1, n_channels)
                inverse_roi_mask = classes*inverse_roi_mask

                true_masks = torch.argmax(true_masks, dim=1)
                true_masks = true_masks*roi_mask+inverse_roi_mask
                true_masks = true_masks.squeeze(1).type(torch.int8)

                pred_list = net(imgs)
                pred_list = [pred_list[i].unsqueeze(1) for i in range(len(pred_list))]
                F_out  = torch.cat(pred_list, dim=1)                    # shape of [B, S, C, H, W]
                F_pred = F.softmax(F_out,dim=2)                         # shape of [B, S, C, H, W]
                F_std  = F_pred.std(dim=2)                              # shape of [B, S, H, W]
                F_std_weight  = F.softmax(F_std, dim=1).unsqueeze(2)    # shape of [B, S, 1, H, W]
                Ensembled_prob= F_pred*F_std_weight                     # shape of [B, S, C, H, W]
                Ensembled_prob= Ensembled_prob.sum(dim=1)               # shape of [B, C, H, W]
                Final_y_hat= torch.argmax(Ensembled_prob,dim=1)         # shape of [B, H, W]

                Final_y_hat = Final_y_hat*roi_mask+inverse_roi_mask
                Final_y_hat = Final_y_hat.squeeze(1).type(torch.int8)

                metrics[-1].add(Final_y_hat.view(-1), true_masks.view(-1))        
                for x in range(Final_y_hat.shape[0]):
                    miou,_,iou = metrics[-1].get_img_iou(Final_y_hat[x],true_masks[x])
                    miou = round(miou,4)
                    temp_name = names[x].split('/')[-1]
                    temp_name = save_patches+'P_Ens_'+temp_name[:-4]+'_'+str(miou)+'.png'

                    temp_pred = Final_y_hat[x].cpu().numpy()*mult
                    heatmap = temp_pred.astype(np.uint8)
                    heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
                    cv2.imwrite(temp_name, heatmap)                        
                    print('saving to', temp_name, Final_y_hat.shape)
                img_count+=imgs.shape[0]

        elif ensemble=='max_proj':
        ################# per-pixel std weight_ensemble ##################################
            with torch.no_grad():
                imgs = batch['image'].cuda()
                true_masks = batch['mask'].cuda()
                names = batch['name']
                n_channels = imgs.shape[1]
                imgs  = tf.rotate(imgs, angle, fill=[1]*n_channels)*roi_mask+img_inverse_roi
                true_masks = tf.rotate(true_masks,angle, fill=[classes])

                true_masks = torch.argmax(true_masks,dim=1,  keepdim=True)
                true_masks = true_masks*roi_mask+inverse_roi_mask
                true_masks = true_masks.squeeze().type(torch.int8)

                pred_list = net(imgs)
                pred_list = [pred_list[i].unsqueeze(1) for i in range(len(pred_list))] 

                F_out  = torch.cat(pred_list, dim=1)                    # shape of [B, S, C, H, W]
                F_out  = torch.max(F_out, dim=1)[0]                        # shape of [B, C, H, W]
                F_pred = F.softmax(F_out,dim=1)                         # shape of [B, C, H, W]
                Final_y_hat= torch.argmax(F_pred,dim=1)         # shape of [B, H, W]

                Final_y_hat = Final_y_hat*roi_mask+inverse_roi_mask
                Final_y_hat = Final_y_hat.squeeze().type(torch.int8)

                metrics[-1].add(Final_y_hat.view(-1), true_masks.view(-1))        

                # for x in range(Final_y_hat.shape[0]):
                #     miou,_,iou = metrics[-1].get_img_iou(Final_y_hat[x],true_masks[x])
                #     # iou = round(iou[-1].item(),4)
                #     temp_name = names[x].split('/')[-1]
                #     temp_name_1 = save_patches+'Max_proj_'+temp_name[:-4]+'_'+str(miou)+'.png'
                #     # print('saving to', temp_name, Final_y_hat.shape)
                #     heatmap = Final_y_hat[x].cpu().numpy().astype(np.uint8)*(255//6)
                #     heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
                #     cv2.imwrite(temp_name_1, heatmap)
                    
                #     temp_name_2 = save_patches+temp_name[:-4]+'_'+'_mask.png'
                #     heatmap = true_masks[x].cpu().numpy().astype(np.uint8)*(255//6)
                #     heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
                #     cv2.imwrite(temp_name_2, heatmap)
                img_count+=imgs.shape[0]

        elif ensemble=='pixel_distance':
        # ################# per-pixel std ###############################################
            with torch.no_grad():
                imgs = batch['image'].cuda()
                true_masks = batch['mask'].cuda()
                names = batch['name']
                n_channels = imgs.shape[1]
                imgs  = tf.rotate(imgs, angle, fill=[1]*n_channels)*roi_mask+img_inverse_roi
                true_masks = tf.rotate(true_masks,angle, fill=[classes])

                true_masks = torch.argmax(true_masks,dim=1,  keepdim=True)
                true_masks = true_masks*roi_mask+inverse_roi_mask
                true_masks = true_masks.squeeze().type(torch.int8)


                pred_list = net(imgs)
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
                Final_y_hat = torch.gather(F_y_hat, 1, Max_d_idx).squeeze()

                Final_y_hat = Final_y_hat*roi_mask+inverse_roi_mask
                Final_y_hat = Final_y_hat.squeeze().type(torch.int8)
                # print('++++++++++++++++++')
                # print('F_pred:',F_pred.shape, F_pred[0,:,:,0,0])
                # print('F_max:',F_max.shape,   F_max[0,:,:,0,0])
                # print('F_second_max:',F_second_Max.shape, F_second_Max[0,:,:,0,0])
                # print('F_distance:',F_distance.shape, F_distance[0,:,:,0,0])
                # print('Max_d_idx:',Max_d_idx.shape,   Max_d_idx[0,:,0,0])
                # print('------------------')

                metrics[-1].add(Final_y_hat.view(-1), true_masks.view(-1)) 
                # for x in range(Final_y_hat.shape[0]):
                #     miou,_,iou = metrics[-1].get_img_iou(Final_y_hat[x],true_masks[x])
                #     # iou = round(iou[-1].item(),4)
                #     temp_name = names[x].split('/')[-1]
                #     temp_name_1 = save_patches+'P_dis_'+temp_name[:-4]+'_'+str(miou)+'.png'
                #     # print('saving to', temp_name, Final_y_hat.shape)
                #     heatmap = Final_y_hat[x].cpu().numpy().astype(np.uint8)*(255//6)
                #     heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
                #     cv2.imwrite(temp_name_1, heatmap)
                    
                #     temp_name_2 = save_patches+temp_name[:-4]+'_'+'_mask.png'
                #     heatmap = true_masks[x].cpu().numpy().astype(np.uint8)*(255//6)
                #     heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
                #     cv2.imwrite(temp_name_2, heatmap)
                img_count+=imgs.shape[0]


        elif ensemble=='pixel_distance_ens':
        # ################# per-pixel std ###############################################
            with torch.no_grad():
                imgs = batch['image'].cuda()
                true_masks = batch['mask'].cuda()
                names = batch['name']
                n_channels = imgs.shape[1]
                imgs  = tf.rotate(imgs, angle, fill=[1]*n_channels)*roi_mask+img_inverse_roi
                true_masks = tf.rotate(true_masks,angle, fill=[classes])

                true_masks = torch.argmax(true_masks,dim=1,  keepdim=True)
                true_masks = true_masks*roi_mask+inverse_roi_mask
                true_masks = true_masks.squeeze().type(torch.int8)

                pred_list = net(imgs)
                pred_list = [pred_list[i].unsqueeze(1) for i in range(len(pred_list))] 
                F_out  = torch.cat(pred_list, dim=1)                                 # shape of [B, S, C, H, W]
                F_pred = F.softmax(F_out,dim=2)                                      # shape of [B, S, C, H, W]
                F_pred_temp = F_pred.clone()
                F_max = F_pred_temp.max(dim=2, keepdim=True)[0]                           # shape of [B, S, 1, H, W]
                F_pred_temp[F_pred_temp==F_max] =-1                                   # shape of [B, S, C, H, W]
                
                F_second_Max = F_pred_temp.max(dim=2, keepdim=True)[0]     # shape of [B, S, 1, H, W]
                F_distance  = (F_max-F_second_Max)                         # shape of [B, S, 1, H, W]
                F_distance  = F.softmax(F_distance,dim=1)                  # shape of [B, S, 1, H, W]
                Ensembled_prob= (F_pred*F_distance).sum(dim=1)             # shape of [B, C, H, W]
                Final_y_hat= torch.argmax(Ensembled_prob,dim=1)             # shape of [B, H, W]
                # print(Final_y_hat.shape, roi_mask.shape, inverse_roi_mask.shape)

                Final_y_hat = Final_y_hat*roi_mask+inverse_roi_mask
                Final_y_hat = Final_y_hat.squeeze().type(torch.int8)
                
                metrics[-1].add(Final_y_hat.view(-1), true_masks.view(-1)) 
                # for x in range(Final_y_hat.shape[0]):
                #     miou,_,iou = metrics[-1].get_img_iou(Final_y_hat[x],true_masks[x])
                #     # print(pred_list[-3].shape)
                #     k = 255//len(iou) 
                #     temp_name = names[x].split('/')[-1]
                #     temp_name_1 = save_patches+'P_dis_ens'+temp_name[:-4]+'_'+str(miou)+'.png'
                #     heatmap = (Final_y_hat[x].cpu().numpy()*k).astype(np.uint8)
                #     heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_RAINBOW)
                #     cv2.imwrite(temp_name_1, heatmap)

                #     temp_name_2 = save_patches+temp_name[:-4]+'_'+'_mask.png'
                #     heatmap = true_masks[x].cpu().numpy().astype(np.uint8)*k
                #     heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_RAINBOW)
                #     cv2.imwrite(temp_name_2, heatmap)
                img_count+=imgs.shape[0]

        # if img_count>=8:
        #     break
        # break
    print('num of images tested:', img_count)
    for i in range(n_scales+1):
        if classes==2:
            mIoU_Per_Scale_Per_Branch.append(metrics[i].iou(average=False)[1].item())
        else:
            mIoU_Per_Scale_Per_Branch.append(metrics[i].iou(average=True))
    return metrics, mIoU_Per_Scale_Per_Branch

def get_args():
    parser = argparse.ArgumentParser(description='Predict masks from input images',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--weight', '-w', type=str, metavar='FILE',
                        help="Specify the file in which the model is stored")
    parser.add_argument('-d', '--data', dest='data', type=str, default='Mosaics',
                        help='dataset')
    parser.add_argument('-e', '--ensemble', dest='ensemble', type=str, default='arithmetric',
                        help='srf')
    parser.add_argument('-o', '--order', dest='order', type=int, default=2,
                        help='order')
    parser.add_argument('-s', '--selection', dest='selection', type=int, default=2,
                        help='srf')
    parser.add_argument('-m', '--mode', dest='mode', type=str, default='predict',
                        help='name')
    parser.add_argument('-a', '--model', dest='model', type=str, default='R',
                        help='name')
    parser.add_argument('-r', '--n_rotation', dest='n_rotation', type=int, default=1,
                        help='num of filters')
    parser.add_argument('-k', '--n_scales', dest='n_scales', type=int, default=4,
                        help='num of filters')
    parser.add_argument('-n', '--n_filters', dest='n_filters', type=int, default=16,
                        help='num of filters')
    return parser.parse_args()

def count_your_model(model, x, y):
        # your rule here
        pass

if __name__ == "__main__":
    filters=60
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"
    args = get_args()
    torch.cuda.set_device(0)
    if args.data=='BCSS':
        classes=5
        n_channels=3
    elif 'Mosaic' in args.data:
        classes=5
        n_channels=1

    else:
        classes=2
        n_channels=3


    if args.model=='R':
        net = UNet_R(n_channels=n_channels, n_classes=classes, filters=args.n_filters, init_order=args.order, bilinear=True, \
                     init_scale=0.99, angles=[torch.tensor(0+i*math.pi/(args.n_rotation/2)) for i in range(args.n_rotation)],\
                     n_scales=args.n_scales, rotation_size=1, learn_sigma=True, selection=args.selection).cuda()
    elif args.model=='CNN':        
        net = UNet(n_channels=n_channels, n_classes=classes, filters=args.n_filters, init_order=args.order,\
               bilinear=True, srf=True, split=True, share_alpha=True, learn_sigma=True,\
               flag=False).cuda()

    # summary(net, (3, 512, 512))

    params = [p.nelement() for p in net.parameters() if p.requires_grad]
    num = sum(params)
    print(f'num of trainable parameters:{num}')

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    logging.info(f'Using device {device}')
    net.to(device=device)

    checkpoint = torch.load(args.weight, map_location=device)
    # state_dict = []
    # for n, p in checkpoint.items():
    #     print(n,p.size())
    #     state_dict.append((n[7:], p))

    # state_dict = dict(state_dict)
    # net.load_state_dict(state_dict)
    net.load_state_dict(checkpoint)
    net.eval()
    # equ_err(net, args.data, 1, 0.25, 2, 0, 4) 
    # equ_err(net, args.data, 1, 0.5, 2, 1, 2)


    r = 2**0.25
    # scales = [round(0.25*r**i,2) for i in range(4,9)]
    # scales = [round(0.25*r**i,2) for i in range(9,10)]
    # scales = [round(0.25*r**i,2) for i in range(10,11)]
    # scales = [round(0.25*r**i,2) for i in range(11,12)]
    # scales = [round(0.25*r**i,2) for i in range(12,13)]
    # scales = [round(0.25*r**i,2) for i in range(7,10)]
    scales = [1]
    angles = [0]
    # angles = [10*i for i in range(0, 36)]

    # scales = [4]
    # print('scales:',scales)
# '''
    if args.mode=='predict':
        # mIoU_matrix = np.empty([0,args.n_scales+1])
        # print("Loading model {}".format(args.weight))
        # # for factor in np.arange(0.25,2.25,0.25):
        # print('testing scales:', scales)
        # print('order:', args.order,',ensemble strategy:', args.ensemble)
        # for factor in scales:
        #     mIoU_list = predict_img('branch', net, device, classes, args.data, factor, args.ensemble)
        #     mIoU_matrix = np.vstack([mIoU_matrix, mIoU_list])
        # print(mIoU_matrix)
        # print('mean:',mIoU_matrix.mean(axis=0))
        print('-'*50,args.ensemble,'-'*50)
        print('testing angle:', angles, '\n testing scales:', scales, '\n weight:', args.weight, '\n filters:',args.n_filters, 'orientations:',args.n_rotation)
        mIoU_array = np.zeros([len(scales), len(angles)])
        for factor, i in zip(scales,[idx for idx in range(len(scales))]):
            for angle,j in zip(angles, [idx for idx in range(len(angles))]):
                mIoU = predict_img(args.model, net, device, classes, args.data, factor, args.ensemble, angle)
                mIoU_array[i,j] = mIoU
        print(mIoU_array, mIoU_array.mean())
# '''
    else:
        # ERR_SCALES = np.empty([0,224])
        for s in scales:
            count=0
            factor_1 = s
            factor_2 = 1
            if args.data=='BCSS':
                test_dataset_1  = BCSS(image_set='test', factor=factor_1)
                C=5
                size = int(512*s)
                O_size=512
                # test_dataset_2  = BCSS(image_set='test', factor=factor_2)
            elif args.data=='Kumar':
                test_dataset_1  = Kumar(image_set='test', factor=factor_1)
                C=2
                # size = int(400*s)
                O_size=400
                # test_dataset_2  = Kumar(image_set='test', factor=factor_2)
            elif dataset=='Mosaic':
                test_dataset_1  = CustomImageSet('test', sample_weight=None, mask_channel=5,  factor=factor_1, visualisation=False)
                C=5
                size = int(512*s)
                O_size=512

            if s<0.8:
                batch_size=20
            else:
                batch_size=2
            
            net = net.eval()
            val_loader_1 = DataLoader(test_dataset_1, batch_size=batch_size, shuffle=False, num_workers=4, pin_memory=True)
            # val_loader_2 = DataLoader(test_dataset_2, batch_size=1, shuffle=False, num_workers=1, pin_memory=True)
            # err_all = torch.empty(0,5,5)
            i=0
            out_dict = {i:np.empty([0,C,O_size,O_size]) for i in range(n_scales+1)}
            # for batch_1, batch_2 in zip(val_loader_1, val_loader_2):
            #     imgs_1 = batch_1['image'].to(device=device, dtype=torch.float32)
                # imgs_2 = batch_2['image'].to(device=device, dtype=torch.float32)
            with torch.no_grad():
                for batch_1 in val_loader_1:
                    imgs_1 = batch_1['image'].to(device=device, dtype=torch.float32)
                    out_1  = net(imgs_1)

            #         out_2  = net(imgs_2)
            #         # break
                    for o, d in zip(out_1,[i for i in range(n_scales)]):
                        o = o.squeeze(1).detach().cpu()
                        o = F.interpolate(o,size=(O_size, O_size), mode='bilinear', align_corners=True)
                        o = o.numpy()
                        out_dict[d]=np.concatenate([out_dict[d],o],axis=0)
                    print('finished ',out_dict[0].shape)
                    if out_dict[0].shape[0]==60:
                        fname = 'data/'+args.data+'/'+str(s)+'_'+str(count)+'.npy'
                        np.save(fname,out_dict)
                        print(fname,'saved!')
                        out_dict = {i:np.empty([0,C,O_size,O_size]) for i in range(n_scales+1)}
                        count+=1

                for o in out_dict.keys():
                    print('out:',out_dict[o].shape)
                fname = 'data/'+args.data+'/'+str(s)+'.npy'
                print(fname,'saved!')
                np.save(fname,out_dict)

            #         out_2 = torch.cat(out_2,dim=0).cpu()
            #         err = measure_error_branch(out_1, out_2)      # [1, 5, 5]
            #         err_all = torch.cat([err_all,err], dim=0)
            #         print(err_all.size())
                
            #     err_mean = err_all.mean(axis=0)
            #     err_idx  = [err_mean.argmin()//5, err_mean.argmin()%5]
            #     print('argmin idx:',err_idx)
            #     err = err_all[:err_idx[0],err_idx[1]].view(1,-1).cpu().numpy()
            #     print(err.shape)
            #     ERR_SCALES = np.vstack([ERR_SCALES, err])
            #     print(f'factor: {factor_1} vs. {factor_2}:')
        # print('overall err:', ERR_SCALES.shape, ERR_SCALES.mean())
