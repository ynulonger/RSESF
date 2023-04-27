import os
import sys
import time
import wandb
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
from torchsummary import summary
import torch.distributed as dist
from models.unet_model import UNet_gabor as UNet
import matplotlib.ticker as ticker
from torch.autograd import Variable
from matplotlib import pyplot as plt
from torch.utils.data import DataLoader, random_split


def get_num_parameters(module):
    params = [p.nelement() for p in module.parameters() if p.requires_grad]
    num = sum(params)
    return num

def compute_loss(criterion, pred_list, mask, net):
    epslion = 1/5
    loss = 0
    alpha_vector = []
    i=0
    loss = torch.empty(0, requires_grad=True).cuda(f'cuda:0')
    for pred in pred_list:

        temp_loss = criterion(pred.squeeze(1), mask).view(1,1)
        loss = torch.cat([loss, temp_loss], dim=1)

    eta_temp = F.softmax(net.eta.view(-1), dim=0)+epslion
    eta_temp = eta_temp/eta_temp.sum()
    # eta_temp = F.softmax(net.eta.view(-1), dim=0)

    loss_ = torch.dot(loss.view(-1), eta_temp)
    return loss_, loss

def evaluate(criterion, net, loader, classes):
    net.eval()
    metrics = Metrics(classes)
    loss = 0
    loss_list = torch.zeros([1,5]).cuda()

    eta = F.softmax(net.eta.view(-1), dim=0)
    branch = eta.argmax()

    for batch in loader:
        with torch.no_grad():
            imgs = batch['image'].cuda(f'cuda:0') #to(device=device, dtype=torch.float32))
            true_masks = batch['mask'].cuda(f'cuda:0') #to(device=device, dtype=torch.long))
            true_masks=torch.argmax(true_masks, dim=1)
            pred_list = net(imgs)
            temp_loss, temp_loss_list = compute_loss(criterion, pred_list, true_masks, net)
            loss += temp_loss
            loss_list += temp_loss_list
            preds = F.softmax(pred_list[branch].squeeze(1),dim=1)
            preds = torch.argmax(preds, dim=1).squeeze(1)
            masks = true_masks.view(-1)
            preds = preds.view(-1)
            metrics.add(preds, masks)
    cm = metrics._confusion_matrix

    return cm, loss, loss_list

def train_net(net, train_dataset, val_dataset, epochs, batch_size, lr, \
              model, dir_checkpoint, loss_fn, img_size, classes, save_name, branches=5):

    ETA = np.ones([1,branches])/branches
    n_train = train_dataset.__len__()
    n_val   = val_dataset.__len__()
    train_loader = DataLoader(train_dataset, batch_size=batch_size, \
                              num_workers=0, pin_memory=False, shuffle=True)
    val_loader   = DataLoader(val_dataset, batch_size=batch_size, \
                              num_workers=0, pin_memory=False, shuffle=False)
    train_loss_list = []
    val_loss_list  = []
    train_h_loss = np.empty([0,branches])
    val_h_loss = np.empty([0,branches])
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

    optimizer = optim.Adam(net.parameters(), lr=lr, weight_decay=1e-5)
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
        e_start=time.time()
        net.train()
        count=0
        for batch in train_loader:
            imgs = batch['image'].cuda() #to(device=device, dtype=torch.float32))
            true_masks = batch['mask'].cuda() #to(device=device, dtype=torch.long))
            true_masks = torch.argmax(true_masks, dim=1)
            count += true_masks.shape[0]
            pred_list = net(imgs)
            # print(masks_pred.shape)
            optimizer.zero_grad()
            # loss = criterion(masks_pred, torch.argmax(true_masks, dim=1))
            loss, loss_list = compute_loss(criterion, pred_list, true_masks, net)

            loss.backward()
            optimizer.step()
            train_scheduler.step()

        train_cm, train_loss, train_hidden_loss = evaluate(criterion, net, train_loader, classes)
        val_cm, val_loss, val_hidden_loss       = evaluate(criterion, net, val_loader, classes)

        
        train_miou = iou(train_cm, False)
        val_miou   = iou(val_cm, False)
        train_loss = train_loss.item()/(n_train*img_size[0]*img_size[1])
        val_loss = val_loss.item()/(n_val*img_size[0]*img_size[1])
        train_hidden_loss = train_hidden_loss/(n_train*img_size[0]*img_size[1])
        val_hidden_loss   = val_hidden_loss/(n_val*img_size[0]*img_size[1])

        e_end=time.time()
        print(f'Epoch:{epoch+1}/{epochs}, time:{round(e_end-e_start, 1)},\
                Train_Loss:, {round(train_loss,4)}, Test_Loss: {round(val_loss,4)}, \
                Train_mIoU:, {round(train_miou.mean(),4)}, Test_mIoU: {round(val_miou.mean(),4)}')

        epslion=1/5
        eta_temp = F.softmax(net.eta.view(-1), dim=0)+epslion
        eta_temp = eta_temp/eta_temp.sum()

        branch = eta_temp.argmax()
        print('eta:', eta_temp.detach().cpu().numpy(), 'max branch:', branch)

        # print(f'train iou: {train_miou}, test iou: {val_miou}')
        train_h_loss = np.concatenate([train_h_loss, train_hidden_loss.cpu().numpy()], axis=0)
        train_loss_list.append(train_loss)
        val_h_loss  = np.concatenate([val_h_loss, val_hidden_loss.cpu().numpy()], axis=0)
        val_loss_list.append(val_loss)

        train_iou_list=np.concatenate([train_iou_list, train_miou], axis=0)
        val_iou_list=np.concatenate([val_iou_list, val_miou], axis=0)

        
        ETA = np.concatenate([ETA, eta_temp.view(1,branches).cpu().detach().numpy()], axis=0)

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
    ETA_record = pd.DataFrame(ETA)
    train_h_loss = pd.DataFrame(train_h_loss)
    val_h_loss  = pd.DataFrame(val_h_loss)

    writer = pd.ExcelWriter(dir_checkpoint+f'{save_name}.xlsx')      
    loss_record.to_excel(writer, 'loss', float_format='%.8f')       
    iou_record.to_excel(writer, 'iou', float_format='%.8f')
    ETA_record.to_excel(writer, 'eta', float_format='%.8f')
    train_h_loss.to_excel(writer, 'train_hidden', float_format='%.8f')
    val_h_loss.to_excel(writer, 'test_hidden', float_format='%.8f')
    writer.save()
    writer.close()
    return net

