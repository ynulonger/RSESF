
import numpy as np
# from sklearn.metrics import confusion_matrix
import torch
import torch.distributed as dist
from torchmetrics import ConfusionMatrix

class Metrics:
    def __init__(self, class_num, ignore_index=set([None])):
        """compute imou for pytorch segementation task
        Args:
            class_num: predicted class number
            ignore_index: ignore index
        """
        self.class_num = class_num
        if self.class_num==1:
            self.class_num=2
        self.ignore_index = ignore_index
        self.CM = ConfusionMatrix(num_classes=self.class_num).cuda()
        self._confusion_matrix = torch.zeros(self.class_num, self.class_num).cuda()
        self._iou_list = torch.empty(1,0).cuda()

    def add(self, preds, gts):
        """update confusion matrix
        Args:
            preds: 1 dimension numpy array, predicted label
            gts: corresponding ground truth for preds, 1 dimension numpy array
        """
        # cm = confusion_matrix(gts, preds, labels=range(self.class_num))
        # print('set of preds:',set(preds.cpu().numpy()),'set of mask:', set(gts.cpu().numpy()))
        # cm = self.CM(preds.to(f'cuda:{dist.get_rank()}'), gts.to(f'cuda:{dist.get_rank()}'))
        cm = self.CM(preds.cuda(), gts.cuda())

        self._confusion_matrix += cm

    def clear(self):
        self._confusion_matrix.fill_(0)

    def precision(self, average=True):

        cm = self._confusion_matrix
        precision = torch.diagonal(cm,0) / (cm.sum(dim=0) + 1e-15)

        if self.ignore_index:
            precision_mask = [i for i in range(self.class_num) if i != self.ignore_index]
            precision = precision[precision_mask]
        if average:
            precision = precision.mean()

        return precision
    
    def accuracy(self):
        cm = self._confusion_matrix
        acc = torch.diagonal(cm,0).sum() / cm.sum()
        return acc

    def recall(self, average=True):

        cm = self._confusion_matrix
        recall = torch.diagonal(cm,0) /(cm.sum(dim=1) + 1e-15)

        if self.ignore_index:
            recall_mask = [i for i in range(self.class_num) if i != self.ignore_index]
            recall = recall[recall_mask]
        if average:
            recall = recall.mean()

        return recall

    def iou(self, average=True):

        cm = self._confusion_matrix
        iou = torch.diagonal(cm, 0) / (cm.sum(dim=1) + cm.sum(dim=0) - torch.diagonal(cm, 0) + 1e-15)
        iou_mask = [i for i in range(self.class_num) if i not in self.ignore_index]
        iou = iou[iou_mask]
        
        if average:
            iou = iou.mean().item()
            return iou
        else:
            return iou

    def append_iou(self, preds, gts):
        N = preds.size()[0]
        for i in range(N):
            idx = gts[i].unique()
            iou_mask = [i for i in idx.cpu().numpy()]

            pred = preds[i].view(-1)
            gt = gts[i].view(-1)
            cm = self.CM(pred, gt)

            iou = torch.diagonal(cm, 0) / (cm.sum(dim=1) + cm.sum(dim=0) - torch.diagonal(cm, 0) + 1e-15)
            iou = iou.view(-1)
            iou = iou[iou_mask]
            miou = iou.mean().view(1,1)
            self._iou_list = torch.cat([self._iou_list, miou], dim=1)

    def append_iou_binary(self, preds, gts):
        N = preds.size()[0]
        for i in range(N):
            pred = preds[i].view(1,-1)
            gt = gts[i].view(1,-1)
            cm = self.CM(pred, gt)

            iou = torch.diagonal(cm, 0) / (cm.sum(dim=1) + cm.sum(dim=0) - torch.diagonal(cm, 0) + 1e-15)
            iou = iou.view(-1)[1].view(1,1)
            self._iou_list = torch.cat([self._iou_list, iou], dim=1)

    def get_img_iou(self, preds, gts):
        # pred_mask = [i for i in range(self.class_num) if i != self.ignore_index]
        # idx = gts.unique()[:-1]
        # print('classes in gt:', idx)
        cm = self.CM(preds, gts)
        # print('confusion matrix:', cm)
        iou = torch.diagonal(cm, 0) / (cm.sum(dim=1) + cm.sum(dim=0) - torch.diagonal(cm, 0) + 1e-15)
        iou = iou.view(-1)
        # print('iou before mask:', iou)
        # iou_mask = [i for i in idx.cpu().numpy()]
        iou_mask = [i for i in range(self.class_num) if i not in self.ignore_index]
        # print(f'iou:{iou}, idx:{idx}')
        iou_1 = iou[iou_mask]
        # print('iou after mask:', iou_1)

        # print(iou, iou_1, iou_1.mean())
        miou = iou_1.mean().item()
        return miou, iou_mask, iou_1

    def dice_coef(self, output, target):#output为预测结果 target为真实结果
        smooth = 1e-15 #防止0除
        intersection = (output * target).sum()
        return (2. * intersection + smooth) / (output.sum() + target.sum() + smooth)

    def multi_dice_coef(self, y_true, y_pred, numLabels):
        dice_0=0
        dice_1=0
        labels = list(y_true.unique().cpu().numpy())
        for index in labels:
            dice_0 += self.dice_coef(y_true==index, y_pred==index)
        for index in labels:
            dice_1 += self.dice_coef(y_true==index, y_pred==index)
        dice_0 = dice_0/numLabels
        dice_1 = dice_1/len(labels)
        # print(f'labels: {labels}, {dice_0},{dice_1}')

        return dice_1 # taking average

def iou(cm, average=True):
    iou = torch.diagonal(cm, 0) / (cm.sum(dim=1) + cm.sum(dim=0) - torch.diagonal(cm, 0) + 1e-15)
    if average:
        iou = iou.mean().item()
        return iou.cpu()
    else:
        return iou.cpu().numpy().reshape([1,-1])