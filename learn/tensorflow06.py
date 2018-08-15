#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' tensorflow学习 '

__author__ = 'fslong'
__version__ = '0.0.1'
import numpy
import tensorflow

# 搭建图纸:
with tensorflow.name_scope('inputs'):
    xs = tensorflow.placeholder(tensorflow.float32, [None, 1], name='x_in')
    ys = tensorflow.placeholder(tensorflow.float32, [None, 1], name='y_in')


def add_layer(inputs, in_size, out_size, activation_function=None):
    with tensorflow.name_scope('layer'):
        with tensorflow.name_scope('weights'):
            weights = tensorflow.Variable(
                tensorflow.random_normal([in_size, out_size]), name='w')
        with tensorflow.name_scope('biases'):
            biases = tensorflow.Variable(
                tensorflow.zeros([1, out_size]) + 0.1, name='b')
        with tensorflow.name_scope('Wx_plus_b'):
            Wx_plus_b = tensorflow.add(
                tensorflow.matmul(inputs, weights), biases)
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
    return outputs


# 开始搭建神经网络：
# 输入层，使用relu作为激励函数,使用xs传入参数：
in1 = add_layer(xs, 1, 10, activation_function=tensorflow.nn.relu)
# 输出层。直接输出预测值就行，所以不需要激励函数：
prediction = add_layer(in1, 10, 1, activation_function=None)
# 计算误差，同样的也需要ys来把结果作为参数传入：

with tensorflow.name_scope('loss'):
    loss = tensorflow.reduce_mean(
        tensorflow.reduce_sum(
            tensorflow.square(ys - prediction), reduction_indices=[1]))

with tensorflow.name_scope('train'):
    train_step=tensorflow.train.GradientDescentOptimizer(0.1).minimize(loss)
sess=tensorflow.Session()
writer=tensorflow.summary.FileWriter('logs/',sess.graph)


