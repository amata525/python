# coding: utf-8

import numpy as np

a = np.array([1,2,3])
print a #a自体
print a.dtype #aのデータ型
print a.shape #aの次元
print a.size #aの要素数
print a.nbytes #aのデータのバイト数

b = np.arange(5)
print
print b
print b.dtype
print b.shape
print b.size
print b.nbytes

c = np.arange(3,9,2) # 開始，終了，ステップ幅
print
print c
print c.dtype
print c.shape
print c.size
print c.nbytes

d = np.linspace(0,8,7) #開始，終了，分割数
print
print d
print d.dtype
print d.shape
print d.size
print d.nbytes

e = np.eye(3) # 単位行列
print
print e
print e.dtype
print e.shape
print e.size
print e.nbytes

f = np.zeros(10) # ゼロベクトル
print
print f
print f.dtype
print f.shape
print f.size
print f.nbytes

g = np.zeros((2,3)) #ゼロ行列
print 
print g
print g.dtype
print g.shape
print g.size
print g.nbytes
