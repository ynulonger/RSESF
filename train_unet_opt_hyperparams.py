import os
import sys
import time
import torch
import wandb
import logging
import argparse
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
from models.unet_model import *
from torch.utils.data import DataLoader, random_split
# from hyperparams_opt import sweep_configuration

# os.environ["WANDB_API_KEY"] = '0a16e1c5a65b09656c4f7bb51f4917d79c065372' 
# os.environ["WANDB_MODE"] ='offline'

class mosaic_Config:
    seed = 42
    device = "cuda" if torch.cuda.is_available() else "cpu"
    save_weights = True
    selected_model = 'CNN'
    dataset = 'Mosaic'
    img_size= 512
    classes = 5
    n_channels=1
    n_rotation=1
    n_filters = 64
    k_size = 5
    train_dataset = CustomImageSet('train', sample_weight=None, mask_channel=classes, factor=1, d_name=dataset)
    test_dataset  = CustomImageSet('test', sample_weight=None, mask_channel=classes,  factor=1, d_name=dataset)

class CRAG_Config:
    seed = 42
    device = "cuda" if torch.cuda.is_available() else "cpu"
    save_weights = True
    selected_model = 'CNN'
    dataset = 'CRAG'
    img_size= 512
    classes = 2
    n_channels=3
    n_rotation=1
    n_filters = 64
    k_size = 5
    train_dataset = CRAG('train', sample_weight=None, mask_channel=classes, factor=1)
    test_dataset  = CRAG('test', sample_weight=None, mask_channel=classes,  factor=1)

class GlaS_Config:
    seed = 42
    device = "cuda" if torch.cuda.is_available() else "cpu"
    save_weights = True
    selected_model = 'CNN'
    dataset = 'GlaS'
    img_size= 512
    classes = 2
    n_channels=3
    n_rotation=1
    n_filters = 64
    k_size = 5
    train_dataset = GlaS('train', sample_weight=None, mask_channel=classes, factor=1)
    test_dataset  = GlaS('test', sample_weight=None, mask_channel=classes,  factor=1)


sweep_config = {
    'method': 'random',
    'metric': {'goal': 'maximize', 'name': 'val_miou'},
    'parameters': 
    {
        'batch_size': {'distribution': 'uniform', 'max': 24, 'min': 2},
        'epochs': {'distribution': 'uniform', 'max': 2, 'min': 1},
        'lr': {'distribution': 'uniform', 'max': 0.1, 'min': 0.0001},
        'weight_decay': {'distribution': 'uniform', 'max': 1e-2, 'min': 1e-8}
     }
}

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

def fit(net, train_dataset, val_dataset, epochs, batch_size, lr, wd, model, dir_checkpoint, classes, save_name):

    device = "cuda" if torch.cuda.is_available() else "cpu"
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

    optimizer = optim.Adam(net.parameters(), lr=lr, weight_decay=wd)
    # if loss_fn=='iou':
    #     print('using iou loss')
    #     criterion = mIoULoss(n_classes=classes).cuda()
    # else:
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

        val_metrics   = {"val/val_loss": val_loss, "val/val_miou": val_miou.mean()}
        train_metrics = {"train/train_loss": train_loss, "train/train_miou": train_miou.mean()}
        wandb.log({**train_metrics, **val_metrics})

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
    wandb.finish()

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
    parser.add_argument('-f', '--factor', dest='factor', type=float, default=1,
                        help='factor')
    parser.add_argument('-k', '--k_size', dest='k_size', type=int, default=5,
                        help='k_size')
    parser.add_argument('-n', '--n_filters', dest='n_filters', type=int, default=8,
                        help='num of filters')
    parser.add_argument('-r', '--n_rotation', dest='n_rotation', type=int, default=8,
                        help='num of rotations')

    return parser.parse_args()

def count_your_model(model, x, y):
    # your rule here
    pass
    

def train(con=None, conf=mosaic_Config):
    with wandb.init(project=f'{conf.selected_model}-{conf.dataset}', config=con, count=3):
        con=wandb.config
        dir_checkpoint = 'checkpoints/'+conf.dataset+'/'
        if not os.path.exists(dir_checkpoint):
            os.makedirs(dir_checkpoint)
        print('--'*10, 'model name:', conf.selected_model, 'n_rotations:', conf.n_rotation, '--'*10)

        if conf.selected_model=='CNN':
            net = UNet_CNN(n_channels=conf.n_channels, n_classes=conf.classes, filters=conf.n_filters, bilinear=True, kernel_size=conf.k_size).cuda()
            save_name='wd_'+str(con.weight_decay)+'_lr_'+str(con.lr)+'_bn_'+str(con.batch_size)+'_epoch_'+str(con.epochs)+'_'+conf.selected_model+'_Ksize_'+str(conf.k_size)
        elif conf.selected_model=='E2CNN':
            if args.n_rotation==-1:
                conf.selected_model='H-Nets'
            net = e2UNet(n_channels=n_channels, n_classes=classes, filters=conf.n_filters, rotations=args.n_rotation, kernel_size=conf.k_size).cuda()
            save_name='wd_'+str(con.weight_decay)+'_lr_'+str(con.lr)+'_bn_'+str(con.batch_size)+'_epoch_'+str(con.epochs)+'_'+conf.selected_model+'_Ksize_'+str(conf.k_size)+'_Roto_'+str(args.n_rotation)
                
        summary(net, (conf.n_channels, conf.img_size, conf.img_size))
        print('--------------------------------------'*3)
        print('num of params:',get_num_parameters(net))
        net.to(device=device)
        net.zero_grad()
        fit(net, conf.train_dataset, conf.val_dataset, con.epochs, con.batch_size, con.lr, con.wd, conf.selected_model, dir_checkpoint, conf.classes, save_name)

print('--'*20)
sweep_id = wandb.sweep(sweep_config, project="cnn-sweep")
print('--'*40)
run=wandb.agent(sweep_id, train, count=6)
