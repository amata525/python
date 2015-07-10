# coding:utf-8

import numpy as np

a = np.random.randn(100)

# aはnumpy配列でなくてはならない
print np.average(a) #平均
print np.var(a) #分散
print np.mean(a) #中間値
print np.median(a) #最頻値
print np.max(a) # 最大値
print np.min(a) # 最小値
