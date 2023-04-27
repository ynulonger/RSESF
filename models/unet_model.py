""" Full assembly of the parts to form the complete network """
from .unet_parts import *
from e2cnn import nn as enn 

class UNet(nn.Module):
    def __init__(self, n_channels, n_classes, filters=16, init_order=2, bilinear=True, \
                 flag=False, srf=True, split=False, share_alpha=True, constraint_sigma=True, learn_sigma=True):
        super(UNet, self).__init__()
        self.n_channels = n_channels
        self.flag  = flag
        self.split = split
        self.scales= 5
        self.filters = filters
        if n_classes==1:
            self.n_classes = 2
        else:
            self.n_classes = n_classes
        self.bilinear = bilinear
        self.inc = DoubleConv(n_channels, filters, init_order=init_order, srf=[0,1], \
                              share_alpha=share_alpha, Min=0, Max=5, learn_sigma=learn_sigma)
        # self.down1 = Down(filters, 2*filters, init_order=init_order, srf=[1,1], share_alpha=share_alpha, Min=0.5, Max=3, learn_sigma=learn_sigma)
        # self.down2 = Down(2*filters, 4*filters, init_order=init_order, srf=[1,1], share_alpha=share_alpha, Min=1, Max=3.5, learn_sigma=learn_sigma)
        # self.down3 = Down(4*filters, 8*filters, init_order=init_order, srf=[1,1], share_alpha=share_alpha, Min=1.5, Max=4, learn_sigma=learn_sigma)
        # self.down4 = Down(8*filters, 16*filters, init_order=init_order, srf=[1,1], share_alpha=share_alpha, Min=2, Max=4.5, learn_sigma=learn_sigma)
        # self.up1 = Up(16*filters, 8*filters, init_order, bilinear, srf=[1,1], share_alpha=share_alpha, Min=1.5, Max=4, learn_sigma=learn_sigma)
        # self.up2 = Up(8*filters, 4*filters, init_order, bilinear, srf=[1,1], share_alpha=share_alpha, Min=1, Max=3.5, learn_sigma=learn_sigma)
        # self.up3 = Up(4*filters, 2*filters, init_order, bilinear, srf=[1,1], share_alpha=share_alpha, Min=0.5, Max=3, learn_sigma=learn_sigma)
        # self.up4 = Up(2*filters, filters, init_order, bilinear, srf=[1,1], share_alpha=share_alpha, Min=0, Max=2.5, learn_sigma=learn_sigma)
        
        self.down1 = Down(filters, 2*filters, init_order=init_order, srf=[1,1], share_alpha=share_alpha, Min=0, Max=5, learn_sigma=learn_sigma)
        self.down2 = Down(2*filters, 4*filters, init_order=init_order, srf=[1,1], share_alpha=share_alpha, Min=0, Max=5, learn_sigma=learn_sigma)
        self.down3 = Down(4*filters, 8*filters, init_order=init_order, srf=[1,1], share_alpha=share_alpha, Min=0, Max=5, learn_sigma=learn_sigma)
        self.down4 = Down(8*filters, 16*filters, init_order=init_order, srf=[1,1], share_alpha=share_alpha, Min=0, Max=5, learn_sigma=learn_sigma)
        self.up1 = Up(16*filters, 8*filters, init_order, bilinear, srf=[1,1], share_alpha=share_alpha, Min=0, Max=5, learn_sigma=learn_sigma)
        self.up2 = Up(8*filters, 4*filters, init_order, bilinear, srf=[1,1], share_alpha=share_alpha, Min=0, Max=5, learn_sigma=learn_sigma)
        self.up3 = Up(4*filters, 2*filters, init_order, bilinear, srf=[1,1], share_alpha=share_alpha, Min=0, Max=5, learn_sigma=learn_sigma)
        self.up4 = Up(2*filters, filters, init_order, bilinear, srf=[1,1], share_alpha=share_alpha, Min=0, Max=5, learn_sigma=learn_sigma)
        
        self.eta = None
        if self.split:
            self.eta = torch.tensor(np.reshape(np.array([1/self.scales]*self.scales), [1,self.scales]), \
                        dtype=torch.float32).cuda()
            self.eta = nn.Parameter(self.eta, requires_grad=True)
            self.outc = OutConv_share(filters, self.n_classes)
        else:
            self.outc = OutConv_share_ens(filters, self.n_classes)

    def forward(self, x):
        # out_conv_list = [self.outc_1,self.outc_2,self.outc_3,self.outc_4,\
        #                  self.outc_5,self.outc_6,self.outc_7,self.outc_8]
        # out_conv_list = [self.outc_1,self.outc_2,self.outc_3,self.outc_4,self.outc_5]
        x1 = self.inc(x)
        x2 = self.down1(x1)
        x3 = self.down2(x2)
        x4 = self.down3(x3)
        x5 = self.down4(x4)
        x6 = self.up1(x5, x4)
        x7 = self.up2(x6, x3)
        x8 = self.up3(x7, x2)
        x9 = self.up4(x8, x1)
        if self.flag:
            return [x1, x2, x3, x4, x5, x6, x7, x8, x9, self.outc(x9)]
        else:
            output = []
            if self.split:
                # for i in range(self.scales):
                #     output.append(out_conv_list[i](x9[:,i*(self.filters//self.scales):(i+1)*(self.filters//self.scales)]))      
                # return output
                logits = self.outc(x9)                
                return logits
            else:
                logits = self.outc(x9)                
                return logits

