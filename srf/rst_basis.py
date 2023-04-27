import math
import torch
import numpy as np
import torch.nn as nn
# from scipy import ndimage
import torch.nn.functional as F
from torch.autograd import Variable
import gc    



""" Create the Gaussian derivative basis.
Input:
    - x: the input grid
    - hermite: a temporary variable (initialized as the grid x)
    - order: the order of the basis
    - sigma: the sigma of the Gaussian
    - alphas: the coefficients for combining the basis
    - use_cuda: on GPU or not
"""

def gaussian_basis_filters(x, y, order, sigma, alphas, use_cuda, angles=[torch.tensor(0)]):
    basis_filters = []
    basis_tensors = []
    basis_roto = []
    step = math.pi/2
#     angles = [torch.tensor(i*2*math.pi/n_roto) for i in range(n_roto)]
            
    """ Define the 0th order Gaussian vector for the current scale. """
    try:
        x = x.cuda()
        y = y.cuda()
    except:
        print("No cuda available")    
    gauss_x = torch.div(1.0, (torch.sqrt(2.0 * torch.tensor(math.pi)) * sigma)) \
        * torch.exp( torch.div( x*x, (-2.0*sigma*sigma)))
    gauss_x = gauss_x / torch.sum(gauss_x)
    
    gauss_y = torch.div(1.0, (torch.sqrt(2.0 * torch.tensor(math.pi)) * sigma)) \
        * torch.exp( torch.div( y*y, (-2.0*sigma*sigma)))
    gauss_y = gauss_y / torch.sum(gauss_y)
    
    """ Define the rest of the Gaussian derivatives. """
    basis = []
    for i in range(0, int(order)+1):
        basis_x = get_basis(x, i, gauss_x, sigma)
        basis_x = torch.pow(sigma, i) * basis_x 

        for j in range(int(order)-i, -1, -1):
#             print('i:',i,'j:',j)
            basis_y = get_basis(y, j, gauss_y, sigma)
            basis_y = torch.pow(sigma, j) * basis_y 

            """ Create square filters from the 1D vectors. """
            basis.append(torch.einsum("i,j->ij", basis_x, basis_y))
    basis_tensor = torch.stack(basis, dim=0) #  FHW
    # basis_roto.append(basis_tensor)   
    
    for angle in angles:
        if order==1:
            temp_basis = torch.ones_like(basis_tensor)
            temp_basis[0] = basis_tensor[0]*torch.cos(angle)+basis_tensor[-1]*torch.sin(angle)
            temp_basis[-1] = basis_tensor[-1]*torch.cos(-angle)+basis_tensor[0]*torch.sin(-angle)
            temp_basis[1] = basis_tensor[1]
        elif order==2:
            
            # temp_basis[0]
            tb_0 = basis_tensor[0]*torch.cos(angle)**2\
                            +basis_tensor[5]*torch.sin(angle)**2\
                            +basis_tensor[3]*torch.sin(angle)*torch.cos(angle)*2

            # temp_basis[1]
            tb_1 = basis_tensor[1]*torch.cos(angle)+basis_tensor[4]*torch.sin(angle)

            # temp_basis[2] 
            tb_2 = basis_tensor[2]

            # temp_basis[5] 
            tb_5 = basis_tensor[0]*torch.cos(step+angle)**2\
                            +basis_tensor[5]*torch.sin(step+angle)**2\
                            +basis_tensor[3]*torch.sin(step+angle)*torch.cos(step+angle)*2
            
            # temp_basis[4] 
            tb_4 = basis_tensor[1]*torch.cos(angle+step)+basis_tensor[4]*torch.sin(angle+step)

            # temp_basis[3]
            tb_3 = tb_1*tb_4/basis_tensor[2]
            temp_basis = torch.cat([tb_0.unsqueeze(0),tb_1.unsqueeze(0),tb_2.unsqueeze(0),\
                                    tb_3.unsqueeze(0),tb_4.unsqueeze(0),tb_5.unsqueeze(0)], dim=0)
            
            # temp_basis = torch.ones_like(basis_tensor)
            # temp_basis[0] = basis_tensor[0]*torch.cos(angle)**2\
            #                 +basis_tensor[5]*torch.sin(angle)**2\
            #                 +basis_tensor[3]*torch.sin(angle)*torch.cos(angle)*2
            # temp_basis[5] = basis_tensor[0]*torch.cos(step+angle)**2\
            #                 +basis_tensor[5]*torch.sin(step+angle)**2\
            #                 +basis_tensor[3]*torch.sin(step+angle)*torch.cos(step+angle)*2
            # temp_basis[1] = basis_tensor[1]*torch.cos(angle)+basis_tensor[4]*torch.sin(angle)
            # temp_basis[4] = basis_tensor[1]*torch.cos(angle+step)+basis_tensor[4]*torch.sin(angle+step)
            # temp_basis[3] = temp_basis[1]*temp_basis[4]/basis_tensor[2]
            # temp_basis[2] = basis_tensor[2]

        elif order==3:
            temp_basis = torch.ones_like(basis_tensor)
            temp_basis[0] = basis_tensor[0]*torch.cos(angle)**3\
                           +basis_tensor[9]*torch.sin(angle)**3\
                           +3*torch.sin(angle)*torch.cos(angle)**2*basis_tensor[1]*basis_tensor[6]/basis_tensor[3]\
                           +3*torch.cos(angle)*torch.sin(angle)**2*basis_tensor[2]*basis_tensor[8]/basis_tensor[3]
            temp_basis[9] = basis_tensor[0]*torch.cos(angle+step)**3\
                           +basis_tensor[9]*torch.sin(angle+step)**3\
                           +3*torch.sin(angle+step)*torch.cos(angle+step)**2*basis_tensor[1]*basis_tensor[6]/basis_tensor[3]\
                           +3*torch.cos(angle+step)*torch.sin(angle+step)**2*basis_tensor[2]*basis_tensor[8]/basis_tensor[3]
            temp_basis[1] = basis_tensor[1]*torch.cos(angle)**2\
                            +basis_tensor[8]*torch.sin(angle)**2\
                            +basis_tensor[5]*torch.sin(angle)*torch.cos(angle)*2
            temp_basis[8] = basis_tensor[1]*torch.cos(angle+step)**2\
                            +basis_tensor[8]*torch.sin(angle+step)**2\
                            +basis_tensor[5]*torch.sin(angle+step)*torch.cos(angle+step)*2
            temp_basis[2] = basis_tensor[2]*torch.cos(angle)\
                            +basis_tensor[6]*torch.sin(angle)
            temp_basis[6] = basis_tensor[2]*torch.cos(angle+step)\
                            +basis_tensor[6]*torch.sin(angle+step)
            temp_basis[3] = basis_tensor[3]            
            temp_basis[4] = temp_basis[2].clone()*temp_basis[8].clone()/basis_tensor[3]
            temp_basis[7] = temp_basis[1].clone()*temp_basis[6].clone()/basis_tensor[3]
            temp_basis[5] = temp_basis[2].clone()*temp_basis[6].clone()/basis_tensor[3]
        
        basis_roto.append(temp_basis)    
        
    """ Create the filter by combining the basis with the coefficients, alpha."""
    basis_filter = None 
    # [out_channels,in_channels,kernel_size[0],kernel_size[1]]

