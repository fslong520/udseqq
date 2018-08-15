#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' tensorflow学习 '

__author__ = 'fslong'
__version__ = '0.0.1'
import numpy
import tensorflow

# 定义暂时存储数据的变量:
input1=tensorflow.placeholder(tensorflow.float64)
input2=tensorflow.placeholder(tensorflow.float64)
# 乘法运算:
output=tensorflow.multiply(input1,input2)

with tensorflow.Session()as sess:
    print(sess.run(output,feed_dict={input1:[7.],input2:[2.]}))