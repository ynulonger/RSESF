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
import torch.distributed as dist
from torchsummary import summary
import torch.distributed as dist
from models.unet_model import UNet
import matplotlib.ticker as ticker
from torch.autograd import Variable
from matplotlib import pyplot as plt
from torch.utils.data import DataLoader, random_split
from torch.nn.parallel import DistributedDataParallel as DPP

os.environ["WANDB_API_KEY"] = '0a16e1c5a65b09656c4f7bb51f4917d79c065372' 
os.environ["WANDB_MODE"] ='offline'

def compute_loss(criterion, pred_list, mask, net):
    loss = 0
    alpha_vector = []
    i=0
    loss = torch.empty(0, requires_grad=True).cuda(f'cuda:{dist.get_rank()}')
    for pred in pred_list:

        temp_loss = criterion(pred, mask).view(1,1)
        loss = torch.cat([loss, temp_loss], dim=1)

    # alpha_temp = (F.softmax(net.alpha.view(-1), dim=0)+epslion)
    # alpha_temp = alpha_temp/alpha_temp.sum()
    eta_temp = F.softmax(net.module.eta.view(-1), dim=0)

    loss_ = torch.dot(loss.view(-1), eta_temp)
    return loss_, loss

def evaluate(criterion, net, loader, classes):
    net.eval()
    metrics = Metrics(classes)
    loss = 0
    loss_list = torch.zeros([1,5]).cuda()

    eta = F.softmax(net.module.eta.view(-1), dim=0)
    branch = eta.argmax()

    for batch in loader:
        with torch.no_grad():
            imgs = batch['image'].cuda(f'cuda:{dist.get_rank()}') #to(device=device, dtype=torch.float32))
            true_masks = batch['mask'].cuda(f'cuda:{dist.get_rank()}') #to(device=device, dtype=torch.long))
            true_masks=torch.argmax(true_masks, dim=1)
            pred_list = net(imgs)
            temp_loss, temp_loss_list = compute_loss(criterion, pred_list, true_masks, net)
            loss += temp_loss
            loss_list += temp_loss_list
            # preds = torch.sigmoid(masks_pred)
            # preds = (preds>0.5)
            preds = F.softmax(pred_list[branch],dim=1)
            preds = torch.argmax(preds, dim=1).squeeze(1)
            masks = true_masks.view(-1)
            preds = preds.view(-1)
            metrics.add(preds, masks)
    # miou = metrics.iou(average=False).cpu().numpy()
    # miou = np.reshape(miou,[1,-1])
    # return miou, loss/length
    cm = metrics._confusion_matrix
    # print(dist.get_rank(), 'loss:', loss/counter, 'length:',counter, 'pixels:', pixels, 'img shape:', masks_pred.shape, 'cm.sum:', cm.sum())
    torch.distributed.reduce(cm, 0)         # op=torch.distributed.ReduceOp.SUM)
    torch.distributed.reduce(loss, 0)       # op=torch.distributed.ReduceOp.SUM)
    torch.distributed.reduce(loss_list, 0)  # op=torch.distributed.ReduceOp.SUM)

    return cm, loss, loss_list