class e2UNet(nn.Module):
    def __init__(self, n_channels, n_classes, filters=32, rotations=8, kernel_size=3, flag=False):
        super().__init__()
        self.n_channels = n_channels
        self.flag  = flag
        self.rotations = rotations
        if n_classes==1:
            self.n_classes = 2
        else:
            self.n_classes = n_classes
        self.inc = einConv(n_channels, filters, rotations, kernel_size)
        self.down1 = eDown(filters, 2*filters, rotations, kernel_size)
        self.down2 = eDown(2*filters, 4*filters, rotations, kernel_size+2)
        self.down3 = eDown(4*filters, 8*filters, rotations, kernel_size+2)
        self.down4 = eDown(8*filters, 16*filters, rotations, kernel_size+4)
        self.up1 = eUp(16*filters, 8*filters, rotations, kernel_size+2)
        self.up2 = eUp(8*filters, 4*filters, rotations, kernel_size+2)
        self.up3 = eUp(4*filters, 2*filters, rotations, kernel_size)
        self.up4 = eUp(2*filters, filters, rotations, kernel_size)
        self.outc = OutConv(filters, self.n_classes)

    def forward(self, x):
        x1 = self.inc(x)
        x2 = self.down1(x1)
        x3 = self.down2(x2)
        x4 = self.down3(x3)
        x5 = self.down4(x4)
        x6 = self.up1(x5, x4)
        x7 = self.up2(x6, x3)
        x8 = self.up3(x7, x2)
        x9 = self.up4(x8, x1)
        if self.rotations==-1:
            logits = self.outc(x9.tensor)
        else:
            logits = self.outc(enn.GroupPooling(x9.type)(x9).tensor)
        if self.flag:
            return [x1, x2, x3, x4, x5, x6, x7, x8, x9, logits]
        else:
            return logits

class e2UNet_Mini(nn.Module):
    def __init__(self, n_channels, n_classes, filters=32, rotations=8, kernel_size=3, flag=False):
        super().__init__()
        self.n_channels = n_channels
        self.flag  = flag
        self.rotations = rotations
        if n_classes==1:
            self.n_classes = 2
        else:
            self.n_classes = n_classes
        self.inc = einConv(n_channels, filters, rotations, kernel_size)
        self.down1 = eDown(filters, 2*filters, rotations, kernel_size+2)
        self.up1 = eUp(2*filters, filters, rotations, kernel_size)
        self.outc = OutConv(filters, self.n_classes)

    def forward(self, x):
        x1 = self.inc(x)
        x2 = self.down1(x1)
        x3 = self.up1(x2, x1)
        if self.rotations==-1:
            logits = self.outc(x3.tensor)
        else:
            logits = self.outc(enn.GroupPooling(x3.type)(x3).tensor)
        if self.flag:
            return [x1, x2, x3, logits]
        else:
            return logits

