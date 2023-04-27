import torch.nn as nn
import math
import torch.nn.functional as F

__all__ = ['nin']

class NiN(nn.Module):
    def __init__(self,
                num_classes):

        super(NiN, self).__init__()
        self.classifier = nn.Sequential(
                nn.Conv2d(3, 192, kernel_size=5, stride=1, padding=2, \
                        bias=False),
                nn.BatchNorm2d(192),
                nn.ReLU(inplace=True),

                nn.Conv2d(192, 160, kernel_size=1, stride=1, padding=0, \
                        bias=False),
                nn.BatchNorm2d(160),
                nn.ReLU(inplace=True),

                nn.Conv2d(160,  96, kernel_size=1, stride=1, padding=0, \
                        bias=False),
                nn.BatchNorm2d(96),
                nn.ReLU(inplace=True),

                nn.MaxPool2d(kernel_size=3, stride=2, padding=1),
                nn.Dropout(0.5),

                nn.Conv2d(96, 192, kernel_size=5, stride=1, padding=2, \
                        bias=False),
                nn.BatchNorm2d(192),
                nn.ReLU(inplace=True),

                nn.Conv2d(192, 192, kernel_size=1, stride=1, padding=0, \
                        bias=False),
                nn.BatchNorm2d(192),
                nn.ReLU(inplace=True),

                nn.Conv2d(192, 192, kernel_size=1, stride=1, padding=0, \
                        bias=False),
                nn.BatchNorm2d(192),
                nn.ReLU(inplace=True),
                nn.AvgPool2d(kernel_size=3, stride=2, padding=1),
                nn.Dropout(0.5),

                nn.Conv2d(192, 192, kernel_size=3, stride=1, padding=1, \
                        bias=False),
                nn.BatchNorm2d(192),
                nn.ReLU(inplace=True),

                nn.Conv2d(192, 192, kernel_size=1, stride=1, padding=0, \
                        bias=False),
                nn.BatchNorm2d(192),
                nn.ReLU(inplace=True),

                nn.Conv2d(192, num_classes, kernel_size=1, stride=1, \
                        padding=0, bias=False),
                nn.BatchNorm2d(num_classes),
                nn.ReLU(inplace=True),
                nn.AvgPool2d(kernel_size=8, stride=1, padding=0)
                ) 
        self.num_classes = num_classes
        self.extra_reg = 0

    def forward(self, x):
        x = self.classifier(x)
        x = x.view(x.size(0), self.num_classes)
        return x

def nin(**kwargs):
    """
    Constructs a standard NiN (M. Lin et. al., ICLR 2014).
    """
    return NiN(**kwargs)

