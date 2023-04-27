# Import general dependencies
import numpy as np
import math
import torch
from torch.autograd import Variable
import torch.nn as nn
from torchvision import transforms
from torch.autograd import Function
from torch.distributions import normal
from srf.rst_basis import *
# from gaussian_basis_filters import *
from torch.utils.data import DataLoader
# from dataset import *
import gc
import torch.nn.functional as F
import time
import cv2
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle



""" The N-Jet convolutional-layer using a linear combination of 
Gaussian derivative filters.
Inputs:
    - inC: input channels
    - outC: output channels
    - init_k: the spatial extent of the kernels (default: 2)
    - init_order: the order of the approximation (default: 3)
    - init_scale: the initial starting scale, where: sigma=2^scale (default: 0)
    - learn_sigma: whether sigma is learnable
    - use_cuda: running on GPU or not
    - groups: groups for the convolution (default: 1)
    - ssample: if we subsample the featuremaps based on sigma (default: False)
"""

class RST_layer(nn.Module):
    def __init__(self, inC, outC, init_k, init_order, init_scale, learn_sigma, use_cuda, groups=1, n_scales=1,
                share_alpha=False,  Min = 0, Max = 0.5, angles=[torch.tensor(0)]):
        super(RST_layer, self).__init__()
        # self.constraint_sigma = constraint_sigma
        self.share_alpha = share_alpha
        self.init_k = init_k
        self.init_order = init_order
        self.init_scale = init_scale
        self.inC = inC
        self.Min = torch.arange(Min,Max,(Max-Min)/n_scales).cuda()
        self.Max = torch.arange(Min+0.5,Max+0.5,(Max-Min)/n_scales).cuda()
        self.n_scales  = n_scales
        self.learn_sigma = learn_sigma
        assert(outC % groups == 0)
        self.outC = outC
        self.groups = groups 
        self.angles=angles
        """ Define the number of basis based on order. """
        N = int((self.init_order + 1) * (self.init_order + 2) / 2)                        

        """ Create weight variables. """
        self.use_cuda = use_cuda
        # self.device = torch.device("cuda" if use_cuda else "cpu")
        if share_alpha:
            self.alphas = torch.nn.Parameter(torch.zeros([N, int(inC/groups), self.outC]),
                                             requires_grad=True) 
        else:
            self.alphas = torch.nn.Parameter(torch.zeros([self.n_scales, F, int(inC/groups), self.outC]), 
                                             requires_grad=True) 

        """ Define the scale parameter. """
        torch.nn.init.normal_(self.alphas, mean=0.0, std=1)
        # self.scales = torch.zeros([self.n_scales], requires_grad=True).cuda()
        # self.sigma = ((self.Max-self.Min)/2)*torch.tanh(self.scales)+((self.Min+self.Max)/2)                     

        if self.learn_sigma==True or self.learn_sigma=='free':    
            # self.sigma = torch.nn.Parameter(self.sigma, requires_grad=True)   
            self.scales = torch.nn.Parameter(torch.zeros([self.n_scales], dtype=torch.float32), requires_grad=True) 
            # torch.nn.init.normal_(self.scales, mean=0.0, std=0.1)
        else:
            self.scales = torch.nn.Parameter(torch.tensor(np.full((self.n_scales), self.init_scale),\
                                            dtype=torch.float32), requires_grad=False)      
                                            
        # self.sigma = torch.zeros((1,self.n_scales))  
        self.filtersize = torch.zeros((1,))                                     
        self.hermite = torch.Tensor()                                           
        self.x = torch.Tensor()                                                 
        self.filters = torch.Tensor()  

        # self.basis = []                                             
        # self.gauss = []   

    """ Forward pass with inputs: creates the filters and performs the convolution. """
    def forward(self, data): 
        """ Define sigma from the scale: sigma = 2^scale """
        # self.sigma = 2.0**self.scales
        # print('----------', self.sigma.size(), self.Min.size())
        # if self.constraint_sigma:
        #     self.sigma = torch.clamp(self.sigma, min=self.Min, max=self.Max)
        # print('----------------------------------------------------')
        # print(f'sigma:{self.sigma}, alpha:{self.alphas.size() }')
        # self.filtersize = torch.ceil(self.init_k*self.sigma+0.5)
        if self.learn_sigma==True:
            self.sigma = ((self.Max-self.Min)/2)*torch.tanh(self.scales)+((self.Min+self.Max)/2)  
        elif self.learn_sigma=='free':
            self.sigma = 2.0**self.scales
        else:
            self.sigma = (self.Max+self.Min)/2
            # self.sigma=self.Max

        # print('sigma:',self.sigma)
        self.filtersize = 2*torch.ceil(self.init_k*self.sigma)
        # self.filtersize = torch.ceil(3*self.sigma)
        # print('sigma:',self.sigma, 'filter size:', self.filtersize*2+1)

        filter_list = []
        
        """ Define the grid on which the filter is created. """
        for i in range(self.n_scales):
            # try:
            x = torch.arange(start=-self.filtersize[i].detach().cpu().float(), \
                    end=self.filtersize[i].detach().cpu().float()+1, step=1)
            y = torch.arange(start=-self.filtersize[i].detach().cpu().float(), \
                    end=self.filtersize[i].detach().cpu().float()+1, step=1)
            # except: 
            #     print("Sigma value is off:", self.sigma, "filter size:", self.filtersize)


            """ Create the Gaussian derivative filters. """
            if self.share_alpha:
                filters, basis = gaussian_basis_filters(x=x, y=y, order=self.init_order, sigma=self.sigma[i], 
                            alphas=self.alphas, use_cuda=self.use_cuda, angles=self.angles)
            else:
                filters, basis = gaussian_basis_filters(x=x_theta, y=y_theta, order=self.init_order, sigma=self.sigma[i], 
                            alphas=self.alphas[i], use_cuda=self.use_cuda, angles=self.angles)