class UNet_R_Mini(nn.Module):
    def __init__(self, n_channels, n_classes, filters=32, init_order=1, init_scale=0.65, bilinear=True, \
                 flag=False, srf='r', split=True, share_alpha=True, constraint_sigma=True, n_scales=1,\
                 learn_sigma=True, angles=[torch.tensor(0)], rotation_size=1, k=2.5, lower_bound=0.4,\
                 selection=0):
        super(UNet_R_Mini, self).__init__()
        self.n_channels = n_channels
        self.flag  = flag
        self.split = split
        self.filters = filters
        if n_classes==1:
            self.n_classes = 2
        else:
            self.n_classes = n_classes
        self.bilinear = bilinear


        self.inc = DoubleConv(n_channels, filters, init_order=init_order, init_scale=init_scale, srf=srf, share_alpha=share_alpha, \
                                 Min = lower_bound+torch.tensor([i/k for i in range(n_scales)]), Max = lower_bound+torch.tensor([i/k for i in range(1, n_scales+1)]),\
                                learn_sigma=learn_sigma, angles=angles, n_scales=n_scales, first=True, rotation_size=rotation_size, k=k)
        self.down1 = Down(filters, 2*filters, init_order=init_order, init_scale=init_scale, srf=srf, share_alpha=share_alpha, \
                                 Min = lower_bound+torch.tensor([i/k for i in range(1, n_scales+1)]), Max = lower_bound+torch.tensor([i/k for i in range(2, n_scales+2)]),\
                                learn_sigma=learn_sigma, angles=angles, n_scales=n_scales, rotation_size=rotation_size, k=k)
        self.up1 = Up_R(2*filters, filters, init_order=init_order, init_scale=init_scale, bilinear=bilinear, srf=srf, share_alpha=share_alpha, \
                                 Min = lower_bound+torch.tensor([i/k for i in range(n_scales)]), Max = lower_bound+torch.tensor([i/k for i in range(1, n_scales+1)]),\
                                learn_sigma=learn_sigma, angles=angles, n_scales=n_scales, rotation_size=rotation_size, k=k)

        self.outc = R_OutConv(filters, self.n_classes, n_scales=n_scales, n_rotations=len(angles), selection=selection)

    def forward(self, x):
        x1 = self.inc(x)
        x2 = self.down1(x1)
        x3 = self.up1(x2, x1)
        logits = self.outc(x3)[0]
        if self.flag:
            return [x1, x2, x3, logits]
        else:
            return logits

