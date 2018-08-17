#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' tensorflow学习 '

__author__ = 'fslong'
__version__ = '0.0.1'
import numpy
import tensorflow
from matplotlib import pyplot

x_data = numpy.linspace(-1, 1, 300, dtype=numpy.float32)[:, numpy.newaxis]
noise = numpy.random.normal(0, 0.05, x_data.shape).astype(numpy.float32)
y_data = numpy.square(x_data) - 0.5 + noise + 3 * x_data
# 搭建图纸:
with tensorflow.name_scope('inputs'):
    xs = tensorflow.placeholder(tensorflow.float32, [None, 1], name='x_in')
    ys = tensorflow.placeholder(tensorflow.float32, [None, 1], name='y_in')


def add_layer(inputs, in_size, out_size, n_layer, activation_function=None):
    layer_name = 'layer%s' % n_layer
    with tensorflow.name_scope('layer'):
        with tensorflow.name_scope('weights'):
            weights = tensorflow.Variable(
                tensorflow.random_normal([in_size, out_size]), name='W')
            tensorflow.summary.histogram(layer_name + '/weights', weights)
        with tensorflow.name_scope('biases'):
            biases = tensorflow.Variable(
                tensorflow.zeros([1, out_size]) + 0.1, name='b')
            tensorflow.summary.histogram(layer_name + '/biases', biases)

        with tensorflow.name_scope('Wx_plus_b'):
            Wx_plus_b = tensorflow.add(
                tensorflow.matmul(inputs, weights), biases)
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
        tensorflow.summary.histogram(layer_name + '/outputs', outputs)
    return outputs


in1 = add_layer(xs, 1, 10, n_layer=1, activation_function=tensorflow.nn.relu)
prediction = add_layer(in1, 10, 1, n_layer=2, activation_function=None)

with tensorflow.name_scope('loss'):
    loss = tensorflow.reduce_mean(
        tensorflow.reduce_sum(
            tensorflow.square(ys - prediction), reduction_indices=[1]))
    tensorflow.summary.scalar('loss', loss)
# 合并所有的训练图
sess = tensorflow.Session()
merged = tensorflow.summary.merge_all()
writer = tensorflow.summary.FileWriter('logs/', sess.graph)
sess.run(tensorflow.global_variables_initializer())
# 训练数据：
with tensorflow.name_scope('train'):
    train_step = tensorflow.train.GradientDescentOptimizer(0.1).minimize(loss)
# 创建图像：
fig = pyplot.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(x_data, y_data)  # 散点图
pyplot.ion()
pyplot.show()
lines = ax.plot(0, 0, 'r-', lw=1)

for i in range(1000):
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    if i % 50 == 0:
        rs = sess.run(merged, feed_dict={xs: x_data, ys: y_data})
        writer.add_summary(rs, i)
        if 'lines' in locals().keys():
            ax.lines.remove(lines[0])
        prediction_value = sess.run(prediction, feed_dict={xs: x_data})
        lines = ax.plot(x_data, prediction_value, 'r-', lw=1)
        pyplot.pause(0.1)

pyplot.ioff()
pyplot.show()