def get_args():
    parser = argparse.ArgumentParser(description='Train the UNet on images and target masks')
    parser.add_argument('-e', '--epochs', metavar='E', type=int, default=70,
                        help='Number of epochs', dest='epochs')
    parser.add_argument('-l', '--learning-rate', metavar='LR', type=float, nargs='?', default=0.015,
                        help='Learning rate', dest='lr')
    parser.add_argument('-b', '--batch_size', dest='batch_size', type=int, default=20,
                        help='batch size')
    parser.add_argument('-m', '--model', dest='model', type=str, default='gabor',
                        help='model')
    parser.add_argument('-d', '--data', dest='data', type=str, default='BCSS',
                        help='dataset')
    parser.add_argument('-s', '--srf', dest='srf', type=str, default='gabor',
                        help='srf')
    parser.add_argument('-f', '--factor', dest='factor', type=float, default=1,
                        help='factor')
    return parser.parse_args()

def count_your_model(model, x, y):
    # your rule here
    pass
    
if __name__ == '__main__':
    torch.manual_seed(34)
    random.seed(34)
    tracemalloc.start()

    classes = 5
    img_size= 512

    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    args = get_args()
    # os.environ["CUDA_VISIBLE_DEVICES"] = str(args.n_gpu)
    
    dataset = args.data
    dir_checkpoint = 'checkpoints/'+dataset+'_'+args.srf+'/'
    if not os.path.exists(dir_checkpoint):
        os.makedirs(dir_checkpoint)


    if args.factor==0:
        args.factor = [1,2,3,4]
        img_size = 384
    else:
        img_size = int(img_size*args.factor)

    if dataset=='BCSS':
        classes = 5
        train_dataset = BCSS('train', sample_weight=None, mask_channel=5, factor=args.factor)
        test_dataset  = BCSS('test', sample_weight=None, mask_channel=5,  factor=args.factor)
    elif dataset=='CRAG':
        classes = 2
        train_dataset = CRAG('train', sample_weight=None, mask_channel=2, factor=args.factor)
        test_dataset  = CRAG('test', sample_weight=None, mask_channel=2,  factor=args.factor)
    elif dataset=='GlaS':
        classes = 2
        train_dataset = GlaS('train', sample_weight=None, mask_channel=2, factor=args.factor)
        test_dataset  = GlaS('test', sample_weight=None, mask_channel=2,  factor=args.factor)
    elif dataset=='Kumar':
        img_size= 400       
        classes = 2
        train_dataset = Kumar('train', sample_weight=None, mask_channel=2, factor=args.factor)
        test_dataset  = Kumar('test', sample_weight=None, mask_channel=2,  factor=args.factor)

    device_ids=range(torch.cuda.device_count())

    net = UNet(n_channels=3, n_classes=classes, filters=60, srf=args.srf, bilinear=True, 
               split=True).cuda()
    # net = torch.nn.parallel.DistributedDataParallel(net, device_ids=[args.local_rank])
    summary(net, (3, img_size, img_size))
    
    print('--------------------------------------')
    print('num of params:',get_num_parameters(net))
    
    if len(device_ids)>1:
        device_ids = str(device_ids)[1:-1]
        print(f"we have {torch.cuda.device_count()} GPUs, let's use DataParallel" )
        net=torch.nn.DataParallel(net)

    # for p in net.parameters():
    #     print(p, p.size())

    # inputs = torch.randn(1, 3, 512, 512).cuda()
    # flops, params = profile(net, inputs=(inputs, ), custom_ops={UNet: count_your_model})
    # flops, params = clever_format([flops, params], "%.3f")
    # print("flops", flops, "params", params)

    # if args.load:
    #     net.load_state_dict(torch.load(args.load, map_location=device))
    #     logging.info(f'Model loaded from {args.load}')


    net = train_net(net=net, train_dataset= train_dataset, val_dataset=test_dataset, epochs=args.epochs, 
                    batch_size=args.batch_size, lr=args.lr, model =args.model, dir_checkpoint=dir_checkpoint, 
                    loss_fn='ce', img_size=[img_size,img_size],classes=classes, 
                    save_name=str(args.lr)+'_'+str(args.batch_size)+'_'+str(args.epochs)+'_'+\
                    args.model)


    # snapshot = tracemalloc.take_snapshot()
    # top_stats = snapshot.statistics('lineno')

    # print("[ Top 10 ]")
    # for stat in top_stats[:10]:
        # print(stat)
    # predict_img(net, val_dataset, device)
