import os
import sys
import time
import math
import torch
import logging
import argparse
import datetime
import numpy as np
import pandas as pd
import torch.nn as nn
from utils.metrics import *
from torch import optim
from thop import profile
from utils.dataset import *
from thop import clever_format
import torch.nn.functional as F
from torchsummary import summary
import matplotlib.ticker as ticker
from torch.autograd import Variable
from matplotlib import pyplot as plt
from models.unet_model import UNet_RST, UNet_R
from torch.utils.data import DataLoader, random_split
from pytorch_modelsize import SizeEstimator

def evaluate(criterion, net, loader, device, classes):
    net.eval()
    metrics = Metrics(classes)
    iou = 0
    loss = 0
    length = 0

    for batch in loader:
        with torch.no_grad():
            imgs = Variable(batch['image'].to(device=device, dtype=torch.float32))
            true_masks = Variable(batch['mask'].to(device=device, dtype=torch.long))
            masks_pred = net(imgs)
            temp_loss = criterion(masks_pred, torch.argmax(true_masks, dim=1))
            # temp_loss = criterion(masks_pred, true_masks)
            loss += temp_loss.item()
            # preds = torch.sigmoid(masks_pred)
            # preds = (preds>0.5)
            preds = F.softmax(masks_pred,dim=1)
            preds = torch.argmax(preds, dim=1).squeeze(1)
            if len(true_masks.size())==4:
                true_masks=torch.argmax(true_masks, dim=1)
            masks = true_masks.view(-1)
            preds = preds.view(-1)
            metrics.add(preds, masks)
            length += 1
    miou = metrics.iou(average=False).cpu().numpy()
    miou = np.reshape(miou,[1,-1])
    return miou, loss/length

def train_net(net, device, train_dataset, val_dataset, epochs, batch_size, lr, model, dir_checkpoint, loss_fn, classes, save_name):

    n_train = train_dataset.__len__()
    n_val   = val_dataset.__len__()
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=8, pin_memory=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False, num_workers=8, pin_memory=True)
    train_loss_list = []
    val_loss_list  = []

    train_iou_list = np.empty([0,classes])
    val_iou_list  = np.empty([0,classes])

    global_step = 0

    logging.info(f'''Starting training:
        Epochs:          {epochs}
        Batch size:      {batch_size}
        Learning rate:   {lr}
        Training size:   {n_train}
        Validation size: {n_val}
        Device:          {device.type}
        model name:      {model}
    ''')

    optimizer = optim.Adam(net.parameters(), lr=lr, weight_decay=1e-5)
    if loss_fn=='iou':
        print('using iou loss')
        criterion = mIoULoss(n_classes=classes).cuda()
    else:
        print('using CE loss')
        # criterion = SoftCrossEntropy(reduction='mean').cuda()
        criterion = nn.CrossEntropyLoss(reduction='mean').cuda()


    train_scheduler = optim.lr_scheduler.OneCycleLR(optimizer, max_lr=lr, steps_per_epoch=len(train_loader), epochs=epochs)
    best_miou=0
    for epoch in range(epochs):

        e_start=time.time()
        net.train()
        train_loss = 0
        for batch in train_loader:
            imgs = Variable(batch['image'].to(device=device, dtype=torch.float32))
            true_masks = Variable(batch['mask'].to(device=device, dtype=torch.long))
            masks_pred = net(imgs)
            optimizer.zero_grad()
            loss = criterion(masks_pred, torch.argmax(true_masks, dim=1))

            train_loss += loss
            loss.backward()
            optimizer.step()
            train_scheduler.step()

        train_miou, train_loss = evaluate(criterion, net, train_loader, device, classes)
        val_miou, val_loss = evaluate(criterion, net, val_loader, device, classes)
        
        

        e_end=time.time()
        print(f'{datetime.datetime.now()}, Epoch:{epoch+1}/{epochs}, time:{round(e_end-e_start, 1)}, Train_Loss:, {round(train_loss,4)}, Test_Loss: {round(val_loss,4)}, Train_mIoU:, {round(train_miou.mean(),4)}, Test_mIoU: {round(val_miou.mean(),4)}')
        print(f'train iou: {train_miou}, test iou: {val_miou}')
        train_loss_list.append(train_loss)
        val_loss_list.append(val_loss)
        train_iou_list=np.concatenate([train_iou_list, train_miou], axis=0)
        val_iou_list=np.concatenate([val_iou_list, val_miou], axis=0)

        if val_miou.mean()>best_miou:
            best_miou = val_miou.mean()
            torch.save(net.state_dict(), dir_checkpoint + f'{save_name}_relu.pth')
            logging.info(f'Checkpoint {epoch + 1} saved !')  
            
    train_loss_list = np.reshape(np.array(train_loss_list),[-1,1])
    val_loss_list   = np.reshape(np.array(val_loss_list),[-1,1])


    loss_curve = np.concatenate([train_loss_list, val_loss_list], axis=1)
    iou_curve = np.concatenate([train_iou_list, val_iou_list], axis=1)

    loss_record = pd.DataFrame(loss_curve)
    iou_record = pd.DataFrame(iou_curve)

    writer = pd.ExcelWriter(dir_checkpoint+f'{save_name}.xlsx')      
    loss_record.to_excel(writer, 'loss', float_format='%.8f')       
    iou_record.to_excel(writer, 'iou', float_format='%.8f')
    writer.save()

    writer.close()
    return net