#             print('filters:',filters.shape)
            # kernel in shape [num_rotations, 1, out_channels, in_channels, H, W]
            filter_list.append(filters)
            # self.basis.append(basis)

        if len(torch.unique(self.filtersize)) == 1:
            self.filters = torch.cat(filter_list,dim=1)
        else:
            # print('filter size:', torch.unique(self.filtersize))
            max_size = self.filtersize.max()
            for i in range(len(filter_list)):
                pad_size = max_size*2+1-filter_list[i].shape[-1]
                pad_size = int(pad_size.cpu().item()/2)
                filter_list[i] = F.pad(filter_list[i],(pad_size, pad_size, pad_size, pad_size),"constant", 0)
            self.filters = torch.cat(filter_list,dim=1)
            # kernel in shape [num_rotations, num_scales, out_channels, in_channels, H, W]
        self.filters = self.filters.permute(2,0,1,3,4,5).contiguous()
#         print('-'*10, 'filter shape:', self.filters.shape)
        # kernel in shape [out_channels, num_rotations, num_scales, in_channels, H, W]
        self.filters = self.filters.view(-1, self.inC, self.filters.shape[-2], self.filters.shape[-1])
#         print('filters---:',self.filters.shape)

        """ Perform the convolution. """
        final_conv = F.conv2d(input=data, # NCHW
                              weight=self.filters, # KCHW
                              bias=None, stride=1, padding=int(self.filters.shape[2]/2))
        # final_conv = torch.sigmoid(final_conv)
        final_conv = F.relu(final_conv)

#         print('final conv:', final_conv.shape)
        final_conv = final_conv.view(-1, self.outC, len(self.angles), self.n_scales, final_conv.shape[-2],final_conv.shape[-1]).squeeze(3)
#         print('final conv (after reshape):', final_conv.shape)
        f_argmax = final_conv.mean(dim=(-1,-2)).max(dim=2)[1]
#         print('arg max idx:', f_argmax)
        f_argmax = f_argmax.view(f_argmax.shape[0],f_argmax.shape[1],1,1,1).repeat(1,1,1,final_conv.shape[-2],final_conv.shape[-1])
        out = torch.gather(final_conv,2,f_argmax).squeeze(2)
        return out

    """ List the parameters. """
    def num_params(self):
        return (sum(p.numel() for p in self.parameters() if p.requires_grad))

