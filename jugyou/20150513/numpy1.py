# coding: utf-8

import numpy as np

a = np.array([1,2,3])
print a

b = np.arange(5)
print b

c = np.arange(3,9,2) # 開始，終了，ステップ幅
print c

d = np.linspace(0,8,7) #開始，終了，分割数
print d

e = np.eye(3) # 単位行列
print e

f = np.zeros(10) # ゼロベクトル
print f

g = np.zeros((2,3)) #ゼロ行列
print g
