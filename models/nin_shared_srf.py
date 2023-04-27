import torch.nn as nn
import math
from srf.structured_conv_layer import *

__all__ = ['nin_shared_srf']

class NiN_shared_srf(nn.Module):
    def __init__(self,
                num_classes,
                init_k, 
                init_order,
                init_scale,
                learn_sigma,
                use_cuda):

        super(NiN_shared_srf, self).__init__()

        """ In our model we removed all padding and pooling """ 
        self.srf1 = Srf_layer_shared(
                        inC=3, 
                        outC=192,
                        init_k=init_k, 
                        init_order=init_order, 
                        init_scale=init_scale, 
                        learn_sigma=learn_sigma,
                        use_cuda=use_cuda)
        self.classifier1 = nn.Sequential(
                nn.BatchNorm2d(192),
                nn.ReLU(inplace=True),
                
                nn.Conv2d(192, 160, kernel_size=1, stride=1, padding=0, \
                        bias=False),
                nn.BatchNorm2d(160),
                nn.ReLU(inplace=True),

                nn.Conv2d(160,  96, kernel_size=1, stride=1, padding=0, \
                        bias=False),
                nn.BatchNorm2d(96),
                nn.ReLU(inplace=True),
                nn.Dropout(0.5)
                )

        self.srf2 = Srf_layer_shared(
                        inC=96, 
                        outC=192,
                        init_k=init_k, 
                        init_order=init_order, 
                        init_scale=init_scale, 
                        learn_sigma=learn_sigma,
                        use_cuda=use_cuda)
        self.classifier2 = nn.Sequential(
                nn.BatchNorm2d(192),
                nn.ReLU(inplace=True),

                nn.Conv2d(192, 192, kernel_size=1, stride=1, padding=0, \
                        bias=False),
                nn.BatchNorm2d(192),
                nn.ReLU(inplace=True),
                
                nn.Conv2d(192, 192, kernel_size=1, stride=1, padding=0, \
                        bias=False),
                nn.BatchNorm2d(192),
                nn.ReLU(inplace=True),
                nn.Dropout(0.5)
                )

        self.srf3 = Srf_layer_shared(
                        inC=192, 
                        outC=192,
                        init_k=init_k, 
                        init_order=init_order, 
                        init_scale=init_scale, 
                        learn_sigma=learn_sigma,
                        use_cuda=use_cuda)
        self.classifier3 = nn.Sequential(
                nn.BatchNorm2d(192),
                nn.ReLU(inplace=True),

                nn.Conv2d(192, 192, kernel_size=1, stride=1, padding=0, \
                        bias=False),
                nn.BatchNorm2d(192),
                nn.ReLU(inplace=True),

                nn.Conv2d(192, num_classes, kernel_size=1, stride=1, padding=0, \
                        bias=False),
                nn.BatchNorm2d(num_classes),
                nn.ReLU(inplace=True),
                )
        self.num_classes = num_classes
        self.extra_reg = 0
    
    def forward(self, x):
        x = self.srf1(x)
        x = self.classifier1(x)
        x = self.srf2(x)
        x = self.classifier2(x)
        x = self.srf3(x)
        x = self.classifier3(x)

        self.extra_reg = self.srf1.extra_reg + self.srf2.extra_reg + \
                            self.srf3.extra_reg

        x = torch.mean(x, dim=(2,3))
        x = x.view(x.size(0), self.num_classes)
        return x

def nin_shared_srf(**kwargs):
    """
    Constructs a NiN with N-Jet layers.
    """
    return NiN_shared_srf(**kwargs)