#     basis_filter = torch.einsum("fck,fhw->kchw", alphas, basis_tensor)

    basis_filter = [torch.einsum("fck,fhw->kchw", alphas, basis_tensor_r).unsqueeze(0) for basis_tensor_r in basis_roto]
    basis_filter = torch.cat(basis_filter,dim=0).unsqueeze(1)
    return basis_filter, basis_roto



""" Hermite, recursive implementation. It's slow and recursivity does not work well with pytorch.
Inputs:
    - x: the input grid
    - order: the order of the derivative
"""
def hermite_recursive(x, order): # Physicists hermite
    assert(order>=0.0)
    if order==0.0:
        return (x * 0.0 + 1.0)

    elif order==1.0:
        # H{1}(x) = 2 x 
        return 2.0 * x
    
    else:
        # H{n}(x) = 2x H{n-1}(x) - 2(n-1) H{n-2}(x)
        return 2.0*x*hermite_recursive(x, order-1.0) - 2.0*(order-1.0) \
                * hermite_recursive(x, order-2.0)


""" 0-order Hermite polynomial. """
def hermite_0(x):
    return (x*0.0+1.0)


""" 1-order Hermite polynomial. """
def hermite_1(x):
    # H{1}(x) = x 
    return 2.0*x
    

""" 2-order Hermite polynomial. """
def hermite_2(x):
    # H{2}(x) = 4 x^2 - 2
    return (4.0*torch.pow(x,2.0) - 2.0)
 
""" 3-order Hermite polynomial. """
def hermite_3(x):
    # H{3}(x) = 8 x^3 - 12x 
    return (8.0*torch.pow(x,3.0) - 12.0 * x)


""" Switching between the Hermite orders."""
switcher = {
        0: hermite_0,
        1: hermite_1,
        2: hermite_2,
        3: hermite_3,
        }


""" Calls the Hermite polynomial computation of a certain order.
Input:
    - x: the grid
    - order: the order of the derivative.
"""
def get_hermite(x, order):
    assert(order>=0.0)
    try:
        func = switcher.get(int(order))
    except:
        func = hermite_recursive
        return func(x,order)
    return func(x)

""" Get the Gaussian basis using Hermite polynomials.
Input:
    - x: the grid
    - order: the order of the derivative.
    - sigma: The sigma of the Gaussian
    - hermite: temporary variable, initialized as the grid.
"""
def get_basis(
        x,
        order,
        gauss,
        sigma):
    # dg^n / dx^n = ( -1/(sqrt(2)sigma) ) ^n H(x / (sqrt(2) sigma)) g

    hermite = get_hermite(torch.div(x, torch.sqrt(torch.tensor(2.0))*sigma), order) 
    return torch.pow(torch.div(-1.0, torch.sqrt(torch.tensor(2.0)) * sigma), order) \
            * hermite * gauss
