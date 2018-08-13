#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' numpy学习 '

__author__ = 'fslong'
__version__ = '0.0.1'

import time

import numpy

if __name__ == '__main__':
    start=time.time()
    array = numpy.array([[1, 2, 3], ['a', 'b', 'c']])
    print('矩阵内容：\n', array)
    print('矩阵的维度：', array.ndim)
    print('矩阵的行列数：', array.shape)
    print('矩阵元素个数：', array.size)
    '''
    array：创建数组
    dtype：指定数据类型
    zeros：创建数据全为0
    ones：创建数据全为1
    empty：创建数据接近0
    arange：按指定范围创建数据
    linspace：创建线段
    '''
    array = numpy.array([1, 2, 3], dtype=int)
    print(array.dtype)
    print('\n')
    array = numpy.zeros([3, 4])  # 3行4列的0矩阵
    print('\n')
    print(array)
    array = numpy.ones([3, 4])  # 3行4列的1矩阵
    print('\n')
    print(array)
    array = numpy.empty([3, 4])  # 3行4列的元素接近于0矩阵
    print('\n')
    print(array)
    array = numpy.arange(0, 12, 1).reshape(
        (3, 4))  # 用0-12的数创建3行4列的矩阵，数字数量必须和矩阵元素数对上，不包含stop的那个数
    print('\n')
    print(array)
    array = numpy.linspace(0, 20, 20).reshape((5, 4))
    print('\n')
    print(array)
    end=time.time()
    print('总共执行的时间：%s'%(end-start))
    #input()
