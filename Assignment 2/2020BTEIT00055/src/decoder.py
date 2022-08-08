 #####################################################################################
 # MIT License                                                                       #
 #                                                                                   #
 # Copyright (C) 2019 Charly Lamothe                                                 #
 # Copyright (C) 2018 Zalando Research                                               #
 #                                                                                   #
 # This file is part of VQ-VAE-images.                                               #
 #                                                                                   #
 #   Permission is hereby granted, free of charge, to any person obtaining a copy    #
 #   of this software and associated documentation files (the "Software"), to deal   #
 #   in the Software without restriction, including without limitation the rights    #
 #   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell       #
 #   copies of the Software, and to permit persons to whom the Software is           #
 #   furnished to do so, subject to the following conditions:                        #
 #                                                                                   #
 #   The above copyright notice and this permission notice shall be included in all  #
 #   copies or substantial portions of the Software.                                 #
 #                                                                                   #
 #   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR      #
 #   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,        #
 #   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE     #
 #   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER          #
 #   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,   #
 #   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE   #
 #   SOFTWARE.                                                                       #
 #####################################################################################

from residual_stack import ResidualStack

import torch.nn as nn
import torch.nn.functional as F


class Decoder(nn.Module):
    
    def __init__(self, in_channels, num_hiddens, num_residual_layers, num_residual_hiddens, use_kaiming_normal=False):
        super(Decoder, self).__init__()
        
        self._conv_1 = nn.Conv2d(
            in_channels=in_channels,
            out_channels=num_hiddens,
            kernel_size=3, 
            stride=1,
            padding=1
        )
        if use_kaiming_normal:
            self._conv_1 = nn.utils.weight_norm(self._conv_1)
            nn.init.kaiming_normal_(self._conv_1.weight)
        
        # Same number of residual layers as specified in the paper
        self._residual_stack = ResidualStack(
            in_channels=num_hiddens,
            num_hiddens=num_hiddens,
            num_residual_layers=num_residual_layers,
            num_residual_hiddens=num_residual_hiddens,
            use_kaiming_normal=use_kaiming_normal
        )
        
        # Same parameters as specified in the paper
        self._conv_trans_1 = nn.ConvTranspose2d(
            in_channels=num_hiddens, 
            out_channels=num_hiddens//2,
            kernel_size=4, 
            stride=2,
            padding=1
        )
        if use_kaiming_normal:
            self._conv_trans_1 = nn.utils.weight_norm(self._conv_trans_1)
            nn.init.kaiming_normal_(self._conv_trans_1.weight)
        
        # Same parameters as specified in the paper
        self._conv_trans_2 = nn.ConvTranspose2d(
            in_channels=num_hiddens//2, 
            out_channels=3,
            kernel_size=4, 
            stride=2,
            padding=1
        )
        if use_kaiming_normal:
            self._conv_trans_2 = nn.utils.weight_norm(self._conv_trans_2)
            nn.init.kaiming_normal_(self._conv_trans_2.weight)

    def forward(self, inputs):
        x = self._conv_1(inputs)
        
        x = self._residual_stack(x)
        
        x = self._conv_trans_1(x)

        x = F.relu(x)
        x = self._conv_trans_2(x)
        
        return x
