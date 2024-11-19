import torch
import torch.nn as nn
import torch.nn.functional as F
import ebayesthresh

class ebayesthresh_nn(torch.nn.Module):
    
    def __init__(self):
        super().__init__()
       
    def forward(self,input,prior="laplace", a = 0.5, bayesfac = False, sdev = None, verbose = False, threshrule = "median", universalthresh = True, stabadjustment = None):
        self.prior = prior
        self.a = a
        self.bayesfac = bayesfac
        self.sdev = sdev
        self.verbose = verbose
        self.threshrule = threshrule
        self.universalthresh = universalthresh
        self.stabadjustment = stabadjustment

        return ebayesthresh.ebayesthresh(input,self.prior, a=self.a, bayesfac=self.bayesfac, sdev=self.sdev, verbose=self.verbose, threshrule=self.threshrule, universalthresh=self.universalthresh, stabadjustment=self.stabadjustment)