class R_layer(nn.Module):
    def __init__(self, inC, outC, init_k, init_order, init_scale, learn_sigma, use_cuda, groups=1, n_scales=5,
                share_alpha=False, Min = torch.tensor([0.33, 0.66, 0.99]), Max = torch.tensor([0.66, 0.99, 1.33]),\
                angles=[torch.tensor(0)], k=3):
        super(R_layer, self).__init__()
        # self.constraint_sigma = constraint_sigma
        self.share_alpha = share_alpha
        self.init_k = k
        self.init_order = init_order
        self.init_scale = init_scale
        self.inC = inC
        self.Min = Min.cuda()
        self.Max = Max.cuda()

        self.n_scales  = n_scales
        self.learn_sigma = learn_sigma
        assert(outC % groups == 0)
        self.outC = outC
        self.groups = groups 
        self.angles=angles
        """ Define the number of basis based on order. """
        N = int((self.init_order + 1) * (self.init_order + 2) / 2)                        

        """ Create weight variables. """
        self.use_cuda = use_cuda
        # self.device = torch.device("cuda" if use_cuda else "cpu")
        if share_alpha:
            self.alphas = torch.nn.Parameter(torch.zeros([N, int(inC/groups), self.outC]),
                                             requires_grad=True) 
        else:
            self.alphas = torch.nn.Parameter(torch.zeros([self.n_scales, F, int(inC/groups), self.outC]), 
                                             requires_grad=True) 

        """ Define the scale parameter. """
        torch.nn.init.normal_(self.alphas, mean=0.0, std=1)
        # self.scales = torch.zeros([self.n_scales], requires_grad=True).cuda()
        # self.sigma = ((self.Max-self.Min)/2)*torch.tanh(self.scales)+((self.Min+self.Max)/2)                     

        if self.learn_sigma==True or self.learn_sigma=='free':    
            # self.sigma = torch.nn.Parameter(self.sigma, requires_grad=True)   
            self.scales = torch.nn.Parameter(torch.zeros([self.n_scales], dtype=torch.float32), requires_grad=True) 
            # torch.nn.init.normal_(self.scales, mean=0.0, std=0.1)
        else:
            self.scales = torch.nn.Parameter(torch.tensor(np.full((self.n_scales), self.init_scale),\
                                            dtype=torch.float32), requires_grad=False)      
                                            
        # self.sigma = torch.zeros((1,self.n_scales))  
        self.filtersize = torch.zeros((1,))                                     
        self.hermite = torch.Tensor()                                           
        self.x = torch.Tensor()                                                 
        self.filters = torch.Tensor()  

        # self.basis = []                                             
        # self.gauss = []   
    def export(self):
        if self.learn_sigma==True:
            self.sigma = ((self.Max-self.Min)/2)*torch.tanh(self.scales)+((self.Min+self.Max)/2)  
        elif self.learn_sigma=='free':
            self.sigma = 2.0**self.scales
        else:
            # self.sigma = (self.Max+self.Min)/2
            if self.n_scales==1:
                self.sigma=torch.tensor(self.init_scale).view(-1)         
            else:
                self.sigma=self.Max

        # print('max:',self.Max, 'min:',self.Min, 'scales:', self.sigma) 


        self.filtersize = torch.ceil(self.init_k*self.sigma)
        # print('max:',self.Max, 'min:',self.Min, 'sigma:',self.sigma, 'filter size:', self.filtersize*2+1)
        

        filter_list = []
        
        """ Define the grid on which the filter is created. """
        for i in range(self.n_scales):
            # try:
            x = torch.arange(start=-self.filtersize[i].detach().cpu().float(), \
                    end=self.filtersize[i].detach().cpu().float()+1, step=1)
            y = torch.arange(start=-self.filtersize[i].detach().cpu().float(), \
                    end=self.filtersize[i].detach().cpu().float()+1, step=1)
            # except: 
            #     print("Sigma value is off:", self.sigma, "filter size:", self.filtersize)


            """ Create the Gaussian derivative filters. """
            if self.share_alpha:
                filters, basis = gaussian_basis_filters(x=x, y=y, order=self.init_order, sigma=self.sigma[i], 
                            alphas=self.alphas, use_cuda=self.use_cuda, angles=self.angles)
            else:
                filters, basis = gaussian_basis_filters(x=x_theta, y=y_theta, order=self.init_order, sigma=self.sigma[i], 
                            alphas=self.alphas[i], use_cuda=self.use_cuda, angles=self.angles)
#             print('filters:',filters.shape)
            # kernel in shape [num_rotations, 1, out_channels, in_channels, H, W]
            filter_list.append(filters)
            # self.basis.append(basis)

        if len(torch.unique(self.filtersize)) == 1:
            self.filters = torch.cat(filter_list,dim=1)
        else:
            # print('filter size:', torch.unique(self.filtersize))
            max_size = self.filtersize.max()
            for i in range(len(filter_list)):
                pad_size = max_size*2+1-filter_list[i].shape[-1]
                pad_size = int(pad_size.cpu().item()/2)
                filter_list[i] = F.pad(filter_list[i],(pad_size, pad_size, pad_size, pad_size),"constant", 0)
            self.filters = torch.cat(filter_list,dim=1)
            # kernel in shape [num_rotations, num_scales, out_channels, in_channels, H, W]
        self.filters = self.filters.permute(2,0,1,3,4,5).contiguous()
