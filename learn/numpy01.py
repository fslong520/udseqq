#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' numpy学习 '

__author__ = 'fslong'
__version__ = '0.0.1'

import time

import numpy


# 使用numpy创建矩阵
def class1():
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


# numpy基础运算：
def class2():
    a = numpy.array([10, 20, 30, 40])
    b = numpy.arange(4)
    print('\n\n矩阵元素的加减乘：\n')
    print('a=', a)
    print('b=', b)
    print('a-b=', a - b)
    print('a+b=', a + b)
    print('a*b=', a * b)
    print('a**2=', a**2)
    print('\n\n矩阵维度的重设\n')
    a = a.reshape([2, 2])
    b = b.reshape((2, 2))
    print('a.reshape([2, 2]):\n', a)
    print('b.reshape((2, 2)):\n', b)
    print('\n\n矩阵相乘：\n')
    print('numpy.dot(a,b):\n', numpy.dot(a, b))
    print('a.dot(b):\n', a.dot(b))
    print('\n\n随机生成矩阵:\n')
    a = 5 * numpy.random.random((3, 4))
    print('5 * numpy.random.random((3, 4)):\n', a)
    b = 15 * numpy.random.random((5, 4))
    print('15 * numpy.random.random((2, 4)):\n', b)
    print('\n\n按需计算最小值最大值以及数学函数:\n')
    print('numpy.max(a):\n', numpy.max(a))
    print('numpy.min(a):\n', numpy.min(a))
    print('numpy.cos(a):\n', numpy.cos(a))
    print('按列计算用numpy.max(a, axis=0):\n', numpy.max(a, axis=0))
    print('按行计算用numpy.max(a, axis=1):\n', numpy.max(a, axis=1))
    print('\n\n 个人理解numpy.array()的索引是从左往右一行一行的线性的，如果是三维那就再加一面一面。')
    print('\n\n 最大值的索引: \n')
    print('numpy.argmax(a)=', numpy.argmax(a))
    print('\n\n 最小值的索引: \n')
    print('numpy.argmin(a)=', numpy.argmin(a))
    print('\n\n 可以使用num.mean()或者num.average()求平均值: \n')
    print('numpy.average(a)=', numpy.average(a))
    print('numpy.mean(a)=', numpy.mean(a))
    print('a.mean()=', a.mean())
    print('\n\n 可以使用num.median()求中位数: \n')
    print('numpy.median(a)=', numpy.median(a))
    print('\n\n 累加: \n')
    print('numpy.cumsum(a):\n', numpy.cumsum(a))
    print('\n\n 累差: \n')
    print('numpy.diff(a):\n', numpy.diff(a))
    print('\n\n 将所有非零元素的行与列坐标分割开: \n')
    print('numpy.nonzero(a):\n', numpy.nonzero(a))
    print('\n\n 排序: \n')
    print('numpy.sort(a):\n', numpy.sort(a))
    print('\n\n 两种转置: \n')
    print('numpy.transpose(a):\n', numpy.transpose(a))
    print('a.T:\n', a.T)
    print('\n\n使用clip可以设置最大值与最小值，如果元素不在范围内，就直接变成这个数:\nnumpy.clip(a,0,3):\n',
          numpy.clip(a,0,3))


if __name__ == '__main__':
    start = time.time()
    class1()
    end = time.time()
    print('------------分隔符------------\n')
    print('class1执行完毕，总共执行的时间：%s\n' % (end - start))
    print('------------分隔符------------\n')
    start = time.time()
    class2()
    end = time.time()
    print('------------分隔符------------\n')
    print('class2总共执行的时间：%s\n' % (end - start))
    print('------------分隔符------------\n')
