from __future__ import print_function

import argparse
import os
import shutil
import time
import random

import torch
import torch.nn as nn
import torch.nn.parallel
import torch.backends.cudnn as cudnn
import torch.optim as optim

from pytorch_classification.train_and_test import *
from pytorch_classification.dataset import *
import models as models

# For tensorboard
from torch.utils.tensorboard import SummaryWriter
import torchvision

# Load the model names
model_names = sorted(name for name in models.__dict__
    if name.islower() and not name.startswith("__")
    and callable(models.__dict__[name]))

parser = argparse.ArgumentParser()

# N-Jet options
parser.add_argument('--srf-init-k', default=2.0, type=float,
                    help='spatial extent of the filters')
parser.add_argument('--srf-init-scale', default=0.0, type=float,
                    help='the initial scale, if not learned')
parser.add_argument('--srf-init-order', default=4.0, type=float,
                    help='the order of the approximation')
parser.add_argument('--srf-learn-sigma', action='store_true', default=True,
                    help='If the scale/sigma are fixed or learned.')

# Optimization options
parser.add_argument('--epochs', default=90, type=int,
                    help='The number of epochs.')
parser.add_argument('--start-epoch', default=0, type=int,
                    help='Epoch for restarting runs.')
parser.add_argument('--schedule', type=int, nargs='+', default=[30, 60],
                    help='Epoch at which the learning rate decreases.')
parser.add_argument('--lr', default=0.1, type=float,
                    help='Initial learning rate.')
parser.add_argument('--train-batch', default=128, type=int,
                    help='Training batch size.')
parser.add_argument('--test-batch', default=100, type=int,
                    help='Test batch size.')
parser.add_argument('--momentum', default=0.9, type=float,
                    help='Optimizer momentum.')
parser.add_argument('--weight-decay', '--wd', default=5e-4, type=float,
                    help='Weight regularization.')
parser.add_argument('--optim', default='sgd', type=str,
                    help='The optimizer.')
parser.add_argument('--gamma', type=float, default=0.1,                         
                    help='LR is multiplied by gamma on schedule.')                               
                    
# Checkpoints
parser.add_argument('--checkpoint', default='checkpoints', type=str,
                    help='Path where to save the checkpoint.')
parser.add_argument('--resume', default='', type=str,
                    help='Path to load the checkpoint.')
# Architecture and data
parser.add_argument('--dataset', default='cifar10', type=str,
                    help='The name of the dataset.')
parser.add_argument('--arch', default='nin', choices=model_names,
                    help='Model architecture: ' +
                        ' | '.join(model_names) + ' (default: nin)')
# Seed
parser.add_argument('--manualSeed', type=int, default=0, help='Manual seed')
parser.add_argument('--evaluate', action='store_true',
                    help='Only evaluate the model.')
parser.add_argument('--workers', default=4, type=int,
                    help='The number of data loading workers.')


args = parser.parse_args()
state = {k: v for k, v in args._get_kwargs()}
assert args.dataset == 'cifar10' or args.dataset == 'cifar100',\
        'Dataset can only be cifar10 or cifar100.'

# Use CUDA
use_cuda = torch.cuda.is_available()

# Random seed
if args.manualSeed is None:
    args.manualSeed = random.randint(1, 10000)
random.seed(args.manualSeed)
torch.manual_seed(args.manualSeed)
if use_cuda:
    torch.cuda.manual_seed_all(args.manualSeed)

""" Save the checkpoint """
def save_checkpoint(state, is_best, checkpoint='checkpoint', filename='checkpoint.pth.tar'):
    filepath = os.path.join(checkpoint, filename)
    torch.save(state, filepath)
    if is_best:
        shutil.copyfile(filepath, os.path.join(checkpoint, 'model_best.pth.tar'))

""" Adjust the learning rate at the wanted epochs """
def adjust_learning_rate(optimizer, epoch):
    global state
    if epoch in args.schedule:
        state['lr'] *= args.gamma
        for param_group in optimizer.param_groups:
            param_group['lr'] = state['lr']