#         print('-'*10, 'filter shape:', self.filters.shape)
        # kernel in shape [out_channels, num_rotations, num_scales, in_channels, H, W]
        self.filters = self.filters.view(-1, self.inC, self.filters.shape[-2], self.filters.shape[-1])
        return self.filters

    """ Forward pass with inputs: creates the filters and performs the convolution. """
    def forward(self, data):
        if self.learn_sigma==True:
            self.sigma = ((self.Max-self.Min)/2)*torch.tanh(self.scales)+((self.Min+self.Max)/2)  
        elif self.learn_sigma=='free':
            self.sigma = 2.0**self.scales
        else:
            # self.sigma = (self.Max+self.Min)/2
            if self.n_scales==1:
                self.sigma=torch.tensor(self.init_scale).view(-1)         
            else:
                self.sigma=self.Max

        # print('max:',self.Max, 'min:',self.Min, 'scales:', self.sigma) 


        self.filtersize = torch.ceil(self.init_k*self.sigma)
        # print('max:',self.Max, 'min:',self.Min, 'sigma:',self.sigma, 'filter size:', self.filtersize*2+1)
        

        filter_list = []
        
        """ Define the grid on which the filter is created. """
        for i in range(self.n_scales):
            # try:
            x = torch.arange(start=-self.filtersize[i].detach().cpu().float(), \
                    end=self.filtersize[i].detach().cpu().float()+1, step=1)
            y = torch.arange(start=-self.filtersize[i].detach().cpu().float(), \
                    end=self.filtersize[i].detach().cpu().float()+1, step=1)
            # except: 
            #     print("Sigma value is off:", self.sigma, "filter size:", self.filtersize)


            """ Create the Gaussian derivative filters. """
            if self.share_alpha:
                filters, basis = gaussian_basis_filters(x=x, y=y, order=self.init_order, sigma=self.sigma[i], 
                            alphas=self.alphas, use_cuda=self.use_cuda, angles=self.angles)
            else:
                filters, basis = gaussian_basis_filters(x=x_theta, y=y_theta, order=self.init_order, sigma=self.sigma[i], 
                            alphas=self.alphas[i], use_cuda=self.use_cuda, angles=self.angles)
#             print('filters:',filters.shape)
            # kernel in shape [num_rotations, 1, out_channels, in_channels, H, W]
            filter_list.append(filters)
            # self.basis.append(basis)

        if len(torch.unique(self.filtersize)) == 1:
            self.filters = torch.cat(filter_list,dim=1)
        else:
            # print('filter size:', torch.unique(self.filtersize))
            max_size = self.filtersize.max()
            for i in range(len(filter_list)):
                pad_size = max_size*2+1-filter_list[i].shape[-1]
                pad_size = int(pad_size.cpu().item()/2)
                filter_list[i] = F.pad(filter_list[i],(pad_size, pad_size, pad_size, pad_size),"constant", 0)
            self.filters = torch.cat(filter_list,dim=1)
            # kernel in shape [num_rotations, num_scales, out_channels, in_channels, H, W]
        self.filters = self.filters.permute(2,0,1,3,4,5).contiguous()
#         print('-'*10, 'filter shape:', self.filters.shape)
        # kernel in shape [out_channels, num_rotations, num_scales, in_channels, H, W]
        self.filters = self.filters.view(-1, self.inC, self.filters.shape[-2], self.filters.shape[-1])
#         print('filters---:',self.filters.shape)

        """ Perform the convolution. """
        final_conv = F.conv2d(input=data, # NCHW
                              weight=self.filters, # KCHW
                              bias=None, stride=1, padding=int(self.filters.shape[2]/2))
        B,C,H,W = final_conv.shape
        final_conv = final_conv.view(B, self.outC, len(self.angles)*self.n_scales, final_conv.shape[-2],final_conv.shape[-1]).squeeze(3)
        return final_conv

