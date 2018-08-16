#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' tensorflow学习处理蓝球 '

__author__ = 'fslong'
__version__ = '0.0.1'
import numpy, json
import tensorflow
from matplotlib import pyplot


# 定义激励层函数：
def add_layer(inputs, in_size, out_size, activation_function=None):
    # 使用在最小值最大值范围内随机初始化一个weights：
    weights = tensorflow.Variable(
        tensorflow.random_normal([in_size, out_size]))
    # 给0向量加0.1生成一个biases：
    biases = tensorflow.Variable(tensorflow.zeros([1, out_size]) + 0.1)
    # 定义未激活的神经网络：
    Wx_plus_b = tensorflow.matmul(inputs,
                                  weights) + biases  # y=x*weights+biases
    # 如果没设置激励函数。输出值直接就是预测值，如果定义了激励函数，使用激励函数对输出值进行处理，然后得到预测值
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs


with open('udseqq.json', 'r', encoding='utf-8') as f:
    udseqq = json.load(f)
x = range(200)
y = []
for i in udseqq:    
    y.append(float(i['blue']))
            

# 生成一个线性的数据序列：
x_data = numpy.array(x)[:, numpy.newaxis]  # 使用numpy.newaxis给x_data增加了维度
print(x_data)
# 随机生成一个后缀：
y_data = numpy.array(y[-200:])[:, numpy.newaxis]
print(y_data)
# 定义传递参数用的变量，None表示传入有多少都可以，1表示传入参数的特征只有1个:
xs = tensorflow.placeholder(tensorflow.float32, [None, 1])
ys = tensorflow.placeholder(tensorflow.float32, [None, 1])
# 开始搭建神经网络：
# 输入层，使用relu作为激励函数,使用xs传入参数：
in1 = add_layer(xs, 1, 200, activation_function=tensorflow.nn.relu)
# 输出层。直接输出预测值就行，所以不需要激励函数：
prediction = add_layer(in1, 200, 1, activation_function=None)
# 计算误差，同样的也需要ys来把结果作为参数传入：
loss = tensorflow.reduce_mean(
    tensorflow.reduce_sum(
        tensorflow.square(ys - prediction), reduction_indices=[1]))

# 使用tensorflow.train.GradientDescentOptimizer().minimize()来最小化loss的误差，从而提供准确率：
train_step = tensorflow.train.GradientDescentOptimizer(16).minimize(loss)

# 初始化之前定义的所有变量：
init = tensorflow.global_variables_initializer()
# 定义session来执行init：
sess = tensorflow.Session()
sess.run(init)
# 创建图像：
fig = pyplot.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(x_data, y_data)  # 散点图
pyplot.axis([-1, 201, 0, 17])  # 设置横纵坐标
pyplot.ion()
pyplot.show()
lines = ax.plot(0, 0, 'r-', lw=5)
for i in range(1001):
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    if i % 20 == 0:
        #print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))
        #print(sess.run(prediction, feed_dict={xs: x_data, ys: y_data}))
        if 'lines' in locals().keys():
            ax.lines.remove(lines[0])
        prediction_value = sess.run(prediction, feed_dict={xs: x_data})
        lines = ax.plot(x_data, prediction_value, 'r-', lw=5)
        pyplot.pause(0.1)

pyplot.ioff()
pyplot.show()