""" The main training loop. """
def main():
    start_epoch = args.start_epoch  

    if not os.path.isdir(args.checkpoint):
        os.mkdir(os.path.normpath(args.checkpoint))

    # For tensorboard
    writer = SummaryWriter(args.checkpoint)

    # Create data splits:
    trainset = dataCIFAR(args.dataset, args.train_batch, train=True, val=False, 
                        workers=args.workers)
    valset = dataCIFAR(args.dataset, args.train_batch, train=True, val=True, 
                        workers=args.workers)
    testset = dataCIFAR(args.dataset, args.test_batch, train=False, val=False, 
                        workers=args.workers)

    # Loading the model
    if args.arch.endswith('nin'):
        model = models.__dict__[args.arch](
                    num_classes=trainset.num_classes)
    elif args.arch.endswith('nin_shared_srf'):
        model = models.__dict__[args.arch](
                    num_classes=trainset.num_classes,
                    init_k=args.srf_init_k, 
                    init_order=args.srf_init_order, 
                    init_scale=args.srf_init_scale, 
                    learn_sigma=args.srf_learn_sigma,
                    use_cuda=use_cuda)
    else:
        print("Model not implemented")

    # Get model summary to list the number of parameters. 
    summary(model, input_size=(1, 3, 32, 32))
    model = torch.nn.DataParallel(model)
    if use_cuda:
        model = model.cuda()
        cudnn.benchmark = True    

    # Define the criterion and the optimizer
    criterion = nn.CrossEntropyLoss()
    if args.optim.endswith('sgd'):
        optimizer = optim.SGD(model.parameters(), lr=args.lr, 
                            momentum=args.momentum, 
                            weight_decay=args.weight_decay)
    elif args.optim.endswith('adam'):
        optimizer = optim.Adam(model.parameters(), lr=args.lr, 
                            weight_decay=args.weight_decay)

    # Resume the training from he checkpoint
    title = args.dataset + args.arch
    if args.resume:
        print('==> Resuming from checkpoint..', args.resume)
        assert os.path.isfile(args.resume), 'Error: no checkpoint directory found!'
        args.checkpoint = os.path.dirname(args.resume)
        checkpoint = torch.load(args.resume)
        best_acc = checkpoint['best_acc']
        start_epoch = checkpoint['epoch']
        model.load_state_dict(checkpoint['state_dict'])
        optimizer.load_state_dict(checkpoint['optimizer'])


    # If we only want to evaluate a pretrained model
    if args.evaluate:
        print('\nEvaluation only')
        test_loss, test_acc = test(testset, model, criterion, start_epoch, use_cuda)
        print(' Test Loss:  %.8f, Test Acc:  %.2f' % (test_loss, test_acc))
        return
    
    # Train and validation
    best_acc = 0  
    for epoch in range(start_epoch, args.epochs):
        adjust_learning_rate(optimizer, epoch)

        print('\nEpoch: [%d | %d] LR: %f' % (epoch + 1, args.epochs, state['lr']))
        train_loss, train_acc = train(trainset, model, criterion, optimizer, epoch, use_cuda, writer, args)
        val_loss, val_acc = test(valset, model, criterion, epoch, use_cuda, args)
        
        # Logging the data
        writer.add_scalar("Train/Loss", train_loss, epoch)
        writer.add_scalar("Val/Loss", val_loss, epoch)
        writer.add_scalar("Train/acc", train_acc, epoch)
        writer.add_scalar("Val/acc", val_acc, epoch)

        # Saving model
        is_best = val_acc > best_acc
        best_acc = max(val_acc, best_acc)
        save_checkpoint({
                'epoch': epoch + 1,
                'state_dict': model.state_dict(),
                'acc': val_acc,
                'best_acc': best_acc,
                'optimizer' : optimizer.state_dict(),
            }, is_best, checkpoint=args.checkpoint)
        
    test_loss, test_acc = test(testset, model, criterion, start_epoch, use_cuda, args)
    print(' Final test loss:  %.8f, test Acc:  %.2f' % (test_loss, test_acc))

    writer.flush()
    writer.close()

if __name__ == '__main__':
    main()
