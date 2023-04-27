import torch
import scipy
import math
import numpy as np
import matplotlib.pyplot as plt
import argparse

import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.nn.functional as F

import sys
sys.path.append("../") 
from gaussian_basis_filters import *

def main():
    # Training settings
    parser = argparse.ArgumentParser()
    parser.add_argument('--use-cuda', action='store_true', default=False,
                        help='disables CUDA training')
    parser.add_argument('--seed', type=int, default=1, metavar='S',
                        help='random seed (default: 1)')

    parser.add_argument('--order', type=int, default=2, \
                        help='Derivatives order')
    parser.add_argument('--sigma', type=float, default=1.0, \
                        help='Derivatives sigma')
    parser.add_argument('--k', type=float, default=2.0, \
                        help='Spatial extent')
    args = parser.parse_args()
    torch.manual_seed(args.seed)


    """ The order of the Gaussian basis. """
    F = int((args.order + 1) * (args.order + 2) / 2)                    

    """ Get the Gaussian derivative filters. """
    filtersize = math.ceil(args.k*args.sigma+0.5)
    x = torch.arange(start=-filtersize,end=filtersize+1,step=1)
    hermite = x
    _, g_srf, _,_ = gaussian_basis_filters_shared(
                x=x,
                hermite=hermite,
                order=args.order,
                sigma=torch.tensor([args.sigma], requires_grad=False),
                alphas=torch.tensor(np.ones([F,1,1]), dtype=torch.float32),
                use_cuda=args.use_cuda) 
    plot2g(g_srf, args.sigma, args.order, truncate=args.k)

if __name__ == '__main__':
    main()