class UNet_R(nn.Module):
    def __init__(self, n_channels, n_classes, filters=32, init_order=1, init_scale=0.65, bilinear=True, \
                 flag=False, srf='r', split=True, share_alpha=True, constraint_sigma=True, n_scales=3,\
                 learn_sigma=True, angles=[torch.tensor(0)], rotation_size=1, k=2.5, scale_offset=[0,1,1,2,2,3],\
                 selection=0):
        super(UNet_R, self).__init__()
        self.n_channels = n_channels
        self.flag  = flag
        self.split = split
        self.filters = filters
        if n_classes==1:
            self.n_classes = 2
        else:
            self.n_classes = n_classes
        self.bilinear = bilinear


        self.inc = DoubleConv(n_channels, filters, init_order=init_order, init_scale=init_scale, srf=srf, share_alpha=share_alpha, \
                                 Min = 0.4+torch.tensor([i/k for i in range(n_scales)]), Max = 0.4+torch.tensor([i/k for i in range(1, n_scales+1)]),\
                                learn_sigma=learn_sigma, angles=angles, n_scales=n_scales, first=True, rotation_size=rotation_size, k=k)
        self.down1 = Down(filters, 2*filters, init_order=init_order, init_scale=init_scale, srf=srf, share_alpha=share_alpha, \
                                 Min = 0.4+torch.tensor([i/k for i in range(n_scales)]), Max = 0.4+torch.tensor([i/k for i in range(1, n_scales+1)]),\
                                learn_sigma=learn_sigma, angles=angles, n_scales=n_scales, rotation_size=rotation_size, k=k)
        self.down2 = Down(2*filters, 4*filters, init_order=init_order, init_scale=init_scale, srf=srf, share_alpha=share_alpha, \
                                 Min = 0.4+torch.tensor([i/k for i in range(1, n_scales+1)]), Max = 0.4+torch.tensor([i/k for i in range(2, n_scales+2)]),\
                                learn_sigma=learn_sigma, angles=angles, n_scales=n_scales, rotation_size=rotation_size, k=k)
        self.down3 = Down(4*filters, 8*filters, init_order=init_order, init_scale=init_scale, srf=srf , share_alpha=share_alpha, \
                                 Min = 0.4+torch.tensor([i/k for i in range(1, n_scales+1)]), Max = 0.4+torch.tensor([i/k for i in range(2, n_scales+2)]),\
                                learn_sigma=learn_sigma, angles=angles, n_scales=n_scales, rotation_size=rotation_size, k=k)
        self.down4 = Down(8*filters, 16*filters, init_order=init_order, init_scale=init_scale, srf=srf, share_alpha=share_alpha, \
                                 Min = 0.4+torch.tensor([i/k for i in range(2, n_scales+2)]), Max = 0.4+torch.tensor([i/k for i in range(3, n_scales+3)]),\
                                learn_sigma=learn_sigma, angles=angles, n_scales=n_scales, rotation_size=rotation_size, k=k)
        self.up1 = Up_R(16*filters, 8*filters, init_order=init_order, init_scale=init_scale, bilinear=bilinear, srf=srf, share_alpha=share_alpha,\
                                 Min = 0.4+torch.tensor([i/k for i in range(1, n_scales+1)]), Max = 0.4+torch.tensor([i/k for i in range(2, n_scales+2)]),\
                                learn_sigma=learn_sigma, angles=angles, n_scales=n_scales, rotation_size=rotation_size, k=k)
        self.up2 = Up_R(8*filters, 4*filters, init_order=init_order, init_scale=init_scale, bilinear=bilinear, srf=srf, share_alpha=share_alpha, \
                                 Min = 0.4+torch.tensor([i/k for i in range(1, n_scales+1)]), Max = 0.4+torch.tensor([i/k for i in range(2, n_scales+2)]),\
                                learn_sigma=learn_sigma, angles=angles, n_scales=n_scales, rotation_size=rotation_size, k=k)
        self.up3 = Up_R(4*filters, 2*filters, init_order=init_order, init_scale=init_scale, bilinear=bilinear, srf=srf, share_alpha=share_alpha, \
                                 Min = 0.4+torch.tensor([i/k for i in range(n_scales)]), Max = 0.4+torch.tensor([i/k for i in range(1, n_scales+1)]),\
                                learn_sigma=learn_sigma, angles=angles, n_scales=n_scales, rotation_size=rotation_size, k=k)
        self.up4 = Up_R(2*filters, filters, init_order=init_order, init_scale=init_scale, bilinear=bilinear, srf=srf, share_alpha=share_alpha, \
                                 Min = 0.4+torch.tensor([i/k for i in range(n_scales)]), Max = lower_bound+torch.tensor([i/k for i in range(1, n_scales+1)]),\
                                learn_sigma=learn_sigma, angles=angles, n_scales=n_scales, rotation_size=rotation_size, k=k)

        self.eta = torch.tensor(np.reshape(np.array([1/n_scales]*n_scales), [1,n_scales]), dtype=torch.float32).cuda()
        self.eta = nn.Parameter(self.eta, requires_grad=True)
        self.outc = R_OutConv(filters, self.n_classes, n_scales=n_scales, n_rotations=len(angles), selection=selection)

    def forward(self, x):
        x1 = self.inc(x)
        x2 = self.down1(x1)
        x3 = self.down2(x2)
        x4 = self.down3(x3)
        x5 = self.down4(x4)
        x6 = self.up1(x5, x4)
        x7 = self.up2(x6, x3)
        x8 = self.up3(x7, x2)
        x9 = self.up4(x8, x1)
        logits = self.outc(x9)
        if self.flag:
            return [x1, x2, x3, x4, x5, x6, x7, x8, x9, logits]
        else:
            return logits

