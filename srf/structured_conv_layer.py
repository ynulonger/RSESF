# Import general dependencies
import numpy as np
import math
import torch
from torch.autograd import Variable
import torch.nn as nn
from torchvision import transforms
from torch.autograd import Function
from torch.distributions import normal
from srf.gaussian_basis_filters import *
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

'''
class Srf_layer(nn.Module):
    def __init__(self,
                inC,
                outC, 
                init_k,
                init_order,
                init_scale,
                learn_sigma, 
                use_cuda,
                groups=1,
                n_scales=5,
                share_alpha=False,
                Min = 0,
                Max = 0.5
                ):
        super(Srf_layer, self).__init__()
        # self.constraint_sigma = constraint_sigma
        self.share_alpha = share_alpha
        self.init_k = init_k
        self.init_order = init_order
        self.init_scale = init_scale
        self.inC = inC
        self.Min = torch.arange(Min,Max,0.5).cuda()
        self.Max = torch.arange(Min+0.5,Max+0.5,0.5).cuda()
        self.n_scales  = n_scales
        self.learn_sigma = learn_sigma
        assert(outC % groups == 0)
        self.outC = outC
        self.groups = groups 
        """ Define the number of basis based on order. """
        N = int((self.init_order + 1) * (self.init_order + 2) / 2)                        

        """ Create weight variables. """
        self.use_cuda = use_cuda
        # self.device = torch.device("cuda" if use_cuda else "cpu")
        if share_alpha:
            self.alphas = torch.nn.Parameter(torch.zeros([N, int(inC/groups), outC//self.n_scales]),
                                             requires_grad=True) 
        else:
            self.alphas = torch.nn.Parameter(torch.zeros([self.n_scales, F, int(inC/groups), outC//self.n_scales]), 
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
  
    """ Forward pass without inputs to return the filters only. """
    def forward_no_input(self):
        """ Define sigma from the scale: sigma = 2^scale """
        if self.learn_sigma==True:
            self.sigma = ((self.Max-self.Min)/2)*torch.tanh(self.scales)+((self.Min+self.Max)/2)  
        elif self.learn_sigma=='free':
            self.sigma = 2.0**self.scales
        else:
            # self.sigma = (self.Max+self.Min)/2
            self.sigma=self.Max
        self.filtersize = torch.ceil(2*self.sigma)
        filter_list = []
        
        """ Define the grid on which the filter is created. """
        for i in range(self.n_scales):
            # try:
            x = torch.arange(start=-self.filtersize[i].detach().cpu().float(), \
                    end=self.filtersize[i].detach().cpu().float()+1, step=1)
            hermite = torch.arange(start=-self.filtersize[i].detach().cpu().float(), \
                    end=self.filtersize[i].detach().cpu().float()+1, step=1)
            # except: 
            #     print("Sigma value is off:", self.sigma, "filter size:", self.filtersize)


            """ Create the Gaussian derivative filters. """
            if self.share_alpha:
                filters= gaussian_basis_filters(x=x, hermite=hermite, order=self.init_order, sigma=self.sigma[i], 
                                            alphas=self.alphas, use_cuda=self.use_cuda)
            else:
                filters= gaussian_basis_filters(x=x, hermite=hermite, order=self.init_order, sigma=self.sigma[i], 
                            alphas=self.alphas[i], use_cuda=self.use_cuda)
            # print(filters.shape)
            filter_list.append(filters)
            # self.basis.append(basis)

        if len(torch.unique(self.filtersize)) == 1:
            self.filters = torch.vstack(filter_list)
        else:
            # print('filter size:', torch.unique(self.filtersize))
            max_size = self.filtersize.max()
            for i in range(len(filter_list)):
                # print(filter_list[i].shape)
                pad_size = max_size*2+1-filter_list[i].shape[-1]
                pad_size = int(pad_size.cpu().item()/2)
                # print('pad_size:', pad_size)
                filter_list[i] = F.pad(filter_list[i],(pad_size, pad_size, pad_size, pad_size),"constant", 0)
            self.filters = torch.vstack(filter_list)

        self.filters = torch.vstack([torch.rot90(self.filters, i, (2,3)) for i in range(4)])
        return self.filters, self.sigma.detach().cpu().numpy()


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
            # self.sigma = (self.Max+self.Min)/2
            self.sigma=self.Max

        # print('sigma:',self.sigma)
        # self.filtersize = 2*torch.ceil(self.init_k*self.sigma)
        self.filtersize = torch.ceil(2*self.sigma)

        filter_list = []
        """ Define the grid on which the filter is created. """
        for i in range(self.n_scales):
            try:
                x = torch.arange(start=-self.filtersize[i].detach().cpu().float(), \
                        end=self.filtersize[i].detach().cpu().float()+1, step=1)
                hermite = torch.arange(start=-self.filtersize[i].detach().cpu().float(), \
                        end=self.filtersize[i].detach().cpu().float()+1, step=1)
            except: 
                print("Sigma value is off:", self.sigma, "filter size:", self.filtersize)

            """ Create the Gaussian derivative filters. """
            if self.share_alpha:
                filters= gaussian_basis_filters(x=x, hermite=hermite, order=self.init_order, sigma=self.sigma[i], 
                                            alphas=self.alphas, use_cuda=self.use_cuda)
            else:
                filters= gaussian_basis_filters(x=x, hermite=hermite, order=self.init_order, sigma=self.sigma[i], 
                            alphas=self.alphas[i], use_cuda=self.use_cuda)
            # print('---------------',type(filters))
            filter_list.append(filters)
            # self.basis.append(basis)

        if len(torch.unique(self.filtersize)) == 1:
            self.filters = torch.vstack(filter_list)
        else:
            # print('filter size:', torch.unique(self.filtersize))
            max_size = self.filtersize.max()
            for i in range(len(filter_list)):
                # print(filter_list[i].shape)
                pad_size = max_size*2+1-filter_list[i].shape[-1]
                pad_size = int(pad_size.cpu().item()/2)
                # print('pad_size:', pad_size)
                filter_list[i] = F.pad(filter_list[i],(pad_size, pad_size, pad_size, pad_size),"constant", 0)
            self.filters = torch.vstack(filter_list)
        
        self.filters = torch.vstack([torch.rot90(self.filters, i, (2,3)) for i in range(4)])
        """ Perform the convolution. """
        final_conv = F.conv2d(input=data, # NCHW
                              weight=self.filters, # KCHW
                              bias=None, stride=1, padding=int(self.filters.shape[2]/2))
    
        return final_conv

    """ List the parameters. """
    def num_params(self):
        return (sum(p.numel() for p in self.parameters() if p.requires_grad))
'''
class Srf_layer(nn.Module):
    def __init__(self, inC, outC, init_k, init_order, init_scale, learn_sigma, use_cuda, groups=1, n_scales=5,
                share_alpha=False,  Min = 0, Max = 0.5, angles=[torch.tensor(0)]):
        super(Srf_layer, self).__init__()
        # self.constraint_sigma = constraint_sigma
        self.share_alpha = share_alpha
        self.init_k = init_k
        self.init_order = init_order
        self.init_scale = init_scale
        self.inC = inC
        self.Min = torch.arange(Min, Max,(Max-Min)/n_scales).cuda()
        self.Max = torch.arange(Min+(Max-Min)/n_scales, Max+(Max-Min)/n_scales,(Max-Min)/n_scales).cuda()
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
            self.alphas = torch.nn.Parameter(torch.zeros([N, int(inC/groups), outC//self.n_scales]),
                                             requires_grad=True) 
        else:
            self.alphas = torch.nn.Parameter(torch.zeros([self.n_scales, F, int(inC/groups), outC//self.n_scales]), 
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
  
    """ Forward pass without inputs to return the filters only. """
    def forward_no_input(self):
        """ Define sigma from the scale: sigma = 2^scale """
        if self.learn_sigma==True:
            self.sigma = ((self.Max-self.Min)/2)*torch.tanh(self.scales)+((self.Min+self.Max)/2)  
        elif self.learn_sigma=='free':
            self.sigma = 2.0**self.scales
        else:
            # self.sigma = (self.Max+self.Min)/2
            self.sigma=self.Max
            
        print('sigma:',self.sigma)
        self.filtersize = torch.ceil(3*self.sigma)
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
        # kernel in shape [out_channels, num_rotations, num_scales, in_channels, H, W]
        self.filters = self.filters.view(-1, self.inC, self.filters.shape[-2], self.filters.shape[-1])
#         print('filters---:',self.filters.shape)
        
        return self.filters, basis, self.sigma.detach().cpu().numpy()


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
            # self.sigma = (self.Max+self.Min)/2
            self.sigma=self.Max

        # print('sigma:',self.sigma)
        # self.filtersize = 2*torch.ceil(self.init_k*self.sigma)
        self.filtersize = torch.ceil(3*self.sigma)

        filter_list = []
        
        """ Define the grid on which the filter is created. """
        for i in range(self.n_scales):
            # try:
            x = torch.arange(start=-self.filtersize[i].detach().cpu().float(), \
                    end=self.filtersize[i].detach().cpu().float()+1, step=1)
            y = torch.arange(start=-self.filtersize[i].detach().cpu().float(), \
                    end=self.filtersize[i].detach().cpu().float()+1, step=1).cuda()
            # except: 
            #     print("Sigma value is off:", self.sigma, "filter size:", self.filtersize)
            hermite = torch.arange(start=-self.filtersize[i].detach().cpu().float(), \
                    end=self.filtersize[i].detach().cpu().float()+1, step=1)

            """ Create the Gaussian derivative filters. """
            if self.share_alpha:
                # filters, basis = gaussian_basis_filters(x=x, y=y, order=self.init_order, sigma=self.sigma[i], 
                #             alphas=self.alphas, use_cuda=self.use_cuda, angles=self.angles)
                filters = gaussian_basis_filters(
                                                x=x, hermite=hermite, order=self.init_order, sigma=self.sigma[i], 
                                                alphas=self.alphas, use_cuda=self.use_cuda)
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
            # self.filters = torch.cat(filter_list,dim=1)
            self.filters = torch.vstack(filter_list)
            # kernel in shape [num_rotations, num_scales, out_channels, in_channels, H, W]
        # print('*'*10,self.filters.shape)
        # self.filters = self.filters.permute(2,0,1,3,4,5).contiguous()
        # kernel in shape [out_channels, num_rotations, num_scales, in_channels, H, W]
        self.filters = self.filters.view(-1, self.inC, self.filters.shape[-2], self.filters.shape[-1])
#         print('filters---:',self.filters.shape)

        """ Perform the convolution. """
        final_conv = F.conv2d(input=data, # NCHW
                              weight=self.filters, # KCHW
                              bias=None, stride=1, padding=int(self.filters.shape[2]/2))
    
        return final_conv

    """ List the parameters. """
    def num_params(self):
        return (sum(p.numel() for p in self.parameters() if p.requires_grad))

class Srf_layer_2(nn.Module):
    def __init__(self,
                inC,
                outC, 
                init_k,
                init_order,
                init_scale,
                learn_sigma, 
                use_cuda,
                n_scales=5,
                share_alpha=False,
                Min = 0,
                Max = 0.5
                ):
        super(Srf_layer_2, self).__init__()
        self.learn_sigma = learn_sigma
        self.init_k = init_k
        self.init_order = init_order
        self.init_scale = init_scale
        self.inC = inC
        self.n_scales  = n_scales
        self.share_alpha = share_alpha
        self.Min = torch.arange(Min, Max,(Max-Min)/n_scales).cuda()
        self.Max = torch.arange(Min+(Max-Min)/n_scales, Max+(Max-Min)/n_scales,(Max-Min)/n_scales).cuda()
        # assert(outC % groups == 0)
        self.outC = outC
 
        """ Define the number of basis based on order. """
        N = int((self.init_order + 1) * (self.init_order + 2) / 2)                        

        """ Create weight variables. """
        self.use_cuda = use_cuda
        self.device = torch.device("cuda" if use_cuda else "cpu")
        if share_alpha:
            self.alphas = torch.nn.Parameter(torch.zeros([N, inC//self.n_scales, outC//self.n_scales],\
                            device=self.device), requires_grad=True) 
        else:
            self.alphas = torch.nn.Parameter(torch.zeros([self.n_scales, F, inC//self.n_scales, outC//self.n_scales],\
                    device=self.device), requires_grad=True) 

        """ Define the scale parameter. """
        torch.nn.init.normal_(self.alphas, mean=0.0, std=1)
        # self.scales = torch.zeros([self.n_scales], requires_grad=True).cuda()
        # self.sigma = ((self.Max-self.Min)/2)*torch.tanh(self.scales)+((self.Min+self.Max)/2)                     

        if learn_sigma==True or self.learn_sigma=='free':         
            self.scales = torch.nn.Parameter(torch.zeros([self.n_scales],\
                            device=self.device, dtype=torch.float32), requires_grad=True)   
            # self.sigma = torch.nn.Parameter(self.sigma, requires_grad=True)   
            # torch.nn.init.normal_(self.scales, mean=0.0, std=0.1)
        else:
            self.scales = torch.nn.Parameter(torch.tensor(np.random.rand(self.n_scales),\
                            device=self.device, dtype=torch.float32), requires_grad=False)      
                                            
        # self.sigma = torch.zeros((1,self.n_scales))                                          
        self.filtersize = torch.zeros((1,))                                     
        self.hermite = torch.Tensor()                                           
        self.x = torch.Tensor()                                                 
        self.filters = torch.Tensor()  
        # self.basis = []                                             
        # self.gauss = [] 
  
    """ Forward pass without inputs to return the filters only. """
    def forward_no_input(self):
        """ Define sigma from the scale: sigma = 2^scale """
        self.sigma = 2.0**self.scales

        self.filtersize = torch.ceil(2*self.sigma)
        
        """ Define the grid on which the filter is created. """
        for i in range(self.n_scales):
            # try:
            x = torch.arange(start=-self.filtersize[i].detach().cpu().float(), \
                    end=self.filtersize[i].detach().cpu().float()+1, step=1)
            hermite = torch.arange(start=-self.filtersize[i].detach().cpu().float(), \
                    end=self.filtersize[i].detach().cpu().float()+1, step=1)
            # except: 
            #     print("Sigma value is off:", self.sigma, "filter size:", self.filtersize)


            """ Create the Gaussian derivative filters. """
            filters, = gaussian_basis_filters(x=x, hermite=hermite, order=self.init_order, sigma=self.sigma[i], 
                                              alphas=self.alphas[i], use_cuda=self.use_cuda)
            # print(filters.shape)
            self.filters.append(filters)
            # self.basis.append(basis)
        return self.filters


    """ Forward pass with inputs: creates the filters and performs the convolution. """
    def forward(self, data): 
        """ Define sigma from the scale: sigma = 2^scale """
        # self.sigma = 2.0**self.scales
        # self.filtersize = torch.ceil(self.init_k*self.sigma)
        if self.learn_sigma==True:
            self.sigma = ((self.Max-self.Min)/2)*torch.tanh(self.scales)+((self.Min+self.Max)/2)  
        elif self.learn_sigma=='free':
            self.sigma = 2.0**self.scales
        else:
            self.sigma = (self.Max+self.Min)/2
        # print('sigma:',self.sigma)

        # self.filtersize = 2*torch.ceil(self.init_k*self.sigma)
        self.filtersize = torch.ceil(2*self.sigma)
        
        filter_list = []
        """ Define the grid on which the filter is created. """
        for i in range(self.n_scales):
            try:
                x = torch.arange(start=-self.filtersize[i].detach().cpu().float(), \
                        end=self.filtersize[i].detach().cpu().float()+1, step=1).cuda()
                hermite = torch.arange(start=-self.filtersize[i].detach().cpu().float(), \
                        end=self.filtersize[i].detach().cpu().float()+1, step=1).cuda()
            except: 
                print("Sigma value is off:", self.sigma, "filter size:", self.filtersize)

            """ Create the Gaussian derivative filters. """
            if self.share_alpha:
                filters = gaussian_basis_filters(
                                                x=x, hermite=hermite, order=self.init_order, sigma=self.sigma[i], 
                                                alphas=self.alphas, use_cuda=self.use_cuda)
            else:
                filters = gaussian_basis_filters(
                                                x=x, hermite=hermite, order=self.init_order, sigma=self.sigma[i], 
                                                alphas=self.alphas[i], use_cuda=self.use_cuda)
                
            filter_list.append(filters)
            # self.basis.append(basis)

        if len(torch.unique(self.filtersize)) == 1:
            self.filters = torch.vstack(filter_list)
        else:
            max_size = self.filtersize.max()
            for i in range(len(filter_list)):
                # filter_list[i] = F.pad(filter_list[i].numpy(),[(max_size-filter_list[i].shape[-1])//2]*4)
                pad_size = (max_size*2+1-filter_list[i].shape[-1])
                pad_size = int(pad_size.cpu().item()/2)
                filter_list[i] = F.pad(filter_list[i],(pad_size, pad_size, pad_size, pad_size),"constant", 0)
            self.filters = torch.vstack(filter_list)
        

        """ Perform the convolution. """
        # print('---------------------', data.size(), self.filters.size())
        # print(f'sigma:{self.sigma}, alpha:{self.alphas.size() }')

        final_conv = F.conv2d(input=data, # NCHW
                              weight=self.filters, # KCHW
                              bias=None, stride=1, padding=int(self.filters.shape[2]/2),
                              groups=self.n_scales)
    
        return final_conv

def gabor_fn_lift(channel_in, channel_out, sigma, theta, Lambda, psi, gamma, max_size):
    '''
    sigma: standard deviation of Gaussian
    theta: angle [0, 2*pi]
    lambda: wavelength [1, max_size]
    psi: phase offset [-pi, pi]
    gamma: spatial aspect ratio (0,1]
    '''
    sigma_x = sigma
    sigma_y = sigma * gamma
    Lambda = Lambda * sigma
#     psi = psi * Lambda
#     print('sigma:',sigma, 'Lambda:', Lambda)
    xmax = max_size
    ymax = max_size
    xmin = -xmax
    ymin = -ymax
#     print('ymin:',ymin)
    ksize = xmax - xmin + 1
    ksize = int(ksize)
    y_0 = torch.arange(ymin, ymax+1).cuda()
    y = y_0.view(1, -1).repeat(channel_out, channel_in, ksize, 1).float()
    x_0 = torch.arange(xmin, xmax+1).cuda()
    x = x_0.view(-1, 1).repeat(channel_out, channel_in, 1, ksize).float()   # [channel_out, channelin, kernel, kernel]
    # Rotation
    x_theta = x * torch.cos(theta.view(-1, channel_in, 1, 1)) + y * torch.sin(theta.view(-1, channel_in, 1, 1))
    y_theta = -x * torch.sin(theta.view(-1, channel_in, 1, 1)) + y * torch.cos(theta.view(-1, channel_in, 1, 1))
    gb = torch.exp(-.5 * (x_theta**2 / sigma_x**2 + y_theta**2 / sigma_y.view(-1, channel_in, 1, 1)**2)) \
         * torch.cos(2 * math.pi / Lambda.view(-1, channel_in, 1, 1) * x_theta + psi.view(-1, channel_in, 1, 1))
    return gb

class GaborConv2d_lift(nn.Module):
    def __init__(self, channel_in, channel_out, Min_sigma, Max_sigma, stride=1, n_scales=5):
        super(GaborConv2d_lift, self).__init__()
        self.channel_in = channel_in
        self.channel_out = channel_out
        self.stride = stride
        offset = (Max_sigma-Min_sigma)/n_scales
        self.Min = torch.arange(Min_sigma, Max_sigma, offset).cuda()
        self.Max = torch.arange(Min_sigma+offset, Max_sigma+offset, offset).cuda()
        self.n_scales = n_scales
        self.L = nn.Parameter(torch.randn(channel_out//n_scales, channel_in), requires_grad=True)
        self.t = nn.Parameter(torch.randn(channel_out//n_scales, channel_in), requires_grad=True)
        self.psi = nn.Parameter(torch.randn(channel_out//n_scales, channel_in), requires_grad=True)
        self.scales = nn.Parameter(torch.randn(n_scales) * 1.0, requires_grad=True)
        self.g = nn.Parameter(torch.randn(channel_out//n_scales, channel_in), requires_grad=True)

    def forward(self, x):
        self.sigma = ((self.Max-self.Min)/2)*torch.tanh(self.scales)+((self.Min+self.Max)/2)  
        self.gamma = F.sigmoid(self.g)  
        self.size = (2.5*self.sigma.max()).ceil().item()
        self.PSI = 2*(F.sigmoid(self.psi)-0.5) * math.pi
        self.theta = F.sigmoid(self.t) * math.pi * 2
        self.Lambda = 1+(self.size-2)/self.sigma.max()*F.sigmoid(self.L)
        self.padding = int((self.size*2+1)/2)
        
        # print(self.sigma,self.gamma,self.PSI,self.theta,self.Lambda)
        k_list = []
        for i in range(self.n_scales):
            kernel = gabor_fn_lift(self.channel_in, self.channel_out//self.n_scales, self.sigma[i], self.theta, self.Lambda, self.psi, self.gamma, self.size)
            kernel = kernel.float()   # [channel_out//n_scales, channel_in, kernel, kernel]
            k_list.append(kernel)
        KERNEL = torch.cat(k_list,dim=0)
        # print(self.padding)
        out = F.conv2d(x, KERNEL, stride=self.stride, padding=self.padding)
        return out
    
    def forward_no_output(self):
        self.sigma = ((self.Max-self.Min)/2)*torch.tanh(self.scales)+((self.Min+self.Max)/2)  
        # print(self.sigma)
        self.gamma = F.sigmoid(self.g)  
        self.size = (2.*self.sigma.max()).ceil().item()
        self.PSI = 2*(F.sigmoid(self.psi)-0.5) * math.pi
        self.theta = F.sigmoid(self.t) * math.pi * 2
        self.Lambda = 1+(self.size-2)/self.sigma.max()*F.sigmoid(self.L)
        
        k_list = []
        for i in range(self.n_scales):
            kernel = gabor_fn_lift(self.channel_in, self.channel_out//self.n_scales, self.sigma[i], self.theta, self.Lambda, self.psi, self.gamma, self.size)
            kernel = kernel.float()   # [channel_out//n_scales, channel_in, kernel, kernel]
#             print(kernel.shape)
            k_list.append(kernel)
        KERNEL = torch.cat(k_list,dim=0)
        # print(KERNEL.shape)
        
        return KERNEL
    
class GaborConv2d(nn.Module):
    def __init__(self, channel_in, channel_out, Min_sigma, Max_sigma, stride=1, n_scales=5):
        super(GaborConv2d, self).__init__()
        self.channel_in = channel_in
        self.channel_out = channel_out
        self.stride = stride
        offset = (Max_sigma-Min_sigma)/n_scales
        self.Min = torch.arange(Min_sigma, Max_sigma, offset).cuda()
        self.Max = torch.arange(Min_sigma+offset, Max_sigma+offset, offset).cuda()
        self.n_scales = n_scales
        self.L = nn.Parameter(torch.randn(channel_out//n_scales, channel_in//n_scales), requires_grad=True)
        self.t = nn.Parameter(torch.randn(channel_out//n_scales, channel_in//n_scales), requires_grad=True)
        self.psi = nn.Parameter(torch.randn(channel_out//n_scales, channel_in//n_scales), requires_grad=True)
        self.scales = nn.Parameter(torch.randn(n_scales) * 1.0, requires_grad=True)
        self.g = nn.Parameter(torch.randn(channel_out//n_scales, channel_in//n_scales), requires_grad=True)

    def forward(self, x):
        self.sigma = ((self.Max-self.Min)/2)*torch.tanh(self.scales)+((self.Min+self.Max)/2)  
        self.gamma = F.sigmoid(self.g)  
        self.size = (2.5*self.sigma.max()).ceil().item()
        self.PSI = 2*(F.sigmoid(self.psi)-0.5) * math.pi
        self.theta = F.sigmoid(self.t) * math.pi * 2
        self.Lambda = 1+(self.size-2)/self.sigma.max()*F.sigmoid(self.L)
        self.padding = int((self.size*2+1)/2)
        
        k_list = []
        for i in range(self.n_scales):
            kernel = gabor_fn_lift(self.channel_in//self.n_scales, self.channel_out//self.n_scales, self.sigma[i], self.theta, self.Lambda, self.psi, self.gamma, self.size)
            kernel = kernel.float()   # [channel_out//n_scales, channel_in, kernel, kernel]
            k_list.append(kernel)
        KERNEL = torch.cat(k_list,dim=0)
        out = F.conv2d(x, KERNEL, stride=self.stride, groups=self.n_scales, padding=self.padding)
        return out
    
    def forward_no_output(self):
        self.sigma = ((self.Max-self.Min)/2)*torch.tanh(self.scales)+((self.Min+self.Max)/2)  
        # print(self.sigma)
        self.gamma = F.sigmoid(self.g)  
        self.size = (2.*self.sigma.max()).ceil().item()
        self.PSI = 2*(F.sigmoid(self.psi)-0.5) * math.pi
        self.theta = F.sigmoid(self.t) * math.pi * 2
        self.Lambda = 1+(self.size-2)/self.sigma.max()*F.sigmoid(self.L)
        
        k_list = []
        for i in range(self.n_scales):
            kernel = gabor_fn_lift(self.channel_in//self.n_scales, self.channel_out//self.n_scales, self.sigma[i], self.theta, self.Lambda, self.psi, self.gamma, self.size)
            kernel = kernel.float()   # [channel_out//n_scales, channel_in, kernel, kernel]
#             print(kernel.shape)
            k_list.append(kernel)
        KERNEL = torch.cat(k_list,dim=0)
        # print(KERNEL.shape)
        
        return KERNEL


""" Subsampling of the featuremaps based on the learned sigma. 
Input:
    - current: input featuremap
    - sigma: the learned sigma values
    - r: the hyperparameter controlling how fast the subsampling goes as a function of sigma.
"""
def safe_sample(current, sigma, r=4.0):        
    update_val = max(1.0, torch.div(2**sigma, r))
    shape = current.shape
    shape_out = max([1,1], [int(float(shape[2])/update_val), \
                            int(float(shape[3])/update_val)])
    current_out = F.interpolate(current, shape_out)
    return current_out

def RST_lift(channel_in, channel_out, n_r, sigma, theta, Lambda, psi, gamma, max_size):
    '''
    sigma: standard deviation of Gaussian
    theta: angle [0, 2*pi]
    lambda: wavelength [1, max_size]
    psi: phase offset [-pi, pi]
    gamma: spatial aspect ratio (0,1]
    '''
    sigma_x = sigma
    sigma_y = sigma * gamma
    Lambda = Lambda * sigma
#     psi = psi * Lambda
#     print('sigma:',sigma, 'Lambda:', Lambda)
    xmax = max_size
    ymax = max_size
    xmin = -xmax
    ymin = -ymax
#     print('ymin:',ymin)
    ksize = xmax - xmin + 1
    ksize = int(ksize)
    y_0 = torch.arange(ymin, ymax+1).cuda()
    y = y_0.view(1, -1).repeat(channel_out, channel_in, ksize, 1).float()
    x_0 = torch.arange(xmin, xmax+1).cuda()
    x = x_0.view(-1, 1).repeat(channel_out, channel_in, 1, ksize).float()   # [channel_out, channelin, kernel, kernel]
    # Rotation
#     print('theta:',theta.shape)
    thetas = [theta+i*math.pi/n_r for i in range(n_r)]
    kernels = []
    for theta in thetas:
        x_theta = x * torch.cos(theta.view(-1, channel_in, 1, 1)) + y * torch.sin(theta.view(-1, channel_in, 1, 1))
        y_theta = -x * torch.sin(theta.view(-1, channel_in, 1, 1)) + y * torch.cos(theta.view(-1, channel_in, 1, 1))
        gb = torch.exp(-.5 * (x_theta**2 / sigma_x**2 + y_theta**2 / sigma_y.view(-1, channel_in, 1, 1)**2)) \
             * torch.cos(2 * math.pi / Lambda.view(-1, channel_in, 1, 1) * x_theta + psi.view(-1, channel_in, 1, 1))
        gb = gb.unsqueeze(1)
#         print('gb:',gb.shape)
        kernels.append(gb)
    kernel = torch.cat(kernels, dim=1)
    return kernel

class RSTConv2d_lift(nn.Module):
    def __init__(self, channel_in, channel_out, Min_sigma, Max_sigma, stride=1, n_scales=5, n_roto=4):
        super(RSTConv2d_lift, self).__init__()
        self.channel_in = channel_in
        self.channel_out = channel_out//(n_scales*n_roto)
        self.stride = stride
        s_offset = (Max_sigma-Min_sigma)/n_scales
        self.Min = torch.arange(Min_sigma, Max_sigma, s_offset).cuda()
        self.Max = torch.arange(Min_sigma+s_offset, Max_sigma+s_offset, s_offset).cuda()
        self.n_scales = n_scales
        self.n_roto = n_roto
        self.L = nn.Parameter(torch.randn(self.channel_out, channel_in), requires_grad=True)
        self.t = nn.Parameter(torch.randn(self.channel_out, channel_in), requires_grad=True)
        self.psi = nn.Parameter(torch.randn(self.channel_out, channel_in), requires_grad=True)
        self.scales = nn.Parameter(torch.randn(n_scales) * 1.0, requires_grad=True)
        self.g = nn.Parameter(torch.randn(self.channel_out, channel_in), requires_grad=True)

    def forward(self, x):
        self.padding = int((self.size*2+1)/2)
        # self.sigma = ((self.Max-self.Min)/2)*torch.tanh(self.scales)+((self.Min+self.Max)/2) 
        self.sigma = ((self.Max-self.Min)/2)+((self.Min+self.Max)/2)  

        # print(self.sigma.shape, self.sigma)
        self.gamma = F.sigmoid(self.g)  
        self.size = int((2.*self.sigma.max()).ceil().item())
        self.PSI = 2*(F.sigmoid(self.psi)-0.5) * math.pi
        self.theta = F.sigmoid(self.t) * math.pi * 2
        self.Lambda = 1+(self.size-2)/self.sigma.max()*F.sigmoid(self.L)
        
        k_list = []
        for i in range(self.n_scales):
            kernel = RST_lift(self.channel_in, self.channel_out, self.n_roto, self.sigma[i], self.theta, self.Lambda, self.psi, self.gamma, self.size)
            kernel = kernel.unsqueeze(0)
            k_list.append(kernel)
        KERNEL = torch.cat(k_list,dim=0)
        # kernel in shape [n_scales, out_ch, n_roto, in_ch, ksize, ksize]
        KERNEL = KERNEL.permute(1,2,0,3,4,5).contiguous()
        # now kernel in shape [out_ch, num_rotations, num_scales, in_ch, ksize, ksize]
        # print('size:',self.size)
        KERNEL = KERNEL.view(-1, self.channel_in, 2*self.size+1, 2*self.size+1)
        # now kernel in shape [out_ch x num_rotations x num_scales, in_ch, ksize, ksize]
        
        out = F.conv2d(x, KERNEL, stride=self.stride, padding=self.padding)
        # out is in shape [batch, out_ch x num_rotations x num_scales, height, width]
        B, C, H, W = out.shape
        out = out.view(B, self.channel_out, self.n_roto, self.n_scales, H, W)
        
        return out
    
    def forward_no_input(self):
        # self.sigma = ((self.Max-self.Min)/2)*torch.tanh(self.scales)+((self.Min+self.Max)/2)  
        self.sigma = ((self.Max-self.Min)/2)+((self.Min+self.Max)/2)  
        print(self.sigma.shape, self.sigma.detach().cpu().numpy())
        self.gamma = F.sigmoid(self.g)  
        self.size = (2.*self.sigma.max()).ceil().item()
        self.PSI = 2*(F.sigmoid(self.psi)-0.5) * math.pi
#         self.PSI = self.psi
        self.theta = F.sigmoid(self.t) * math.pi * 2
        self.Lambda = 1+(self.size-2)/self.sigma.max()*F.sigmoid(self.L)
        
        k_list = []
        for i in range(self.n_scales):
            kernel = RST_lift(self.channel_in, self.channel_out, self.n_roto, self.sigma[i], self.theta, self.Lambda, self.psi, self.gamma, self.size)
            kernel = kernel.unsqueeze(0)
            # print(i,kernel.shape)
            k_list.append(kernel)
        KERNEL = torch.cat(k_list,dim=0)
        KERNEL = KERNEL.permute(1,2,0,3,4,5).contiguous()
        # now kernel in shape [out_ch, num_rotations, num_scales, in_ch, ksize, ksize]
        # print('stacked:',KERNEL.shape)
        
        return KERNEL, self.sigma.detach().cpu().numpy()


def plot_err_mat(err, sigma, factor, num_roto_90, angle, order):
    if num_roto_90==0:
        theta=0
    elif num_roto_90==1:
        theta=r'$\frac{\pi}{2}$'
    elif num_roto_90==2:
        theta=r'$\pi$'
    elif num_roto_90==3:
        theta=r'$\frac{3\pi}{2}$'
    fig = plt.figure(dpi=300)
    fig.clf()
    ax = fig.add_subplot(1, 1, 1)

    ax.annotate('', xy=(-.07, 1.07), xycoords='axes fraction', xytext=(0.01, 0.99),
           arrowprops=dict(arrowstyle="-", color='black', linewidth=0.5))


    for i in range(5):
        ax.annotate('', xy=(0.008,i*0.25), xycoords='axes fraction', xytext=(-0.08, i*0.25),
            arrowprops=dict(arrowstyle="-", color='black', linewidth=0.5))
        ax.annotate('', xy=(i*0.25, 0.99), xycoords='axes fraction', xytext=(i*0.25,1.08),
            arrowprops=dict(arrowstyle="-", color='black', linewidth=0.5))

    for i in range(20):
        for j in range(20):

            ax.text(j,i,"%00.2f" %(err[i,j]), color='white', fontsize=4, va='center', ha='center')

    idx = np.argmin(err,axis=1)
    for i in range(20):
        ax.add_patch(Rectangle((idx[i]-0.5,i%20-0.5), 1,1,
                     edgecolor = 'red',
                     fill=False,
                     lw=1))

    idx = [i for i in range(4)]
    idy = [(i+num_roto_90)%4 for i in range(4)]
    coord = zip(idx,idy)

    # print('idx:',idx, 'idy:',idy)
    for i in range(4):

        temp = err[idx[i]*5:(idx[i]+1)*5,idy[i]*5:(idy[i]+1)*5,]
#         print(temp.shape)
        r, c = np.where(temp == np.min(temp))
        # print('row:',r,'col:',c)
        ax.add_patch(Rectangle((idy[i]*5+c-0.5,idx[i]*5+r-0.5), 1,1,
                     edgecolor = 'blue',
                     fill=False,
                     lw=1))
        ax.add_patch(Rectangle((idy[i]*5-0.5,idx[i]*5-0.5), 5,5,
                     edgecolor = 'pink',
                     fill=False,
                     lw=1))

    xlocations = np.array([0.5, 1, 1.5, 2, 2.5]*4)
    # xlocations = sigma.tolist()+sigma.tolist()+sigma.tolist()+sigma.tolist()
    xlocations = sigma.tolist()*4

    plt.xticks([i for i in range(err.shape[0])], xlocations,fontsize=5)
    plt.yticks([i for i in range(err.shape[0])], xlocations,fontsize=5)

    for i,text in zip([.125,.375,.625,.875],['0',r'$\pi/2$',r'$\pi$',r'$3\pi/2$']):
        ax.text(i,1.06,text,transform = ax.transAxes,va="center",ha="center", fontsize=5)

    for i,text in zip([.125,.375,.625,.875],[r'$\frac{3\pi}{2}$', r'$\pi$', r'$\frac{\pi}{2}$', '0']):
        ax.text(-.06,i,text,transform = ax.transAxes,va="center",ha="center", fontsize=5)

    ax.text(-.015,1.06,r'$r$',transform = ax.transAxes,va="center",ha="center", fontsize=5)
    ax.text(-.03,1.01,r'$\sigma\prime$',transform = ax.transAxes,va="center",ha="center", fontsize=5)

    ax.text(-.015,1.035,r'$\sigma$',transform = ax.transAxes,va="center",ha="center", fontsize=5)
    ax.text(-.06,1.01,r'$r\prime$',transform = ax.transAxes,va="center",ha="center", fontsize=5)

    ax.xaxis.set_ticks_position('top')
    ax.tick_params(bottom=False,top=False,left=False,right=False)
    ax.tick_params(axis='x', pad=1)
    ax.tick_params(axis='y', pad=-1)
    plt.title(f'scale factor: {factor}')
    plt.title(r'$s={}$'.format(factor)+r',$\theta=${}'.format(theta), fontsize=6, x=0.5, y=1.06)

    ax.imshow(err,cmap='viridis') 
    plt.savefig(f'figs/{str(order)}_{str(angle)}_scale={factor}.png',bbox_inches='tight',dpi=400,pad_inches=0.0,set_visiable = False)

    # plt.show()


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



