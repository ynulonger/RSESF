import os
import sys
import time
import torch
import logging
import argparse
import tracemalloc
import numpy as np
import pandas as pd
import torch.nn as nn
from torch import optim
from thop import profile
from utils.dataset import *
from utils.metrics import *
from thop import clever_format
import torch.nn.functional as F
import torch.distributed as dist
from torchsummary import summary
import torch.distributed as dist
from models.unet_model import UNet
import matplotlib.ticker as ticker
from torch.autograd import Variable
from matplotlib import pyplot as plt
from torch.utils.data import DataLoader, random_split
from torch.nn.parallel import DistributedDataParallel as DPP

def evaluate(criterion, net, loader, classes):
    net.eval()
    metrics = Metrics(classes)
    loss = 0
    counter = 0
    pixels = torch.tensor(0).cuda()
    for batch in loader:
        with torch.no_grad():
            imgs = batch['image'].cuda(f'cuda:{dist.get_rank()}') #to(device=device, dtype=torch.float32))
            true_masks = batch['mask'].cuda(f'cuda:{dist.get_rank()}') #to(device=device, dtype=torch.long))
            masks_pred = net(imgs)
            temp_loss = criterion(masks_pred, torch.argmax(true_masks, dim=1))
            loss += temp_loss
            # preds = torch.sigmoid(masks_pred)
            # preds = (preds>0.5)
            preds = F.softmax(masks_pred,dim=1)
            preds = torch.argmax(preds, dim=1).squeeze(1)
            if len(true_masks.size())==4:
                true_masks=torch.argmax(true_masks, dim=1)
            masks = true_masks.view(-1)
            preds = preds.view(-1)
            metrics.add(preds, masks)
            counter += masks_pred.shape[0]
            pixels += masks_pred.shape[0]*masks_pred.shape[2]*masks_pred.shape[3]
    # miou = metrics.iou(average=False).cpu().numpy()
    # miou = np.reshape(miou,[1,-1])
    # return miou, loss/length
    cm = metrics._confusion_matrix
    # print(dist.get_rank(), 'loss:', loss/counter, 'length:',counter, 'pixels:', pixels, 'img shape:', masks_pred.shape, 'cm.sum:', cm.sum())
    torch.distributed.reduce(cm, 0)#op=torch.distributed.ReduceOp.SUM)
    torch.distributed.reduce(loss, 0)# op=torch.distributed.ReduceOp.SUM)
    torch.distributed.reduce(pixels, 0)# op=torch.distributed.ReduceOp.SUM)
    return cm, loss, pixels