class UNet_R_Pool(nn.Module):
    def __init__(self, n_channels, n_classes, filters=32, init_order=2, init_scale=0.65, bilinear=True, \
                 flag=False, srf='r', share_alpha=True, n_scales=4, learn_sigma=True, \
                 angles=[torch.tensor(0+i*math.pi/2) for i in range(4)], rotation_size=1):
        super(UNet_R_Pool, self).__init__()
        self.n_channels = n_channels
        self.flag  = flag
        self.filters = filters
        if n_classes==1:
            self.n_classes = 2
        else:
            self.n_classes = n_classes
        self.bilinear = bilinear

        self.inc = DoubleConv(n_channels, filters, init_order=init_order, init_scale=init_scale, srf=srf, share_alpha=share_alpha, \
                                 Min = torch.tensor([i/k for i in range(n_scales)]), Max = torch.tensor([i/k for i in range(1, n_scales+1)]),\
                                learn_sigma=learn_sigma, angles=angles, n_scales=n_scales, first=True, rotation_size=rotation_size, k=k)
        self.down1 = Down(filters, 2*filters, init_order=init_order, init_scale=init_scale, srf=srf, share_alpha=share_alpha, \
                                 Min = torch.tensor([i/k for i in range(n_scales)]), Max = torch.tensor([i/k for i in range(1, n_scales+1)]),\
                                learn_sigma=learn_sigma, angles=angles, n_scales=n_scales, rotation_size=rotation_size, k=k)
        self.down2 = Down(2*filters, 4*filters, init_order=init_order, init_scale=init_scale, srf=srf, share_alpha=share_alpha, \
                                 Min = torch.tensor([i/k for i in range(1, n_scales+1)]), Max = torch.tensor([i/k for i in range(2, n_scales+2)]),\
                                learn_sigma=learn_sigma, angles=angles, n_scales=n_scales, rotation_size=rotation_size, k=k)
        self.down3 = Down(4*filters, 8*filters, init_order=init_order, init_scale=init_scale, srf=srf , share_alpha=share_alpha, \
                                 Min = torch.tensor([i/k for i in range(1, n_scales+1)]), Max = torch.tensor([i/k for i in range(2, n_scales+2)]),\
                                learn_sigma=learn_sigma, angles=angles, n_scales=n_scales, rotation_size=rotation_size, k=k)
        self.down4 = Down(8*filters, 16*filters, init_order=init_order, init_scale=init_scale, srf=srf, share_alpha=share_alpha, \
                                 Min = torch.tensor([i/k for i in range(2, n_scales+2)]), Max = torch.tensor([i/k for i in range(3, n_scales+3)]),\
                                learn_sigma=learn_sigma, angles=angles, n_scales=n_scales, rotation_size=rotation_size, k=k)
        self.up1 = Up_R(16*filters, 8*filters, init_order=init_order, init_scale=init_scale, bilinear=bilinear, srf=srf, share_alpha=share_alpha,\
                                 Min = torch.tensor([i/k for i in range(1, n_scales+1)]), Max = torch.tensor([i/k for i in range(2, n_scales+2)]),\
                                learn_sigma=learn_sigma, angles=angles, n_scales=n_scales, rotation_size=rotation_size, k=k)
        self.up2 = Up_R(8*filters, 4*filters, init_order=init_order, init_scale=init_scale, bilinear=bilinear, srf=srf, share_alpha=share_alpha, \
                                 Min = torch.tensor([i/k for i in range(1, n_scales+1)]), Max = torch.tensor([i/k for i in range(2, n_scales+2)]),\
                                learn_sigma=learn_sigma, angles=angles, n_scales=n_scales, rotation_size=rotation_size, k=k)
        self.up3 = Up_R(4*filters, 2*filters, init_order=init_order, init_scale=init_scale, bilinear=bilinear, srf=srf, share_alpha=share_alpha, \
                                 Min = torch.tensor([i/k for i in range(n_scales)]), Max = torch.tensor([i/k for i in range(1, n_scales+1)]),\
                                learn_sigma=learn_sigma, angles=angles, n_scales=n_scales, rotation_size=rotation_size, k=k)
        self.up4 = Up_R(2*filters, filters, init_order=init_order, init_scale=init_scale, bilinear=bilinear, srf=srf, share_alpha=share_alpha, \
                                 Min = torch.tensor([i/k for i in range(n_scales)]), Max = torch.tensor([i/k for i in range(1, n_scales+1)]),\
                                learn_sigma=learn_sigma, angles=angles, n_scales=n_scales, rotation_size=rotation_size, k=k)
        self.outc = R_Pool_OutConv(filters, self.n_classes)

    def forward(self, x):
        x1 = self.inc(x)
        x2 = self.down1(x1)
        x3 = self.down2(x2)
        x4 = self.down3(x3)
        x5 = self.down4(x4)
        x6 = self.up1(x5, x4)
        x7 = self.up2(x6, x3)
        x8 = self.up3(x7, x2)
        x9 = self.up4(x8, x1)
        logits = self.outc(x9)
        if self.flag:
            return [x1, x2, x3, x4, x5, x6, x7, x8, x9, logits]
        else:
            return logits

