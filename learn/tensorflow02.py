
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' tensorflow学习 '

__author__ = 'fslong'
__version__ = '0.0.1'
import numpy
import tensorflow

# 创建两个matrixes：
matrix1 = tensorflow.constant([[3, 3]])
matrix2 = tensorflow.constant([[2], [2]])
product = tensorflow.matmul(matrix1, matrix2)
# produck不会直接计算结果，还要用Session来run结果
print('方法一：')
sess=tensorflow.Session()
result=sess.run(product)
print(result)
sess.close()
print('方法二：')
with tensorflow.Session() as sess:
    result2=sess.run(product)
    print(result2)