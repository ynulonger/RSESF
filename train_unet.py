import os
import sys
import time
import torch
import logging
import argparse
import numpy as np
import pandas as pd
import torch.nn as nn
from utils.metrics import *
from torch import optim
from thop import profile
# from utils.dataset import *
from utils.aug_dataset import *
from thop import clever_format
import torch.nn.functional as F
from torchsummary import summary
import matplotlib.ticker as ticker
from torch.autograd import Variable
from matplotlib import pyplot as plt
from models.unet_model import *
from torch.utils.data import DataLoader, random_split

Mosaic_train_transform = A.Compose(
    [
        A.ShiftScaleRotate(shift_limit=0., scale_limit=[-0.5, 2], rotate_limit=[0, 360], p=0.99),
        ToTensorV2(),
    ]
)
Mosaic_test_transform = A.Compose(
    [
        ToTensorV2(),
    ]
)

CRAG_train_transform = A.Compose(
    [
        A.ShiftScaleRotate(shift_limit=0., scale_limit=[-0.5, 2], rotate_limit=[0, 360], p=0.99),
        A.Normalize(mean=(0.8568, 0.7219, 0.8302), std=(0.0935, 0.1676, 0.1277)),
        ToTensorV2(),
    ]
)
CRAG_test_transform = A.Compose(
    [
        A.Normalize(mean=(0.8568, 0.7219, 0.8302), std=(0.0935, 0.1676, 0.1277)),
        ToTensorV2(),
    ]
)

GlaS_train_transform = A.Compose(
    [
        A.ShiftScaleRotate(shift_limit=0., scale_limit=[-0.5, 2], rotate_limit=[0, 360], p=0.99),
        A.Normalize(mean=(0.6535, 0.5831, 0.7515), std=(0.1994, 0.2388, 0.2010)),
        ToTensorV2(),
    ]
)
GlaS_test_transform = A.Compose(
    [
        A.Normalize(mean=(0.6535, 0.5831, 0.7515), std=(0.1994, 0.2388, 0.2010)),
        ToTensorV2(),
    ]
)

def get_num_parameters(module):
    params = [p.nelement() for p in module.parameters() if p.requires_grad]
    num = sum(params)
    return num

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
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=4, pin_memory=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False, num_workers=4, pin_memory=True)
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

    optimizer = optim.Adam(net.parameters(), lr=lr, weight_decay=1e-6)
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
        print(f'Epoch:{epoch+1}/{epochs}, time:{round(e_end-e_start, 1)}, Train_Loss:, {round(train_loss,4)}, Test_Loss: {round(val_loss,4)}, Train_mIoU:, {round(train_miou.mean(),4)}, Test_mIoU: {round(val_miou.mean(),4)}')
        print(f'train iou: {train_miou}, test iou: {val_miou}')
        train_loss_list.append(train_loss)
        val_loss_list.append(val_loss)
        train_iou_list=np.concatenate([train_iou_list, train_miou], axis=0)
        val_iou_list=np.concatenate([val_iou_list, val_miou], axis=0)

        if val_miou.mean()>best_miou:
            best_miou = val_miou.mean()
            torch.save(net.state_dict(), dir_checkpoint + f'{save_name}.pth')
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
    parser.add_argument('-e', '--epochs', metavar='E', type=int, default=50,
                        help='Number of epochs', dest='epochs')
    parser.add_argument('-l', '--learning-rate', metavar='LR', type=float, nargs='?', default=0.002,
                        help='Learning rate', dest='lr')
    parser.add_argument('-b', '--batch_size', dest='batch_size', type=int, default=16,
                        help='batch size')
    parser.add_argument('-m', '--model', dest='model', type=str, default='unet',
                        help='model')
    parser.add_argument('-g', '--gpu', dest='n_gpu', type=str, default='0',
                        help='number of gpus')
    parser.add_argument('-d', '--data', dest='data', type=str, default='GlaS',
                        help='dataset')
    parser.add_argument('-c', '--cost', dest='cost', type=str, default='ce',
                        help='dataset')
    parser.add_argument('-k', '--k_size', dest='k_size', type=int, default=3,
                        help='k_size')
    parser.add_argument('-n', '--n_filters', dest='n_filters', type=int, default=8,
                        help='num of filters')
    parser.add_argument('-r', '--n_rotation', dest='n_rotation', type=int, default=8,
                        help='num of rotations')

    return parser.parse_args()

def count_your_model(model, x, y):
    # your rule here
    pass
    
if __name__ == '__main__':
    img_size= 512

    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    args = get_args()
    os.environ["CUDA_VISIBLE_DEVICES"] = str(args.n_gpu)
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    logging.info(f'Using device {device}')
    dataset = args.data
    # dir_checkpoint = 'checkpoints/'+dataset+'/'
    dir_checkpoint = 'checkpoints_Aug/'+dataset+'/'
    if not os.path.exists(dir_checkpoint):
        os.makedirs(dir_checkpoint)
    print('--'*10, 'model name:', args.model, 'n_rotations:', args.n_rotation, '--'*10)

    if dataset=='CRAG':
        img_size= 512
        classes = 2
        n_channels=3
        train_dataset = CRAG('train',  mask_channel=2, transform=CRAG_train_transform)
        test_dataset  = CRAG('test',  mask_channel=2,  transform=CRAG_test_transform)
    elif dataset=='GlaS':
        img_size= 512
        classes = 2
        n_channels=3
        train_dataset = GlaS('train',  mask_channel=classes, transform=GlaS_train_transform)
        test_dataset  = GlaS('test',  mask_channel=classes,  transform=GlaS_test_transform)
    elif 'Mosaic' in dataset:
        img_size= 512
        classes = 5
        n_channels=1
        train_dataset = CustomImageSet('train',  mask_channel=classes, transform=Mosaic_train_transform, d_name=dataset)
        test_dataset  = CustomImageSet('test',  mask_channel=classes,  transform=Mosaic_test_transform, d_name=dataset)

    if args.model=='unet':
        net = UNet_CNN(n_channels=n_channels, n_classes=classes, filters=args.n_filters, bilinear=True, kernel_size=args.k_size).cuda()
        # save_name=str(args.lr)+'_'+args.cost+'_'+str(args.batch_size)+'_'+str(args.epochs)+'_'+args.model+'_KernelSize_'+str(args.k_size)
    elif args.model=='E2CNN' or args.model=='HNets':
        net = e2UNet(n_channels=n_channels, n_classes=classes, filters=args.n_filters, rotations=args.n_rotation, kernel_size=args.k_size).cuda()
    save_name='lr_'+str(args.lr)+'_bn_'+str(args.batch_size)+'_epoch_'+str(args.epochs)+'_'+args.model+'_Ksize_'+str(args.k_size)+'_rotation_'+str(args.n_rotation)
            
    summary(net, (n_channels, img_size, img_size))
    print('--------------------------------------'*3)
    print('num of params:',get_num_parameters(net))
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
                    save_name=save_name)
    # predict_img(net, val_dataset, device)