class Rh_layer(nn.Module):
    def __init__(self, inC, outC, init_k, init_order, init_scale, learn_sigma, use_cuda, groups=1, n_scales=5,
                share_alpha=False, Min = torch.tensor([0.33, 0.66, 0.99]), Max = torch.tensor([0.66, 0.99, 1.33]),\
                angles=[torch.tensor(0)], rotation_size=1, scale_size=1, k=3):
        super(Rh_layer, self).__init__()
        # self.constraint_sigma = constraint_sigma
        self.rotation_size = rotation_size
        self.scale_size = scale_size
        self.share_alpha = share_alpha
        self.init_k = k
        self.init_order = init_order
        self.init_scale = init_scale
        self.inC = inC
        self.Min = Min.cuda()
        self.Max = Max.cuda()

        self.n_scales  = n_scales
        self.learn_sigma = learn_sigma
        assert(outC % groups == 0)
        self.outC = outC
        self.groups = groups 
        self.angles=angles
        self.stride=1
        """ Define the number of basis based on order. """
        N = int((self.init_order + 1) * (self.init_order + 2) / 2)                        

        """ Create weight variables. """
        self.use_cuda = use_cuda
        # self.device = torch.device("cuda" if use_cuda else "cpu")
        if share_alpha:
            self.alphas = torch.nn.Parameter(torch.zeros([N, int(inC/groups), self.outC]),
                                             requires_grad=True) 
        else:
            self.alphas = torch.nn.Parameter(torch.zeros([self.n_scales, F, int(inC/groups), self.outC]), 
                                             requires_grad=True) 

        """ Define the scale parameter. """
        torch.nn.init.normal_(self.alphas, mean=0.0, std=1)
        # self.scales = torch.zeros([self.n_scales], requires_grad=True).cuda()
        # self.sigma = ((self.Max-self.Min)/2)*torch.tanh(self.scales)+((self.Min+self.Max)/2)                     

        if self.learn_sigma==True or self.learn_sigma=='free':    
            # self.sigma = torch.nn.Parameter(self.sigma, requires_grad=True)   
            self.scales = torch.nn.Parameter(torch.zeros([self.n_scales], dtype=torch.float32), requires_grad=True) 
            # torch.nn.init.normal_(self.scales, mean=0.0, std=0.1)
        else:
            self.scales = torch.nn.Parameter(torch.tensor(np.full((self.n_scales), self.init_scale),\
                                            dtype=torch.float32), requires_grad=False)      
                                            
        # self.sigma = torch.zeros((1,self.n_scales))  
        self.filtersize = torch.zeros((1,))                                     
        self.hermite = torch.Tensor()                                           
        self.x = torch.Tensor()                                                 
        self.filters = torch.Tensor()  

        # self.basis = []                                             
        # self.gauss = []   

    def export(self):
        if self.learn_sigma==True:
            self.sigma = ((self.Max-self.Min)/2)*torch.tanh(self.scales)+((self.Min+self.Max)/2)  
        elif self.learn_sigma=='free':
            self.sigma = 2.0**self.scales
        else:
            # self.sigma = (self.Max+self.Min)/2
            if self.n_scales==1:
                self.sigma=torch.tensor(self.init_scale).view(-1)         
            else:
                self.sigma=self.Max

        # print('max:',self.Max, 'min:',self.Min, 'scales:', self.sigma) 

        self.filtersize = torch.ceil(self.init_k*self.sigma)
        # print('max:',self.Max, 'min:',self.Min, 'sigma:',self.sigma, 'filter size:', self.filtersize*2+1)


        filter_list = []
        
        """ Define the grid on which the filter is created. """
        for i in range(self.n_scales):
            # try:
            x = torch.arange(start=-self.filtersize[i].detach().cpu().float(), \
                    end=self.filtersize[i].detach().cpu().float()+1, step=1)
            y = torch.arange(start=-self.filtersize[i].detach().cpu().float(), \
                    end=self.filtersize[i].detach().cpu().float()+1, step=1)
            # except: 
            #     print("Sigma value is off:", self.sigma, "filter size:", self.filtersize)


            """ Create the Gaussian derivative filters. """
            if self.share_alpha:
                filters, basis = gaussian_basis_filters(x=x, y=y, order=self.init_order, sigma=self.sigma[i], 
                            alphas=self.alphas, use_cuda=self.use_cuda, angles=self.angles)
            else:
                filters, basis = gaussian_basis_filters(x=x_theta, y=y_theta, order=self.init_order, sigma=self.sigma[i], 
                            alphas=self.alphas[i], use_cuda=self.use_cuda, angles=self.angles)