class UNet_gabor(nn.Module):
    def __init__(self, n_channels, n_classes, filters=16, bilinear=True, flag=False, srf='gabor', split=True):
        super(UNet_gabor, self).__init__()
        self.n_channels = n_channels
        self.flag  = flag
        self.split = split
        self.scales= 5
        self.filters = filters
        if n_classes==1:
            self.n_classes = 2
        else:
            self.n_classes = n_classes
        self.bilinear = bilinear

        self.inc = DoubleConv(n_channels, filters, srf='gabor', Min=0, Max=2.5, first=True)
        self.down1 = Down(filters, 2*filters, srf='gabor',  Min=0, Max=2.5,)
        self.down2 = Down(2*filters, 4*filters, srf='gabor', Min=0, Max=2.5,)
        self.down3 = Down(4*filters, 8*filters, srf='gabor', Min=0, Max=2.5,)
        self.down4 = Down(8*filters, 16*filters, srf='gabor', Min=0, Max=2.5,)
        self.up1 = Up(16*filters, 8*filters, bilinear, srf='gabor', Min=0, Max=2.5,)
        self.up2 = Up(8*filters, 4*filters, bilinear, srf='gabor', Min=0, Max=2.5,)
        self.up3 = Up(4*filters, 2*filters, bilinear, srf='gabor', Min=0, Max=2.5,)
        self.up4 = Up(2*filters, filters, bilinear, srf='gabor', Min=0, Max=2.5,)

        self.eta = None
        if self.split:
            self.eta = torch.tensor(np.reshape(np.array([1/self.scales]*self.scales), [1,self.scales]), \
                        dtype=torch.float32).cuda()
            self.eta = nn.Parameter(self.eta, requires_grad=True)
            self.outc = OutConv_share(filters, self.n_classes)
        else:
            self.outc = OutConv_share_ens(filters, self.n_classes)

    def forward(self, x):
        # out_conv_list = [self.outc_1,self.outc_2,self.outc_3,self.outc_4,\
        #                  self.outc_5,self.outc_6,self.outc_7,self.outc_8]
        # out_conv_list = [self.outc_1,self.outc_2,self.outc_3,self.outc_4,self.outc_5]
        x1 = self.inc(x)
        x2 = self.down1(x1)
        x3 = self.down2(x2)
        x4 = self.down3(x3)
        x5 = self.down4(x4)
        x6 = self.up1(x5, x4)
        x7 = self.up2(x6, x3)
        x8 = self.up3(x7, x2)
        x9 = self.up4(x8, x1)
        if self.flag:
            return [x1, x2, x3, x4, x5, x6, x7, x8, x9, self.outc(x9)]
        else:
            output = []
            if self.split:
                # for i in range(self.scales):
                #     output.append(out_conv_list[i](x9[:,i*(self.filters//self.scales):(i+1)*(self.filters//self.scales)]))      
                # return output
                logits = self.outc(x9)                
                return logits
            else:
                logits = self.outc(x9)                
                return logits


class UNet_CNN(nn.Module):
    def __init__(self, n_channels, n_classes, filters=16, bilinear=False, flag=False, kernel_size=3):
        super(UNet_CNN, self).__init__()
        self.n_channels = n_channels
        self.flag = flag
        if n_classes==1:
            self.n_classes = 2
        else:
            self.n_classes = n_classes
        self.bilinear = bilinear
        self.inc = DoubleConv_CNN(n_channels, filters, kernel_size=kernel_size)
        self.down1 = Down_CNN(filters, 2*filters, kernel_size=kernel_size)
        self.down2 = Down_CNN(2*filters, 4*filters, kernel_size=kernel_size)
        self.down3 = Down_CNN(4*filters, 8*filters, kernel_size=kernel_size)
        # factor = 2 if bilinear else 1
        self.down4 = Down_CNN(8*filters, 16*filters, kernel_size=kernel_size)
        self.up1 = Up_CNN(16*filters, 8*filters, bilinear, kernel_size=kernel_size)
        self.up2 = Up_CNN(8*filters, 4*filters, bilinear, kernel_size=kernel_size)
        self.up3 = Up_CNN(4*filters, 2*filters, bilinear, kernel_size=kernel_size)
        self.up4 = Up_CNN(2*filters, filters, bilinear, kernel_size=kernel_size)
        self.outc = OutConv(filters, self.n_classes)

    def forward(self, x):
        x1 = self.inc(x)
        x2 = self.down1(x1)
        x3 = self.down2(x2)
        x4 = self.down3(x3)
        x5 = self.down4(x4)
        x6 = self.up1(x5, x4)
        x7 = self.up2(x6, x3)
        x8 = self.up3(x7, x2)
        x9 = self.up4(x8, x1)
        logits = self.outc(x9)
        if self.flag:
            return [x1, x2, x3, x4, x5, x6, x7, x8, x9, logits]
        else:
            return logits