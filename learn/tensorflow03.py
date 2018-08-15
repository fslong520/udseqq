#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' tensorflow学习 '

__author__ = 'fslong'
__version__ = '0.0.1'
import numpy
import tensorflow

# 定义变量:
state = tensorflow.Variable(0, name='counter')

# 定义常量：
one = tensorflow.constant(1)

# 加法：
new_value = tensorflow.add(state, one)

# 将state更新为new_value：
update = tensorflow.assign(state, new_value)

# 激活变量：
init = tensorflow.global_variables_initializer()
with tensorflow.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))

# state、one、update这些其实是指针（C++运算很多都需要指针，所以在这里页用到了指针)