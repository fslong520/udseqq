#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' pytorch学习 '

__author__ = 'fslong'
__version__ = '0.0.1'

import torch
import numpy
np_data = numpy.arange(6).reshape(3, 2)
torch_data = torch.from_numpy(np_data)
tensor2array = torch_data.numpy()
print(
    '\nnumpy array:',
    np_data,
    '\nnumpy tensor:',
    torch_data,
    '\ntensor to array:',
    tensor2array,
)