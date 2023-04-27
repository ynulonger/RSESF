""" Parts of the U-Net model """
import torch
import numpy as np 
import torch.nn as nn
from e2cnn import nn as enn 
from e2cnn import gspaces                                          
import torch.nn.functional as F
from srf.structured_conv_layer import *
from srf.rst_layer import *


class sSE(nn.Module):
    def __init__(self, out_channels):
        super(sSE, self).__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(in_channels=out_channels,out_channels=1,kernel_size=1,padding=0),
            nn.BatchNorm2d(1))
    def forward(self,x):
        x=self.conv(x)
        x=torch.sigmoid(x)
        return x

class cSE(nn.Module):
    def __init__(self, out_channels):
        super(cSE, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(in_channels=out_channels,out_channels=int(out_channels/2),kernel_size=1,padding=0),
            nn.BatchNorm2d(int(out_channels/2))
        )
        self.conv2 = nn.Sequential(
            nn.Conv2d(in_channels=int(out_channels/2),out_channels=out_channels,kernel_size=1,padding=0),
            nn.BatchNorm2d(out_channels)
        )
        self.activation = nn.ReLU()

    def forward(self,x):
        x=nn.AvgPool2d(x.size()[2:])(x)
        #print('channel',x.size())
        x=self.conv1(x)
        x=self.activation(x)
        x=self.conv2(x)
        x=torch.sigmoid(x)
        return x

class SCSE_Block(nn.Module):
    def __init__(self, out_channels):
        super(SCSE_Block, self).__init__()
        self.spatial_gate = sSE(out_channels)
        self.channel_gate = cSE(out_channels)

    def forward(self, x):
        g1 = self.spatial_gate(x)
        # print('g1',g1.size())
        g2 = self.channel_gate(x)
        # print('g2',g2.size())
        x = g1 * x + g2 * x
        return x

class depth_seperate_conv(nn.Module):
    """docstring for depth_seperate_conv"""
    def __init__(self, ch_in, ch_out, kernel_size, padding):
        super(depth_seperate_conv, self).__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(ch_in, ch_in, kernel_size=kernel_size, padding=padding, groups=ch_in),
            nn.Conv2d(ch_in, ch_out, kernel_size=1, padding=0, groups=1),
            nn.BatchNorm2d(ch_out),
            nn.ReLU(inplace=True)
        )
    def forward(self,x):
        x = self.conv(x)
        return x

