#coding:utf-8

import numpy as np

# 多次元配列の演算

a = np.array([1,2])
b = np.array([5,6])

print a + b #各要素の和
print a * b #各要素の積

print np.dot(a,b) #内積
print np.cross(a,b) #外積

# 乱数
print np.random.rand(10) #0~1の一様乱数
print np.random.rand(2,3)
print np.random.randn(2,3) #標準正規分布に従う乱数
print np.random.randint(0,10,(2,3)) #0以上10未満の整数からなる乱数
