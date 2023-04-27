import os
import glob
import torch
import argparse
import numpy as np
import torch.nn as nn
from torch.autograd import Variable
from torch.utils.data import DataLoader

def measure_error(f_1, f_2, num_datapoints, mode='best'):
    '''
    args:
        f_1: phi(f), Dictionary of Dictionary
        f_2: phi(Ls[f]), Dictionary of Dictionary
    '''
    for i in range(5):
        f_1[i] = torch.tensor(f_1[i]).cuda()
        f_2[i] = torch.tensor(f_2[i])

    if mode=='best':
        err_mat = torch.empty(num_datapoints,0).cuda()
        for i in range(5):
            for j in range(5):
                err = torch.norm(f_2[i]-f_1[i], p=2, dim=(1,2,3))/torch.norm(f_1[j], p=2,dim=(1,2,3))
                err = err.view(-1,1)
                err_mat = torch.cat([err_mat, err], dim=1)

        err_mat_mean = err_mat.mean(dim=0)
        err_min = err_mat[:,err_mat_mean.argmin()]
        return err_min.view(-1,1)

    elif mode=='mean':
        f_1_mean =0
        f_2_mean =0
        for i in range(5):
            f_1_mean += f_1[i]
            f_2_mean += f_2[i]
        err = torch.norm(f_2_mean-f_1_mean, p=2, dim=(1,2,3))/torch.norm(f_1_mean, p=2,dim=(1,2,3))
        err = err.view(-1,1)
        return err
    # elif mode=='p_dist':
    # 	pred_list_1 = [f_1[i].unsqueeze(1) for i in range(5)]
    # 	pred_list_2 = [f_2[i].unsqueeze(1) for i in range(5)]

    # 	F_out_1  = torch.cat(pred_list_1, dim=1)                                 # shape of [B, S, C, H, W]
    # 	F_out_2  = torch.cat(pred_list_2, dim=1)                                 # shape of [B, S, C, H, W]

    #     F_pred_1 = F.softmax(F_out_1,dim=2)                                      # shape of [B, S, C, H, W]
    #     F_pred_temp_1 = F_pred_1.clone()
    #     F_max_1 = F_pred_temp_1.max(dim=2, keepdim=True)[0]                           # shape of [B, S, 1, H, W]
    #     F_pred_temp_1[F_pred_temp_1==F_max_1] =-1                                   # shape of [B, S, C, H, W]
        
    #     F_second_Max_1 = F_pred_temp_1.max(dim=2, keepdim=True)[0]     # shape of [B, S, 1, H, W]
    #     F_distance_1  = (F_max_1-F_second_Max_1)                         # shape of [B, S, 1, H, W]
    #     Max_d_idx_1 = F_distance_1.argmax(1)                                 # shape of [B, 1, H, W]
    #     F_out_1 = torch.gather(F_out_1, 1, Max_d_idx).squeeze()
    # elif mode=='p_ens':

    # print(err_mat.shape, err_mat_mean.shape, err_mat_mean.argmin(), err_mat_mean.min())

def get_args():
    parser = argparse.ArgumentParser(description='Predict masks from input images',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-d', '--data', dest='data', type=str, default='BCSS',
                        help='dataset')
    parser.add_argument('-f', '--factor', dest='factor', type=float, default=1,
                        help='factor')
    parser.add_argument('-e', '--ens', dest='ens', type=str, default='best',
                        help='factor')
    return parser.parse_args()

if __name__ == "__main__":
    args = get_args()
    print(f'-----------{args.ens}-----------')
    r = 2**0.25
    # scales = [round(0.25*r**i,2) for i in range(0,17)]
    scales = [round(0.25*r**i,2) for i in range(0,8)]+[round(0.25*r**i,2) for i in range(9,17)]
    print('scales', scales)
    if args.data=='Kumar':
        err_all = torch.empty(224,0).cuda()
    elif args.data=='BCSS':
        err_all = torch.empty(1200,0).cuda()

    for s in scales:

        base_files = glob.glob(f'data/{args.data}/1.0*')
        base_files.sort()

        scaled_files = glob.glob(f'data/{args.data}/{s}*')
        scaled_files.sort()
        err_per_scale = torch.empty(0,1).cuda()
        for b_file, s_file in zip(base_files, scaled_files):
            # print(b_file, s_file)
            b_dataset = np.load(b_file, allow_pickle=True).item()
            s_dataset = np.load(s_file, allow_pickle=True).item()
            temp_err = measure_error(b_dataset, s_dataset, b_dataset[0].shape[0],args.ens)
            err_per_scale = torch.cat([err_per_scale, temp_err], dim=0)
        print('scale:',s, 'err_per_scale:', err_per_scale.mean().item(), err_per_scale.shape)
        err_all = torch.cat([err_all, err_per_scale], dim=1)
    print('err_all:',err_all.shape, 'overall_err:', err_all.mean())