class DoubleConv_CNN(nn.Module):
    """(convolution => [BN] => ReLU) * 2"""

    def __init__(self, in_channels, out_channels, mid_channels=None, kernel_size=3):
        super().__init__()
        if not mid_channels:
            mid_channels = out_channels
        self.double_conv = nn.Sequential(
            # depth_seperate_conv(in_channels, out_channels,kernel_size=3, padding=1),
            # depth_seperate_conv(out_channels, out_channels,kernel_size=3, padding=1)
            nn.Conv2d(in_channels, out_channels, kernel_size, padding=kernel_size//2),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True),
            nn.Conv2d(out_channels, out_channels, kernel_size, padding=kernel_size//2),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True)
        )

    def forward(self, x):
        return self.double_conv(x)

class DoubleConv(nn.Module):
    """(convolution => [BN] => ReLU) * 2"""

    def __init__(self, in_channels, out_channels, init_k=2, init_order=4, init_scale=0.65, learn_sigma=True, \
                 srf=[0,1], share_alpha=False, Min=0, Max=0.25, first=False, n_scales=3, \
                 angles = [torch.tensor(0+i*math.pi/2) for i in range(4)], rotation_size=1, k=3):
        super().__init__()
        if type(srf)==list:
            self.double_conv = nn.Sequential(
                # Srf_layer_shared(inC=in_channels, outC=out_channels, init_k=init_k, init_order=init_order, init_scale=init_scale, learn_sigma=learn_sigma, use_cuda=True),
                Srf_layer(inC=in_channels, outC=out_channels, init_k=init_k, init_order=init_order, \
                          init_scale=init_scale, learn_sigma=learn_sigma, use_cuda=True, \
                          share_alpha=share_alpha, Min=Min, Max=Max) if srf[0]==0 else \
                Srf_layer_2(inC=in_channels, outC=out_channels, init_k=init_k, init_order=init_order, 
                          init_scale=init_scale, learn_sigma=learn_sigma, use_cuda=True, \
                          share_alpha=share_alpha, Min=Min, Max=Max),
                nn.BatchNorm2d(out_channels),
                nn.ReLU(inplace=True),
                # Srf_layer_shared(inC=out_channels, outC=out_channels, init_k=init_k, init_order=init_order, init_scale=init_scale, learn_sigma=learn_sigma, use_cuda=True),
                Srf_layer(inC=out_channels, outC=out_channels, init_k=init_k, init_order=init_order, \
                          init_scale=init_scale, learn_sigma=learn_sigma, use_cuda=True, \
                          share_alpha=share_alpha, Min=Min, Max=Max) if srf[1]==0 else \
                Srf_layer_2(inC=out_channels, outC=out_channels, init_k=init_k, init_order=init_order, 
                          init_scale=init_scale, learn_sigma=learn_sigma, use_cuda=True, \
                          share_alpha=share_alpha, Min=Min, Max=Max),
                nn.BatchNorm2d(out_channels),
                nn.ReLU(inplace=True),
            )
        elif srf=='gabor':
            self.double_conv = nn.Sequential(
                GaborConv2d_lift(in_channels, out_channels, Min_sigma=Min, Max_sigma=Max) if first else \
                GaborConv2d(in_channels, out_channels, Min_sigma=Min, Max_sigma=Max),
                nn.BatchNorm2d(out_channels),
                nn.ReLU(inplace=True),
                GaborConv2d(out_channels, out_channels, Min_sigma=Min, Max_sigma=Max),
                nn.BatchNorm2d(out_channels),
                nn.ReLU(inplace=True),
            )
        elif srf=='rst':
            self.double_conv = nn.Sequential(
                RST_layer(in_channels, out_channels, init_k=init_k, init_order=init_order, init_scale=init_scale,\
                         learn_sigma=learn_sigma, use_cuda=True, groups=1, n_scales=n_scales,\
                         share_alpha=share_alpha,  Min = Min, Max = Max, \
                         angles=angles),
                nn.BatchNorm2d(out_channels),
                # nn.ReLU(inplace=True),
                RST_layer(out_channels, out_channels, init_k=init_k, init_order=init_order, init_scale=init_scale,\
                         learn_sigma=learn_sigma, use_cuda=True, groups=1, n_scales=n_scales,\
                         share_alpha=share_alpha,  Min = Min, Max = Max, \
                         angles=angles),
                nn.BatchNorm2d(out_channels),
                # nn.ReLU(inplace=True),
            )
        elif srf=='r' or srf=='R':
            self.double_conv = nn.Sequential(
                R_layer(in_channels, out_channels, init_k=init_k, init_order=init_order, init_scale=init_scale,\
                         learn_sigma=learn_sigma, use_cuda=True, groups=1, n_scales=n_scales,\
                         share_alpha=share_alpha,  Min = Min, Max = Max, angles=angles, k=k) if first else \
                Rh_layer(in_channels, out_channels, init_k=init_k, init_order=init_order, init_scale=init_scale,\
                         learn_sigma=learn_sigma, use_cuda=True, groups=1, n_scales=n_scales,\
                         share_alpha=share_alpha,  Min = Min, Max = Max, angles=angles, rotation_size=rotation_size, k=k),
                nn.BatchNorm3d(out_channels),
                nn.ReLU(inplace=True),
                Rh_layer(out_channels, out_channels, init_k=init_k, init_order=init_order, init_scale=init_scale,\
                         learn_sigma=learn_sigma, use_cuda=True, groups=1, n_scales=n_scales,\
                         share_alpha=share_alpha,  Min = Min, Max = Max, angles=angles, rotation_size=rotation_size, k=k),
                nn.BatchNorm3d(out_channels),
                nn.ReLU(inplace=True),
            )
        else:
            self.double_conv = nn.Sequential(
                nn.Conv2d(in_channels, out_channels, 3, padding=1),
                nn.BatchNorm2d(out_channels),
                nn.ReLU(inplace=True),
                nn.Conv2d(out_channels, out_channels, 3, padding=1),
                nn.BatchNorm2d(out_channels),
                nn.ReLU(inplace=True)
            )

    def forward(self, x):
        return self.double_conv(x)


class Down_CNN(nn.Module):
    """Downscaling with maxpool then double conv"""
    def __init__(self, in_channels, out_channels, kernel_size = 3):
        super().__init__()
        self.maxpool_conv = nn.Sequential(
            nn.MaxPool2d(2),
            DoubleConv_CNN(in_channels, out_channels, kernel_size=kernel_size)
        )

    def forward(self, x):
        return self.maxpool_conv(x)

class Down(nn.Module):
    """Downscaling with maxpool then double conv"""
    def __init__(self, in_channels, out_channels, init_order=2, init_scale=0.65, srf=[1,1], share_alpha=True, \
                 Min=0, Max=0.25, learn_sigma=True, n_scales=3, \
                 angles = [torch.tensor(0+i*math.pi/2) for i in range(4)], rotation_size=1, k=3):
        super().__init__()

        self.maxpool_conv = nn.Sequential(
            nn.MaxPool3d((1,2,2),(1,2,2)) if srf=='r' or srf=='R' else nn.MaxPool2d(2),
            DoubleConv(in_channels, out_channels, init_order=init_order, init_scale=init_scale, srf=srf, share_alpha=share_alpha,\
                 Min=Min, Max=Max, learn_sigma=learn_sigma, n_scales=n_scales, angles=angles, rotation_size=rotation_size, k=k) if type(srf)==list else \
            DoubleConv(in_channels, out_channels, init_order=init_order, init_scale=init_scale, srf=srf, share_alpha=share_alpha,\
                 Min=Min, Max=Max, learn_sigma=learn_sigma, n_scales=n_scales, angles=angles, rotation_size=rotation_size, k=k)
        )

    def forward(self, x):
        return self.maxpool_conv(x)

class Up_CNN(nn.Module):
    """Upscaling then double conv"""

    def __init__(self, in_channels, out_channels, bilinear=True, kernel_size=3):
        super(Up_CNN, self).__init__()

        # if bilinear, use the normal convolutions to reduce the number of channels
        if bilinear:
            self.up = nn.Sequential(nn.Upsample(scale_factor=2, mode='bilinear', align_corners=True),
                                    nn.Conv2d(in_channels=in_channels, out_channels=out_channels, kernel_size=1, stride=1)
                                    )
            self.conv = DoubleConv_CNN(in_channels, out_channels, in_channels // 2, kernel_size=kernel_size)
        else:
            self.up = nn.ConvTranspose2d(in_channels , in_channels // 2, kernel_size=2, stride=2)
            self.conv = DoubleConv_CNN(in_channels, out_channels)

    def forward(self, x1, x2):
        x1 = self.up(x1)
        # input is CHW
        diffY = x2.size()[2] - x1.size()[2]
        diffX = x2.size()[3] - x1.size()[3]

        x1 = F.pad(x1, [diffX // 2, diffX - diffX // 2,
                        diffY // 2, diffY - diffY // 2])
        # if you have padding issues, see
        # https://github.com/HaiyongJiang/U-Net-Pytorch-Unstructured-Buggy/commit/0e854509c2cea854e247a9c615f175f76fbb2e3a
        # https://github.com/xiaopeng-liao/Pytorch-UNet/commit/8ebac70e633bac59fc22bb5195e513d5832fb3bd
        x = torch.cat([x2, x1], dim=1)
        return self.conv(x)

class Up_RST(nn.Module):
    """Upscaling then double conv"""

    def __init__(self, in_channels, out_channels, init_order=1, init_scale=0.65, bilinear=True, srf=False,share_alpha=False,\
                 Min=0, Max=0.25, learn_sigma=True, angles = [torch.tensor(0+i*math.pi/2) for i in range(4)]):
        super(Up_RST, self).__init__()
        self.in_channels = in_channels
        self.out_channels = out_channels
        # if bilinear, use the normal convolutions to reduce the number of channels
        # self.filters = torch.nn.Parameter(torch.zeros([self.out_channels//5, self.in_channels//5, 2,2]), requires_grad=True) 
        # torch.nn.init.normal_(self.filters, mean=0.0, std=1)

        if bilinear:
            self.up = nn.Sequential(nn.Upsample(scale_factor=2, mode='bilinear', align_corners=True),
                                    nn.Conv2d(in_channels=in_channels, out_channels=out_channels, \
                                        kernel_size=1, stride=1),
                                    nn.ReLU(inplace=True),
                                    nn.BatchNorm2d(out_channels),
                                    )
            self.conv = DoubleConv(self.in_channels, self.out_channels, init_order= init_order,\
                                        srf=srf, share_alpha=share_alpha,Min=Min, Max=Max, learn_sigma=learn_sigma)
        else:
            self.up = nn.ConvTranspose2d(self.in_channels, self.out_channels, kernel_size=2, stride=2, groups=5)
            self.conv = DoubleConv(self.in_channels, self.out_channels, init_order=init_order,\
                                   srf=srf, share_alpha=share_alpha,Min=Min, Max=Max, learn_sigma=learn_sigma)

    def forward(self, x1, x2):
        x1 = self.up(x1)

        diffY = x2.size()[2] - x1.size()[2]
        diffX = x2.size()[3] - x1.size()[3]

        x1 = F.pad(x1, [diffX // 2, diffX - diffX // 2,
                        diffY // 2, diffY - diffY // 2])
        x = torch.cat([x2, x1], dim=1)
        return self.conv(x)

class Up_R(nn.Module):
    """Upscaling then double conv"""

    def __init__(self, in_channels, out_channels, init_order=1, bilinear=True, srf='R', share_alpha=True,\
                 Min=0, Max=0.25, learn_sigma=False, init_k=2, init_scale=0.62, n_scales=3,\
                angles = [torch.tensor(0+i*math.pi/2) for i in range(4)], rotation_size=1, k=3):
        super(Up_R, self).__init__()
        self.in_channels = in_channels
        self.out_channels = out_channels

        if bilinear:
            self.up = nn.Sequential(nn.Upsample(scale_factor=(1,2,2), mode='trilinear', align_corners=True),
                                    nn.Conv3d(in_channels=in_channels, out_channels=out_channels, \
                                        kernel_size=1, stride=1),
                                    nn.BatchNorm3d(out_channels),
                                    nn.ReLU(inplace=True),
                                    )
            self.conv = DoubleConv(self.in_channels, self.out_channels, init_order= init_order, init_scale=init_scale, srf=srf, \
                                    share_alpha=share_alpha, Min=Min, Max=Max, learn_sigma=learn_sigma,\
                                    angles = angles, n_scales=n_scales, rotation_size=rotation_size, k=k)
        else:
            self.up = nn.ConvTranspose2d(self.in_channels, self.out_channels, kernel_size=2, stride=2, groups=5)
            self.conv = DoubleConv(self.in_channels, self.out_channels, init_order=init_order, init_scale=init_scale,\
                                   srf=srf, share_alpha=share_alpha, Min=Min, Max=Max, learn_sigma=learn_sigma)

    def forward(self, x1, x2):
        # B, C, R, H, W = x1.shape
        # x1 = x1.view(B, C*R, H, W)
        x1 = self.up(x1)

        diffY = x2.size()[3] - x1.size()[3]
        diffX = x2.size()[4] - x1.size()[4]

        x1 = F.pad(x1, [diffX // 2, diffX - diffX // 2,
                        diffY // 2, diffY - diffY // 2])
        x = torch.cat([x2, x1], dim=1)
        return self.conv(x)


class Up(nn.Module):
    """Upscaling then double conv"""

    def __init__(self, in_channels, out_channels, init_order=2, bilinear=True, srf=False,share_alpha=False,\
                 Min=0, Max=0.25, learn_sigma=True):
        super(Up, self).__init__()
        self.in_channels = in_channels
        self.out_channels = out_channels
        # if bilinear, use the normal convolutions to reduce the number of channels
        # self.filters = torch.nn.Parameter(torch.zeros([self.out_channels//5, self.in_channels//5, 2,2]), requires_grad=True) 
        # torch.nn.init.normal_(self.filters, mean=0.0, std=1)

        if bilinear:
            self.squeeze = nn.Conv2d(in_channels//5, out_channels//5, 1, 1)
            # self.up = nn.Sequential(nn.Upsample(scale_factor=2, mode='bilinear', align_corners=True),
                                    # nn.Conv2d(in_channels=in_channels, out_channels=out_channels, kernel_size=1, stride=1, groups=5)
                                    # Srf_layer_2(inC=self.in_channels, outC=self.out_channels, init_k=2, 
                                    #             init_order=2, init_scale=0, learn_sigma=True, use_cuda=True, \
                                    #             share_alpha=True, Min=Min, Max=Max)
                                    # )
            self.up = nn.Upsample(scale_factor=2, mode='bilinear', align_corners=True)
            self.conv = DoubleConv(self.in_channels, self.out_channels, init_order= init_order,\
                                   srf=srf, share_alpha=share_alpha,Min=Min, Max=Max, learn_sigma=learn_sigma) if type(srf)==list else \
                        DoubleConv(in_channels, out_channels, srf=srf, Min=Min, Max=Max)
        else:
            self.up = nn.ConvTranspose2d(self.in_channels, self.out_channels, kernel_size=2, stride=2, groups=5)
            self.conv = DoubleConv(self.in_channels, self.out_channels, init_order=init_order,\
                                   srf=srf, share_alpha=share_alpha,Min=Min, Max=Max, learn_sigma=learn_sigma)

    def forward(self, x1, x2):
        x1 = self.up(x1)
        # x1 = F.conv2d(input=x1, weight=self.filters, bias=None, stride=1, groups=5)
        # print(x1.shape, self.up.weight.shape)
        x1_0 = self.squeeze(x1[:,0:self.in_channels//5,:,:])
        x1_1 = self.squeeze(x1[:,self.in_channels//5*1:self.in_channels//5*2,:,:])
        x1_2 = self.squeeze(x1[:,self.in_channels//5*2:self.in_channels//5*3,:,:])
        x1_3 = self.squeeze(x1[:,self.in_channels//5*3:self.in_channels//5*4,:,:])
        x1_4 = self.squeeze(x1[:,self.in_channels//5*4:self.in_channels//5*5,:,:])

        # x1_0 = F.conv2d(input=x1[:,0:self.in_channels//5,:,:], weight=self.filters, bias=None, stride=1)
        # x1_1 = F.conv2d(input=x1[:,self.in_channels//5*1:self.in_channels//5*2,:,:], weight=self.filters, bias=None, stride=1)
        # x1_2 = F.conv2d(input=x1[:,self.in_channels//5*2:self.in_channels//5*3,:,:], weight=self.filters, bias=None, stride=1)
        # x1_3 = F.conv2d(input=x1[:,self.in_channels//5*3:self.in_channels//5*4,:,:], weight=self.filters, bias=None, stride=1)
        # x1_4 = F.conv2d(input=x1[:,self.in_channels//5*4:self.in_channels//5*5,:,:], weight=self.filters, bias=None, stride=1)
        
        x1 = torch.cat((x1_0,x1_1,x1_2,x1_3,x1_4),dim=1)
        # print(x1_0.shape)
        # print(x1.shape)

        # input is CHW
        diffY = x2.size()[2] - x1.size()[2]
        diffX = x2.size()[3] - x1.size()[3]

        x1 = F.pad(x1, [diffX // 2, diffX - diffX // 2,
                        diffY // 2, diffY - diffY // 2])
        x = torch.cat([x2, x1], dim=1)
        x = channel_shuffle(x, 2)
        return self.conv(x)

def channel_shuffle(x, groups):
    batchsize, num_channels, height, width = x.data.size()
    channels_per_group = num_channels // groups
    # num_channels = groups * channels_per_group
    # b, num_channels, h, w =======>  b, groups, channels_per_group, h, w
    x = x.view(batchsize, groups, channels_per_group, height, width)
    x = torch.transpose(x, 1, 2).contiguous()
    # x.shape=(batchsize, channels_per_group, groups, height, width)
    # flatten
    x = x.view(batchsize, -1, height, width)
    return x

class R_OutConv(nn.Module):
    def __init__(self, in_channels, out_channels, n_scales, n_rotations, selection=2):
        super(R_OutConv, self).__init__()
        self.n_scales = n_scales
        self.n_rotations = n_rotations
        self.selection = selection
        # share channel squeeze layer between scale branches
        self.conv = nn.Conv2d(in_channels, out_channels, kernel_size=1)

        # each scale branch has its own channel squeeze layer
        # self.conv = nn.ModuleList([nn.Conv2d(in_channels, out_channels, kernel_size=1) for i in range(n_scales)])

    def forward(self, x):
        # print('last layer out:', x.shape)
        if self.training or self.selection==0:
            # Pooling over R rotation channels, return prediction for each scale s.
            B, C, N, H, W = x.shape
            x = x.view(B,C,self.n_rotations,self.n_scales,H,W)
            x = x.max(dim=2)[0]
            # share channel squeeze layer between scale branches
            out = [self.conv(x[:,:,i,:,:]) for i in range(self.n_scales)]

            # each scale branch has its own channel squeeze layer
            # out = [self.conv[i](x[:,:,i,:,:]) for i in range(self.n_scales)]
        else:
            if self.selection==1:
            # Pooling over R & S  
                print('Pooling over R & S')      
                B, C, N, H, W = x.shape
                x = x.max(dim=2)[0]
                out = self.conv(x)
            
            elif self.selection==2:
                # select a rotation channel r for each pixel, at each scale s.  
                B, C, N, H, W = x.shape
                x = x.view(B,C,self.n_rotations,self.n_scales,H,W)
                out_m = x.sum(dim=[1]).squeeze(0)  # [Nr, Ns, H, W]
                out_m_idx = out_m.max(dim=0)[1].detach()  # [Ns, H, W]
                out_m_idx = out_m_idx.unsqueeze(0).unsqueeze(0).unsqueeze(0)  # [B, C, Nr, Ns, H, W]
                out_m_idx = torch.repeat_interleave(out_m_idx, C, dim=1)
                x = torch.gather(x, 2, out_m_idx).squeeze(2)  # [B, C, Ns, H, W]
                # print('x shape:', x.shape)
                out = [self.conv(x[:,:,i,:,:]) for i in range(self.n_scales)] #[B, C, H, W]
            
            elif self.selection==3:
                # Generate prediction for each Rotation channel and Scale channel, R*S predictions in total.
                B, C, N, H, W = x.shape
                out = [self.conv(x[:,:,i,:,:]) for i in range(N)]
            
            elif self.selection==4:
                # select R^c for each c, and each s.
                B, C, N, H, W = x.shape
                x = x.view(B,C,self.n_rotations,self.n_scales,H,W)
                x_mean = x.mean(dim=[4,5]).squeeze()    # [C, Nr, Ns]
                max_idx = x_mean.max(dim=1)[1].unsqueeze(1).unsqueeze(0).unsqueeze(-1).unsqueeze(-1).clone().detach()  # [1, C, 1, Ns, 1, 1]
                max_idx = torch.repeat_interleave(max_idx, H, dim=4)
                max_idx = torch.repeat_interleave(max_idx, W, dim=5)  # [1, C, 1, Ns, H, W]
                out = torch.gather(x, 2, max_idx).squeeze(2)    # [1, C, Ns, H, W]
                # print('idx shape:', max_idx.shape, 'out shape:', out.shape)
                # print('max idx',x_mean.max(dim=2)[1], 'max idx:',max_idx.shape, 'out shape:', out.shape)
                out = [self.conv(out[:,:,i,:,:]) for i in range(self.n_scales)]
                # out = self.conv(out)

            elif self.selection==5:
                # ''' 11-02-2023
                # Selecting R* over C and H,W! Final!!!
                # print('Selecting R over C, then ensemble over S best version!')
                B, C, N, H, W = x.shape
                x = x.view(B,C,self.n_rotations,self.n_scales,H,W)
                # out_m = x.mean(dim=[4,5])   # [B, C, Nr, Ns]
                out_m = x.sum(dim=[1,4,5]).squeeze(0)  # [Nr, Ns]
                out_m_idx = out_m.max(dim=0)[1].detach().cpu().numpy()
                # share squeeze layer
                out = [self.conv(x[:,:,out_m_idx[i],i,:,:]) for i in range(self.n_scales)] #[B, C, H, W]    
                # don't share squeeze layer
                # out = [self.conv[i](x[:,:,out_m_idx[i],i,:,:]) for i in range(self.n_scales)]
                # print(f'Selecting branch {branch}')
                # out = self.conv(x[:,:,out_m_idx[branch], branch,]) #[B, C, H, W]
                # out = self.conv(x) #[B, C, H, W]
                # print('out shape:', out.shape)
                # '''
            elif self.selection==6:
                # Selecting one prediction  over R & S over C
                B, C, N, H, W = x.shape
                x = x.view(B,C,self.n_rotations,self.n_scales,H,W)
                out_m = out_m.sum(dim=[1,4,5])  # [B, Nr, Ns]
                out_m_idx = out_m.max(dim=1)[1].squeeze().detach().cpu().numpy()
                final_rotation_idx = np.bincount(out_m_idx)
                final_rotation_idx = np.argmax(final_rotation_idx)
                
                out_m = x[:,:,final_rotation_idx,:,:,:]  # [B, C, Ns, H, W]
                out_m = out_m.mean(dim=[3,4])  # [B, C, Ns]
                out_m_idx = out_m.max(dim=2)[1].squeeze().detach().cpu().numpy()
                final_scale_idx = np.bincount(out_m_idx)
                final_scale_idx = np.argmax(final_scale_idx)

                # print('max rotation idx:', final_rotation_idx, 'max scale idx:', final_scale_idx)
                out = self.conv(x[:,:,final_rotation_idx,final_scale_idx,:,:])

            elif self.selection==7:
                # Generate prediction for each Rotation channel and Scale channel, R*S predictions in total.
                B, C, N, H, W = x.shape
                x = x.view(B,C,self.n_rotations,self.n_scales,H,W)
                out = [self.conv(x[:,:,i,2,:,:]) for i in range(self.n_rotations)]

            elif self.selection==9:
                # select Rotation channel and Scale channel for each C channel.
                B, C, N, H, W = x.shape
                print('BatchNorm2d...')
                bn = torch.nn.BatchNorm2d(C*N).cuda()
                # print('layerNorm...')
                # bn = torch.nn.LayerNorm(C*N).cuda()
                # print('instanceNorm...')
                # bn = torch.nn.InstanceNorm2d(C*N).cuda()
                x_prime = x.view(B,-1,H,W)
                x_prime = bn(x_prime)
                x_prime = x_prime.view(B,C,N,H,W)


                out_m = x_prime.sum(dim=[1]).squeeze(0)  # [N, H, W]
                out_m_idx = out_m.max(dim=0)[1].detach()  # [H, W]
                out_m_idx = out_m_idx.unsqueeze(0).unsqueeze(0).unsqueeze(0)  # [B, C, N, H, W]
                out_m_idx = torch.repeat_interleave(out_m_idx, C, dim=1)
                x = torch.gather(x, 2, out_m_idx).squeeze(2)  # [B, C, H, W]
                # print('x shape:', x.shape)
                out = self.conv(x) #[B, C, H, W]
            
            elif self.selection==10:
                # blur feature maps by 5*5 window, then select a rotation channel r for each pixel, at each scale s.  
                B, C, N, H, W = x.shape
                filters = torch.ones(1, C, 1, 5, 5).cuda()
                x_prime = F.conv3d(x, filters, padding='same') #[B, 1, N, H, W]
                out_m = x_prime.squeeze()  #[N, H, W]
                out_m_idx = out_m.max(dim=0)[1].detach()  # [H, W]
                out_m_idx = out_m_idx.unsqueeze(0).unsqueeze(0).unsqueeze(0)  # [1, 1, 1, H, W]
                out_m_idx = torch.repeat_interleave(out_m_idx, C, dim=1)
                x = torch.gather(x, 2, out_m_idx).squeeze(2)  # [B, C, H, W]
                # print('x shape:', x.shape)
                out = self.conv(x) #[B, C, H, W]
            
        return out

class R_Pool_OutConv(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(R_Pool_OutConv, self).__init__()
        self.conv = nn.Conv2d(in_channels, out_channels, kernel_size=1)

    def forward(self, x):
        B, C, N, H, W = x.shape
        x = x.max(dim=2)[0]
        out = self.conv(x)
        return out

class OutConv(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(OutConv, self).__init__()
        self.conv = nn.Conv2d(in_channels, out_channels, kernel_size=1)

    def forward(self, x):
        return self.conv(x)

class OutConv_share(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(OutConv_share, self).__init__()
        self.in_channels = in_channels
        self.squeeze = nn.Conv2d(self.in_channels//5, out_channels, kernel_size=1)

    def forward(self, x1):
        x1_0 = self.squeeze(x1[:,0:self.in_channels//5,:,:]).unsqueeze(1)
        x1_1 = self.squeeze(x1[:,self.in_channels//5*1:self.in_channels//5*2,:,:]).unsqueeze(1)
        x1_2 = self.squeeze(x1[:,self.in_channels//5*2:self.in_channels//5*3,:,:]).unsqueeze(1)
        x1_3 = self.squeeze(x1[:,self.in_channels//5*3:self.in_channels//5*4,:,:]).unsqueeze(1)
        x1_4 = self.squeeze(x1[:,self.in_channels//5*4:self.in_channels//5*5,:,:]).unsqueeze(1)
        x = [x1_0,x1_1,x1_2,x1_3,x1_4]
        return x

class OutConv_share_ens(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(OutConv_share_ens, self).__init__()
        self.in_channels = in_channels
        self.squeeze = nn.Sequential(nn.Conv2d(self.in_channels//5, out_channels, kernel_size=1),
                                     nn.Softmax(dim=1))
        self.conv = nn.Conv2d(out_channels*5, out_channels, kernel_size=5, padding=2)

    def forward(self, x1):
        x1_0 = self.squeeze(x1[:,0:self.in_channels//5,:,:])
        x1_1 = self.squeeze(x1[:,self.in_channels//5*1:self.in_channels//5*2,:,:])
        x1_2 = self.squeeze(x1[:,self.in_channels//5*2:self.in_channels//5*3,:,:])
        x1_3 = self.squeeze(x1[:,self.in_channels//5*3:self.in_channels//5*4,:,:])
        x1_4 = self.squeeze(x1[:,self.in_channels//5*4:self.in_channels//5*5,:,:])
        x = torch.cat([x1_0,x1_1,x1_2,x1_3,x1_4],dim=1)
        x = self.conv(x)
        return x

class einConv(nn.Module):
    """(convolution => [BN] => ReLU) * 2"""
    def __init__(self, in_channels, out_channels, rotations=8, kernel_size=5):
        super().__init__()
        maximum_frequency=3 if rotations==-1 else None
        r2_act = gspaces.Rot2dOnR2(N=rotations, maximum_frequency=maximum_frequency)
        type_in  = enn.FieldType(r2_act,  in_channels*[r2_act.trivial_repr])     #  6
        type_out = enn.FieldType(r2_act, out_channels*[r2_act.trivial_repr if rotations==-1 else r2_act.regular_repr])     #  7
        self.type_in = type_in

        self.double_conv = enn.SequentialModule(
            enn.R2Conv(type_in, type_out, kernel_size=kernel_size, padding=kernel_size//2, bias=False),
            enn.InnerBatchNorm(type_out),
            enn.ReLU(type_out, inplace=True),
            enn.R2Conv(type_out, type_out, kernel_size=kernel_size, padding=kernel_size//2, bias=False),
            enn.InnerBatchNorm(type_out),
            enn.ReLU(type_out, inplace=True)
        )

    def forward(self, x):
        x = enn.GeometricTensor(x, self.type_in)
        return self.double_conv(x)

class eDoubleConv(nn.Module):
    """(convolution => [BN] => ReLU) * 2"""
    def __init__(self, in_channels, out_channels, rotations=8, kernel_size=5):
        super().__init__()
        maximum_frequency=3 if rotations==-1 else None
        r2_act = gspaces.Rot2dOnR2(N=rotations, maximum_frequency=maximum_frequency)
        type_in  = enn.FieldType(r2_act, in_channels*[r2_act.trivial_repr if rotations==-1 else r2_act.regular_repr])
        type_out = enn.FieldType(r2_act, out_channels*[r2_act.trivial_repr if rotations==-1 else r2_act.regular_repr])     #  7
        self.type_in = type_in

        self.double_conv = enn.SequentialModule(
            enn.R2Conv(type_in, type_out, kernel_size=kernel_size, padding=kernel_size//2, bias=False),
            enn.InnerBatchNorm(type_out),
            enn.ReLU(type_out, inplace=True),
            enn.R2Conv(type_out, type_out, kernel_size=kernel_size, padding=kernel_size//2, bias=False),
            enn.InnerBatchNorm(type_out),
            enn.ReLU(type_out, inplace=True)
        )

    def forward(self, x):
        return self.double_conv(x)

class eDown(nn.Module):
    """Downscaling with maxpool then double conv"""
    def __init__(self, in_channels, out_channels, rotations=8, kernel_size = 5):
        super().__init__()
        self.conv = eDoubleConv(in_channels, out_channels, rotations, kernel_size=kernel_size)

    def forward(self, x):
        y = enn.PointwiseMaxPool(x.type, kernel_size=2, stride=2)(x)
        y = self.conv(y)
        return y

class eUp(nn.Module):
    """Upscaling then double conv"""
    def __init__(self, in_channels, out_channels, rotations=8, kernel_size=5):
        super().__init__()
        self.squeeze = eDoubleConv(in_channels, out_channels, rotations, kernel_size=kernel_size)
        self.conv = eDoubleConv(in_channels, out_channels, rotations, kernel_size=kernel_size)
            
    def forward(self, x1, x2):
        x1 = enn.R2Upsampling(x1.type, scale_factor=2, align_corners=True)(x1)
        x1 = self.squeeze(x1)
        # input is CHW
        diffY = x2.size()[2] - x1.size()[2]
        diffX = x2.size()[3] - x1.size()[3]
        x1_type = x1.type
        x1 = F.pad(x1.tensor, [diffX // 2, diffX - diffX // 2,
                        diffY // 2, diffY - diffY // 2])
        x1 = enn.GeometricTensor(x1, x1_type)
        x = enn.tensor_directsum([x2, x1])
#         print('x shape:',x.shape)
        return self.conv(x)