#             print('filters:',filters.shape)
            # kernel in shape [num_rotations, 1, out_channels, in_channels, H, W]
            filter_list.append(filters)
            # self.basis.append(basis)

        if len(torch.unique(self.filtersize)) == 1:
            self.filters = torch.cat(filter_list,dim=1)
        else:
            # print('filter size:', torch.unique(self.filtersize))
            max_size = self.filtersize.max()
            for i in range(len(filter_list)):
                pad_size = max_size*2+1-filter_list[i].shape[-1]
                pad_size = int(pad_size.cpu().item()/2)
                filter_list[i] = F.pad(filter_list[i],(pad_size, pad_size, pad_size, pad_size),"constant", 0)
            self.filters = torch.cat(filter_list,dim=1)
            # kernel in shape [num_rotations, num_scales, out_channels, in_channels, H, W]
        self.filters = self.filters.permute(2,3,0,1,4,5).contiguous()
        # kernel in shape [out_channels, in_channels, num_rotations, num_scale, H, W]
        self.filters = self.filters.view(self.outC, self.inC, self.rotation_size * self.scale_size, 
                                        len(self.angles)*self.n_scales, self.filters.shape[-2], self.filters.shape[-1])
        return self.filters

    """ Forward pass with inputs: creates the filters and performs the convolution. """
    def forward(self, data): 
        if self.learn_sigma==True:
            self.sigma = ((self.Max-self.Min)/2)*torch.tanh(self.scales)+((self.Min+self.Max)/2)  
        elif self.learn_sigma=='free':
            self.sigma = 2.0**self.scales
        else:
            # self.sigma = (self.Max+self.Min)/2
            if self.n_scales==1:
                self.sigma=torch.tensor(self.init_scale).view(-1)         
            else:
                self.sigma=self.Max

        # print('max:',self.Max, 'min:',self.Min, 'scales:', self.sigma) 

        self.filtersize = torch.ceil(self.init_k*self.sigma)
        # print('max:',self.Max, 'min:',self.Min, 'sigma:',self.sigma, 'filter size:', self.filtersize*2+1)


        filter_list = []
        
        """ Define the grid on which the filter is created. """
        for i in range(self.n_scales):
            # try:
            x = torch.arange(start=-self.filtersize[i].detach().cpu().float(), \
                    end=self.filtersize[i].detach().cpu().float()+1, step=1)
            y = torch.arange(start=-self.filtersize[i].detach().cpu().float(), \
                    end=self.filtersize[i].detach().cpu().float()+1, step=1)
            # except: 
            #     print("Sigma value is off:", self.sigma, "filter size:", self.filtersize)


            """ Create the Gaussian derivative filters. """
            if self.share_alpha:
                filters, basis = gaussian_basis_filters(x=x, y=y, order=self.init_order, sigma=self.sigma[i], 
                            alphas=self.alphas, use_cuda=self.use_cuda, angles=self.angles)
            else:
                filters, basis = gaussian_basis_filters(x=x_theta, y=y_theta, order=self.init_order, sigma=self.sigma[i], 
                            alphas=self.alphas[i], use_cuda=self.use_cuda, angles=self.angles)
#             print('filters:',filters.shape)
            # kernel in shape [num_rotations, 1, out_channels, in_channels, H, W]
            filter_list.append(filters)
            # self.basis.append(basis)

        if len(torch.unique(self.filtersize)) == 1:
            self.filters = torch.cat(filter_list,dim=1)
        else:
            # print('filter size:', torch.unique(self.filtersize))
            max_size = self.filtersize.max()
            for i in range(len(filter_list)):
                pad_size = max_size*2+1-filter_list[i].shape[-1]
                pad_size = int(pad_size.cpu().item()/2)
                filter_list[i] = F.pad(filter_list[i],(pad_size, pad_size, pad_size, pad_size),"constant", 0)
            self.filters = torch.cat(filter_list,dim=1)
            # kernel in shape [num_rotations, num_scales, out_channels, in_channels, H, W]
        self.filters = self.filters.permute(2,3,0,1,4,5).contiguous()
        # kernel in shape [out_channels, in_channels, num_rotations, num_scale, H, W]
        self.filters = self.filters.view(self.outC, self.inC, self.rotation_size * self.scale_size, 
                                        len(self.angles)*self.n_scales, self.filters.shape[-2], self.filters.shape[-1])
        self.filters = self.filters.permute(3, 0, 1, 2, 4, 5).contiguous()
        self.filters = self.filters.view(-1, self.inC, self.rotation_size, self.scale_size,
                             self.filters.shape[-2], self.filters.shape[-1])

        B, C, S, H, W = data.shape
        # expand x into shape [batchsize x in_channels, num_rotations, num_scales, H x W], indexed by [batch x lambda', thata, alpha, u1 x u2]
        data = data.view(B, C, len(self.angles) + self.rotation_size - 1, self.n_scales + self.scale_size - 1, H, W)
            
        output = 0.0
        # to be complete
        for i in range(self.rotation_size):
            for j in range(self.scale_size):
                # print("rotation difference")
                # print(x[:, :, i, j:j + self.num_scales]-x[:, :, i+1, j:j + self.num_scales])
                data_ = data[:, :, i:i + len(self.angles), j:j + self.n_scales]
                # expand X
                B, C, R, S, H, W = data_.shape
                data_ = data_.permute(0, 2, 3, 1, 4, 5).contiguous()
                data_ = data_.view(B, -1, H, W)
                output += F.conv2d(data_, self.filters[:, :, i, j], padding = int(self.filters.shape[-1]/2),
                                   groups=R*S, stride=self.stride)

        # squeeze output
        B, C_, H_, W_ = output.shape
        output = output.view(B, R*S, -1, H_, W_)
        output = output.permute(0, 2, 1, 3, 4).contiguous()
        
        return output