def train_net(net, train_dataset, val_dataset, epochs, batch_size, lr, \
              model, dir_checkpoint, loss_fn, img_size, classes, save_name):
    tr_cm =0
    va_cm =0
    n_train = train_dataset.__len__()
    n_val   = val_dataset.__len__()
    train_sampler = torch.utils.data.distributed.DistributedSampler(train_dataset, drop_last=False)
    val_sampler   = torch.utils.data.distributed.DistributedSampler(val_dataset, shuffle=False, drop_last=False)

    train_loader = DataLoader(train_dataset, batch_size=batch_size, \
                              num_workers=0, pin_memory=False, sampler=train_sampler)
    val_loader   = DataLoader(val_dataset, batch_size=batch_size, \
                              num_workers=0, pin_memory=False, sampler=val_sampler)
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
        model name:      {model}
    ''')

    optimizer = optim.Adam(net.parameters(), lr=lr, weight_decay=1e-7)
    if loss_fn=='iou':
        print('using iou loss')
        criterion = mIoULoss(n_classes=classes).cuda()
    else:
        print('using CE loss')
        # criterion = SoftCrossEntropy(reduction='mean').cuda()
        criterion = nn.CrossEntropyLoss(reduction='sum').cuda()


    train_scheduler = optim.lr_scheduler.OneCycleLR(optimizer, max_lr=lr, \
                            steps_per_epoch=len(train_loader), epochs=epochs)
    best_miou=0
    for epoch in range(epochs):

        # for n, p in net.named_parameters():
        #     if 'scales' in n or 'sigma' in n:
        #         print(n, 2**p)

        e_start=time.time()
        net.train()
        train_loss = 0
        train_sampler.set_epoch(epoch)
        for batch in train_loader:
            imgs = Variable(batch['image'].cuda()) #to(device=device, dtype=torch.float32))
            true_masks = Variable(batch['mask'].cuda()) #to(device=device, dtype=torch.long))
            masks_pred = net(imgs)
            # print(masks_pred.shape)
            optimizer.zero_grad()
            loss = criterion(masks_pred, torch.argmax(true_masks, dim=1))

            train_loss += loss
            loss.backward()
            optimizer.step()
            train_scheduler.step()

        train_cm, train_loss, train_pixels = evaluate(criterion, net, train_loader, classes)
        val_cm, val_loss, val_pixels       = evaluate(criterion, net, val_loader, classes)

        # print('----------------',train_cm.sum(), val_cm.sum(),'----------------')

        # torch.distributed.reduce(train_cm, 0, op=dist.ReduceOp.SUM)#op=torch.distributed.ReduceOp.SUM)
        # torch.distributed.reduce(train_loss, 0, op=dist.ReduceOp.SUM)# op=torch.distributed.ReduceOp.SUM)
        # torch.distributed.reduce(val_cm, 0, op=dist.ReduceOp.SUM)#op=torch.distributed.ReduceOp.SUM)
        # torch.distributed.reduce(val_loss, 0, op=dist.ReduceOp.SUM)# op=torch.distributed.ReduceOp.SUM)
        
        if dist.get_rank()==0:
            # print('----------------',train_cm.sum(), val_cm.sum(), train_pixels, val_pixels, '----------------')
            train_miou = iou(train_cm, False)
            val_miou   = iou(val_cm, False)
            train_loss = train_loss.item()/(n_train*img_size[0]*img_size[1])
            val_loss = val_loss.item()/(n_val*img_size[0]*img_size[1])

            e_end=time.time()
            print(f'Epoch:{epoch+1}/{epochs}, time:{round(e_end-e_start, 1)},\
                    Train_Loss:, {round(train_loss,4)}, Test_Loss: {round(val_loss,4)}, \
                    Train_mIoU:, {round(train_miou.mean(),4)}, Test_mIoU: {round(val_miou.mean(),4)}')
            # print(f'train iou: {train_miou}, test iou: {val_miou}')
            train_loss_list.append(train_loss)
            val_loss_list.append(val_loss)
            train_iou_list=np.concatenate([train_iou_list, train_miou], axis=0)
            val_iou_list=np.concatenate([val_iou_list, val_miou], axis=0)

            if val_miou.mean()>best_miou:
                best_miou = val_miou.mean()
                torch.save(net.state_dict(), dir_checkpoint + f'{save_name}.pth')
                logging.info(f'Checkpoint {epoch + 1} saved !')  
    if dist.get_rank()==0:    
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
    parser.add_argument('-b', '--batch_size', dest='batch_size', type=int, default=10,
                        help='batch size')
    parser.add_argument('-m', '--model', dest='model', type=str, default='unet',
                        help='model')
    parser.add_argument('-d', '--data', dest='data', type=str, default='BCSS',
                        help='dataset')
    parser.add_argument('-c', '--cost', dest='cost', type=str, default='ce',
                        help='dataset')
    parser.add_argument('-f', '--factor', dest='factor', type=float, default=1,
                        help='factor')
    parser.add_argument('--local_rank', default=-1, type=int,
                        help='node rank for distributed training')
    return parser.parse_args()

def count_your_model(model, x, y):
    # your rule here
    pass
    
if __name__ == '__main__':
    torch.manual_seed(43)
    random.seed(43)
    # tracemalloc.start()

    img_size= 512

    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    args = get_args()
    # os.environ["CUDA_VISIBLE_DEVICES"] = str(args.n_gpu)
    # device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    dist.init_process_group(backend='nccl')
    torch.cuda.set_device(args.local_rank)
    
    dataset = args.data
    dir_checkpoint = 'checkpoints/'+dataset+'/'
    if not os.path.exists(dir_checkpoint):
        os.makedirs(dir_checkpoint)
 
    if args.factor==0:
        args.factor = [1,2,3,4]
    
    if dataset=='BCSS':
        classes = 5
        train_dataset = BCSS('train', sample_weight=None, mask_channel=5, factor=args.factor)
        test_dataset  = BCSS('test', sample_weight=None, mask_channel=5,  factor=args.factor)

    elif dataset=='CRAG':
        classes = 2
        train_dataset = CRAG('train', sample_weight=None, mask_channel=2, factor=args.factor)
        test_dataset  = CRAG('test', sample_weight=None, mask_channel=2,  factor=args.factor)


    img_size = int(img_size*args.factor)

    net = UNet(n_channels=3, n_classes=classes, filters=60, bilinear=True, srf=srf).cuda()
    summary(net, (3, img_size, img_size))
    net = torch.nn.parallel.DistributedDataParallel(net, device_ids=[args.local_rank])

    # inputs = torch.randn(1, 3, 512, 512).cuda()
    # flops, params = profile(net, inputs=(inputs, ), custom_ops={UNet: count_your_model})
    # flops, params = clever_format([flops, params], "%.3f")
    # print("flops", flops, "params", params)

    # if args.load:
    #     net.load_state_dict(torch.load(args.load, map_location=device))
    #     logging.info(f'Model loaded from {args.load}')


    net = train_net(net=net, train_dataset= train_dataset, val_dataset=test_dataset,
                    epochs=args.epochs, batch_size=args.batch_size, lr=args.lr, model =args.model,
                    dir_checkpoint=dir_checkpoint, loss_fn=args.cost, img_size=[img_size,img_size],
                    classes=classes, save_name=str(args.lr)+'_'+args.cost+'_'+str(args.batch_size)+'_'+str(args.epochs)+'_'+args.model+'_'+str(args.factor))
    # snapshot = tracemalloc.take_snapshot()
    # top_stats = snapshot.statistics('lineno')

    # print("[ Top 10 ]")
    # for stat in top_stats[:10]:
    #     print(stat)
    # predict_img(net, val_dataset, device)