def train_net(net, train_dataset, val_dataset, epochs, batch_size, lr, \
              model, dir_checkpoint, loss_fn, img_size, classes, save_name, branches=5):
    wandb.init(
          # Set the project where this run will be logged
          project="N-JetNet", 
          # We pass a run name (otherwise it’ll be randomly assigned, like sunshine-lollypop-10)
          name=f"iridis_5", 
          # Track hyperparameters and run metadata
          config={
          "learning_rate": lr,
          "architecture": "N-JetNet(sigma constrained)",
          "dataset": "BCSS",
          "epochs": epochs,
          })

    ETA = np.ones([1,branches])/branches
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
    train_h_loss = np.empty([0,branches])
    val_h_loss = np.empty([0,branches])
    train_iou_list = np.empty([0,classes])
    val_iou_list  = np.empty([0,classes])

    global_step = 0
    if dist.get_rank()==0:
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
        e_start=time.time()
        net.train()
        train_sampler.set_epoch(epoch)
        for batch in train_loader:
            imgs = batch['image'].cuda() #to(device=device, dtype=torch.float32))
            true_masks = batch['mask'].cuda() #to(device=device, dtype=torch.long))
            true_masks = torch.argmax(true_masks, dim=1)

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

        # print('----------------',train_cm.sum(), val_cm.sum(),'----------------')

        # torch.distributed.reduce(train_cm, 0, op=dist.ReduceOp.SUM)#op=torch.distributed.ReduceOp.SUM)
        # torch.distributed.reduce(train_loss, 0, op=dist.ReduceOp.SUM)# op=torch.distributed.ReduceOp.SUM)
        # torch.distributed.reduce(val_cm, 0, op=dist.ReduceOp.SUM)#op=torch.distributed.ReduceOp.SUM)
        # torch.distributed.reduce(val_loss, 0, op=dist.ReduceOp.SUM)# op=torch.distributed.ReduceOp.SUM)
        
        if dist.get_rank()==0:
            # for n, p in net.named_parameters():
            # # if 'scales' in n or 'sigma' in n:
            #     if 'eta' in n:
            #         print(n, p.shape)
            #     if 'scale' in n:
            #         print(n, p)
                    
            # print('----------------',train_cm.sum(), val_cm.sum(), train_pixels, val_pixels, '----------------')
            train_miou = iou(train_cm, False)
            val_miou   = iou(val_cm, False)
            train_loss = train_loss.item()/(n_train*img_size[0]*img_size[1])
            val_loss = val_loss.item()/(n_val*img_size[0]*img_size[1])
            train_hidden_loss = train_hidden_loss/(n_train*img_size[0]*img_size[1])
            val_hidden_loss   = val_hidden_loss/(n_val*img_size[0]*img_size[1])

            val_metrics   = {"val/val_loss": val_loss, "val/val_miou": val_miou.mean()}
            train_metrics = {"train/train_loss": train_loss, "train/train_miou": train_miou.mean()}
            wandb.log({**train_metrics, **val_metrics})

            e_end=time.time()
            print(f'Epoch:{epoch+1}/{epochs}, time:{round(e_end-e_start, 1)},\
                    Train_Loss:, {round(train_loss,4)}, Test_Loss: {round(val_loss,4)}, \
                    Train_mIoU:, {round(train_miou.mean(),4)}, Test_mIoU: {round(val_miou.mean(),4)}')
            eta = F.softmax(net.module.eta.view(-1), dim=0)
            branch = eta.argmax()
            print('eta:', eta.detach().cpu().numpy(), 'max branch:', branch)

            # print(f'train iou: {train_miou}, test iou: {val_miou}')
            train_h_loss = np.concatenate([train_h_loss, train_hidden_loss.cpu().numpy()], axis=0)
            train_loss_list.append(train_loss)
            val_h_loss  = np.concatenate([val_h_loss, val_hidden_loss.cpu().numpy()], axis=0)
            val_loss_list.append(val_loss)

            train_iou_list=np.concatenate([train_iou_list, train_miou], axis=0)
            val_iou_list=np.concatenate([val_iou_list, val_miou], axis=0)
            ETA = np.concatenate([ETA, F.softmax(net.module.eta.view(-1), dim=0).view(1,branches).cpu().detach().numpy()], axis=0)

            if val_miou.mean()>best_miou:
                best_miou = val_miou.mean()
                torch.save(net.state_dict(), dir_checkpoint + f'{save_name}.pth')
                logging.info(f'Checkpoint {epoch + 1} saved !')  
    
    wandb.finish()

    if dist.get_rank()==0:    
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
    parser.add_argument('-l', '--learning-rate', metavar='LR', type=float, nargs='?', default=0.001,
                        help='Learning rate', dest='lr')
    parser.add_argument('-b', '--batch_size', dest='batch_size', type=int, default=3,
                        help='batch size')
    parser.add_argument('-m', '--model', dest='model', type=str, default='unet',
                        help='model')
    parser.add_argument('-d', '--data', dest='data', type=str, default='BCSS',
                        help='dataset')
    parser.add_argument('-s', '--srf', dest='srf', type=str, default='srf',
                        help='srf')
    parser.add_argument('-f', '--factor', dest='factor', type=float, default=0.25,
                        help='factor')
    parser.add_argument('-a', '--share_alpha', dest='share_alpha', type=str, default='True',
                        help='share_alpha')
    parser.add_argument('-c', '--constraint_sigma', dest='constraint_sigma', type=str, default='True',
                        help='constraint_sigma')
    parser.add_argument('--local_rank', default=-1, type=int,
                        help='node rank for distributed training')
    return parser.parse_args()

def count_your_model(model, x, y):
    # your rule here
    pass
    
if __name__ == '__main__':
    torch.manual_seed(43)
    random.seed(43)
    tracemalloc.start()

    classes = 5
    img_size= 512

    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    args = get_args()
    # os.environ["CUDA_VISIBLE_DEVICES"] = str(args.n_gpu)
    # device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    dist.init_process_group(backend='nccl')
    torch.cuda.set_device(args.local_rank)
    
    dataset = args.data
    dir_checkpoint = 'checkpoints/'+dataset+'_branch/'
    # if not os.path.exists(dir_checkpoint):
    #     os.makedirs(dir_checkpoint)
 
    if args.srf=='srf':
        srf=True
        SRF='SRF'
    else:
        srf=False
        SRF='baseline'
    if args.constraint_sigma=='True':
        args.constraint_sigma=True
    else:
        args.constraint_sigma=False

    if args.share_alpha=='True':
        args.share_alpha=True
    else:
        args.share_alpha=False

    if args.factor==0:
        args.factor = [1,2,3,4]
        img_size = 384
    else:
        img_size = int(img_size*args.factor)

    train_dataset = BCSS('train', sample_weight=None, mask_channel=5, factor=args.factor)
    test_dataset  = BCSS('test', sample_weight=None, mask_channel=5,  factor=args.factor)

    net = UNet(n_channels=3, n_classes=classes, filters=60, bilinear=True, srf=srf, 
               split=True, share_alpha=args.share_alpha).cuda()
    net = torch.nn.parallel.DistributedDataParallel(net, device_ids=[args.local_rank])
    
    if dist.get_rank()==0:
        summary(net, (3, img_size, img_size))

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
                    SRF+'_'+str(args.factor))
    # snapshot = tracemalloc.take_snapshot()
    # top_stats = snapshot.statistics('lineno')

    # print("[ Top 10 ]")
    # for stat in top_stats[:10]:
        # print(stat)
    # predict_img(net, val_dataset, device)
