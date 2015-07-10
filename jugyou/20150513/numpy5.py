# coding:utf-8

import numpy as np

a = np.random.randint(0,10,32)
print a

# 1次元配列
print a[3:5] # 3~5-1番目の要素
print a[:5]  # 最初~5-1番目の要素
print a[3:]  # 3~最後の要素
print a[:]   # 全要素
print a[3:9:2] #aの3,5,7番目の要素

b = np.random.randint(0,10,(5,5))
print b

#多次元配列
print b[3,4] #3目４列目の要素
print b[:,4] #４列目の要素全部