def measure_error(f_1, f_2):
    '''
    args:
        f_1: phi(f), Dictionary of Dictionary
        f_2: phi(Ls[f]), Dictionary of Dictionary
    '''
    num_datapoints = f_1.shape[0]
    if f_1.shape[-1]>f_2.shape[-1]:
        pass
    else:
        f_3 = f_1
        f_1 = f_2
        f_2 = f_3
    err_mat = torch.empty(0,1)#.cuda()
    ratio = f_2.shape[-1]/f_1.shape[-1]
    for i in range(f_2.shape[0]):
        for j in range(f_1.shape[0]):
            temp =F.interpolate(f_1[j],size=(f_2[i].shape[2],f_2[i].shape[2]))
            err = torch.norm(f_2[i]-ratio**2*F.interpolate(f_1[j],size=(f_2[i].shape[2],f_2[i].shape[2]), mode='bilinear', align_corners=True), p=2, dim=(0,1,2,3))/\
                            torch.norm(F.interpolate(f_1[j],size=(f_2[i].shape[2],f_2[i].shape[2]), mode='bilinear', align_corners=True), p=2,dim=(0,1,2,3))
            # print('err:',err, err.size())
            err_mat = torch.cat([err_mat, err.view(1,1)], dim=0)
    err_mat=err_mat.view(f_1.shape[0],f_1.shape[0])
    # print(err_mat)
    return err_mat