def get_args():
    parser = argparse.ArgumentParser(description='Train the UNet on images and target masks')
    parser.add_argument('-e', '--epochs', metavar='E', type=int, default=70,
                        help='Number of epochs', dest='epochs')
    parser.add_argument('-l', '--learning-rate', metavar='LR', type=float, nargs='?', default=0.001,
                        help='Learning rate', dest='lr')
    parser.add_argument('-b', '--batch_size', dest='batch_size', type=int, default=120,
                        help='batch size')
    parser.add_argument('-m', '--model', dest='model', type=str, default='r',
                        help='model')
    parser.add_argument('-g', '--gpu', dest='n_gpu', type=str, default='0',
                        help='number of gpus')
    parser.add_argument('-d', '--data', dest='data', type=str, default='BCSS',
                        help='dataset')
    parser.add_argument('-c', '--cost', dest='cost', type=str, default='ce',
                        help='dataset')
    parser.add_argument('-f', '--factor', dest='factor', type=float, default=1,
                        help='factor')
    parser.add_argument('-o', '--order', dest='order', type=int, default=2,
                        help='order')
    parser.add_argument('-n', '--n_filters', dest='n_filters', type=int, default=12,
                        help='num of filters')
    parser.add_argument('-s', '--sigma', dest='sigma', type=float, default=0.66,
                        help='num of filters')
    parser.add_argument('-r', '--n_rotation', dest='n_rotation', type=int, default=2,
                        help='num of filters')
    parser.add_argument('-k', '--n_scales', dest='n_scales', type=int, default=3,
                        help='num of filters')
    return parser.parse_args()

def count_your_model(model, x, y):
    # your rule here
    pass
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    args = get_args()
    os.environ["CUDA_VISIBLE_DEVICES"] = str(args.n_gpu)
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    logging.info(f'Using device {device}')
    print('order:', args.order, 'number of rotation interaction:', args.rotation_size, 'sigma:', args.sigma)
    dataset = args.data
    dir_checkpoint = 'checkpoints/'+dataset+f'/rotation_size_{str(args.rotation_size)}'
    if not os.path.exists(dir_checkpoint):
        os.makedirs(dir_checkpoint)

    if args.factor==0:
        args.factor = [1,2,3,4]
    if dataset=='BCSS':
        img_size= 512
        classes = 5
        n_channels=3
        train_dataset = BCSS('train', sample_weight=None, mask_channel=5, factor=args.factor)
        test_dataset  = BCSS('test', sample_weight=None, mask_channel=5,  factor=args.factor)

    elif dataset=='CRAG':
        img_size= 512
        classes = 2
        n_channels=3
        train_dataset = CRAG('train', sample_weight=None, mask_channel=2, factor=args.factor)
        test_dataset  = CRAG('test', sample_weight=None, mask_channel=2,  factor=args.factor)

    elif dataset=='Mosaic':
        img_size= 512
        classes = 5
        n_channels=1
        train_dataset = CustomImageSet('train', sample_weight=None, mask_channel=classes, factor=args.factor)
        test_dataset  = CustomImageSet('test', sample_weight=None, mask_channel=classes,  factor=args.factor)

    elif dataset=='Kumar':
        img_size= 400       
        classes = 2
        n_channels=3
        train_dataset = Kumar('train', sample_weight=None, mask_channel=2, factor=args.factor)
        test_dataset  = Kumar('test', sample_weight=None, mask_channel=2,  factor=args.factor)

    if args.model=='rst':
        net = UNet_RST(n_channels=3, n_classes=classes, filters=args.n_filters, init_order=args.order, bilinear=True).cuda()
    elif args.model=='r':
        net = UNet_R(n_channels=n_channels, n_classes=classes, filters=args.n_filters, init_order=args.order, bilinear=True, \
                     init_scale=args.sigma, angles=[torch.tensor(0+i*math.pi/2) for i in range(args.n_rotation)],\
                     n_scales=args.n_scales, rotation_size=1).cuda()

    img_size = int(img_size*args.factor)    
    summary(net, (n_channels, img_size, img_size))
    # se = SizeEstimator(net, input_size=(4, n_channels, img_size, img_size))
    # estimate = se.estimate_size()
    # print('(Size in Megabytes, Total Bits):', estimate)
    print('num of params', sum(p.numel() for p in net.parameters() if p.requires_grad))
    net.to(device=device)


    # inputs = torch.randn(1, 3, 512, 512).to(device=device)
    # flops, params = profile(net, inputs=(inputs, ), custom_ops={UNet: count_your_model})
    # flops, params = clever_format([flops, params], "%.3f")
    # print("flops", flops, "params", params)
    # if args.load:
    #     net.load_state_dict(torch.load(args.load, map_location=device))
    #     logging.info(f'Model loaded from {args.load}')

    net = train_net(net=net, device=device, train_dataset= train_dataset, val_dataset=test_dataset,
                    epochs=args.epochs, batch_size=args.batch_size, lr=args.lr, model =args.model,
                    dir_checkpoint=dir_checkpoint, loss_fn=args.cost, classes=classes, 
                    save_name=str(args.lr)+'_'+args.cost+'_'+str(args.batch_size)+'_'+str(args.epochs)+'_'+args.model+'_order_'+str(args.order)+'_sigma_'+str(args.sigma))
    # predict_img(net, val_dataset, device)
