#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' tensorflow学习 '

__author__ = 'fslong'
__version__ = '0.0.1'
import numpy as np
import tensorflow as tf

# 初始化测试用数据：
x_data = np.random.rand(100).astype(np.float64)
y_data = x_data * 0.1 + 3

# 搭建模型。其实就是给定y=Weights * x + biases中Weights和biases的范围
weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))
y = weights * x_data + biases
# 计算误差(mean表示平均误差，就是平方差):
loss = tf.reduce_mean(tf.square(y - y_data))
# 传播误差，将误差传播给tensorflow，让他自己去找最小的误差并更新参数：
optimizer = tf.train.GradientDescentOptimizer(0.1)
train = optimizer.minimize(loss)
# 开始训练：
init = tf.global_variables_initializer()
# 新建会话，我们用 Session 来执行 init 初始化步骤. 并且, 用 Session 来 run 每一次 training 的数据. 逐步提升神经网络的预测准确性.：
sess = tf.Session()
# 开始训练：
sess.run(init)
for step in range(2001):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(weights), sess.run(biases))