if __name__ == '__main__':
    torch.manual_seed(34)
    in_ch =3
    out_ch=5
    n_s = 5
    n_r = 4
    order = 2
    num_roto_90 = 1
    

    # layer= RSTConv2d_lift(in_ch, out_ch, 0.2, 4, stride=1, n_scales=n_s, n_roto=n_r).cuda()

    # layer = Srf_layer(inC=in_ch, outC=out_ch, init_k=2, init_order=1, init_scale=0.5, learn_sigma=False, 
    #                   use_cuda=True, share_alpha=True, Min=0, Max=2.5).cuda()

    angles_1 = [torch.tensor(0+i*math.pi/2) for i in range(4)]
    # angles_1 = [torch.tensor(math.pi/4+i*math.pi/2) for i in range(4)]

    layer = Srf_layer(inC=in_ch, outC=out_ch, init_k=2, init_order=order, init_scale=0.5, learn_sigma=False, n_scales=5,
                  use_cuda=False, share_alpha=True, Min=0, Max=2.5, angles=angles_1)
    
    
     # for srf_layer
    filters, _, sigma = layer.forward_no_input()
    i = 1
    print('filter shape:',filters.shape)

    for f in filters:
        f = f[0].detach().cpu().numpy()
        plt.imshow(f)
        plt.savefig(f'figs/{i}.png',bbox_inches='tight',dpi=300,pad_inches=0.0,set_visiable = False)
        i+=1
    
    # for rst layer
    # filters,sigma = layer.forward_no_input()
    # filters = filters.detach().cpu().numpy()
    # sigma = np.around(sigma,2)
    # print('filter shape:',filters.shape)
    # for i in range(n_s):
    #     for j in range(n_r):
    #         f = filters[0,j,i,0]
    #         plt.imshow(f)
    #         plt.savefig(f'figs/{i}_{j}.png',bbox_inches='tight',dpi=300,pad_inches=0.0,set_visiable = False)


    # plt.savefig('figs/filters.png',bbox_inches='tight',dpi=300,pad_inches=0.0,set_visiable = False)
        # print(f[0].detach().cpu().numpy())
        # temp = cv2.resize(f[0].detach().cpu().numpy(),(110,110),interpolation = cv2.INTER_NEAREST)*255
        # temp = temp.astype(np.uint8)
        # temp = cv2.applyColorMap(temp, cv2.COLORMAP_SUMMER)
        # cv2.imwrite(f'figs/{i}.png', temp)
        # i+=1


    layer.eval()

    r = 2**0.25

    stacked_err = []
    # scales = [round(0.25*r**i,2) for i in range(0,8)]+[round(0.25*r**i,2) for i in range(9,17)]
    scales = [0.5]

    for s in scales:
        factor_1 = s
        factor_2 = 1

        test_dataset_1  = Kumar(image_set='test', factor=factor_1)
        test_dataset_2  = Kumar(image_set='test', factor=factor_2)
        
        val_loader_1 = DataLoader(test_dataset_1, batch_size=1, shuffle=False, num_workers=2, pin_memory=True)
        val_loader_2 = DataLoader(test_dataset_2, batch_size=1, shuffle=False, num_workers=2, pin_memory=True)

        err_all = 0
        i=0
        for batch_1, batch_2 in zip(val_loader_1, val_loader_2):
            with torch.no_grad():
                imgs_1 = batch_1['image']#.cuda() #to(device=device, dtype=torch.float32))
                imgs_2 = batch_2['image']#.cuda() #to(device=device, dtype=torch.float32))

                imgs_2 =torch.rot90(imgs_2, num_roto_90, (2,3))
                out_1  = layer(imgs_1)
                out_2  = layer(imgs_2)
                # break
                # print(out_1.shape, out_2.shape)
                out_2=out_2.squeeze()
                out_2=torch.rot90(out_2, -num_roto_90, (1, 2))
                out_1=out_1.squeeze()*s**2
    
                # for srf layer
                # out_1=out_1.view(5,1,out_1.shape[1], out_1.shape[2]).unsqueeze(dim=1)
                # out_2=out_2.view(5,1,out_2.shape[1], out_2.shape[2]).unsqueeze(dim=1)

                # for rts layer
                out_1=out_1.view(-1,out_1.shape[-1], out_1.shape[-1]).unsqueeze(dim=1).unsqueeze(dim=1)
                out_2=out_2.view(-1,out_2.shape[-1], out_2.shape[-1]).unsqueeze(dim=1).unsqueeze(dim=1)

                # print(out_1.shape, out_2.shape)
                err_all += measure_error(out_1, out_2)
                # print(err_all.shape)
                # for k in [0,1,2,3,4]:
                #     o_1 = (out_1[k,0,0].detach().cpu().numpy()*255).astype(np.uint8)
                #     o_1 = cv2.applyColorMap(o_1, cv2.COLORMAP_JET)
                #     o_2 = (out_2[k,0,0].detach().cpu().numpy()*255).astype(np.uint8)
                #     o_2 = cv2.applyColorMap(o_2, cv2.COLORMAP_JET)
                #     cv2.imwrite(f"figs/{str(factor_1)}_{str(k)}_{batch_1['name'][0]}",o_1)
                #     cv2.imwrite(f"figs/{str(factor_2)}_{str(k)}_{batch_2['name'][0]}",o_2)

                # break

                i+=imgs_2.shape[0]
        # print(f'factor: {factor_1} vs. {factor_2}:')
        err_all = (err_all/i).cpu().detach().numpy()
        # if s>1:
        #     err_all = err_all.transpose()
        # print(f'scale={s}')
        # fig, ax = plt.subplots(dpi=400)
        # plt.imshow(err_all)
        # for i in range(err_all.shape[0]):
        #     for j in range(err_all.shape[1]):
        #         plt.text(j,i,"%00.2f" %(err_all[i,j]), color='white', fontsize=5, va='center', ha='center')

        # idx = np.argmin(err_all,axis=1)
        # # print('idx:',idx)
        # for i in range(err_all.shape[-1]):
        #     ax.add_patch(Rectangle((idx[i]-0.5,i%20-0.5), 1,1,
        #                  edgecolor = 'red',
        #                  fill=False,
        #                  lw=1))

        # idx = [i for i in range(4)]
        # idy = [(i+num_roto_90)%4 for i in range(4)]
        # coord = zip(idx,idy)

        # # print('idx:',idx, 'idy:',idy)
        # for i in range(4):
            
        #     temp = err_all[idx[i]*5:(idx[i]+1)*5,idy[i]*5:(idy[i]+1)*5,]
        #     # print(temp.shape)
        #     r, c = np.where(temp == np.min(temp))
        #     # print('row:',r,'col:',c)
        #     ax.add_patch(Rectangle((idy[i]*5+c-0.5,idx[i]*5+r-0.5), 1,1,
        #                  edgecolor = 'blue',
        # #                  facecolor = 'blue',
        #                  fill=False,
        #                  lw=1))
            
        #     ax.add_patch(Rectangle((idy[i]*5-0.5,idx[i]*5-0.5), 5,5,
        #                  edgecolor = 'pink',
        #                  fill=False,
        #                  lw=1))

        # # xlocations = np.array([i for i in range(n_r*n_s)])
        # xlocations = sigma.tolist()+sigma.tolist()+sigma.tolist()+sigma.tolist()
        # xlocations = [np.round(x,2) for x in xlocations]
        # plt.xticks([i for i in range(n_r*n_s)], xlocations,fontsize=6)
        # plt.yticks([i for i in range(n_r*n_s)], xlocations,fontsize=6)
        # plt.title(f'scale factor: {s}')

        # plt.savefig(f'figs/scale={s}.png',bbox_inches='tight',dpi=300,pad_inches=0.0,set_visiable = False)

        plot_err_mat(err_all, sigma, s, num_roto_90, angles_1[0], order)
        # print(err_all.shape)
    #     stacked_err.append(err_all)
    # stacked_err = torch.cat(stacked_err,dim=0)
    # print(stacked_err.shape)
    # print('all:',stacked_err)



