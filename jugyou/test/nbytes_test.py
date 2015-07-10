# coding:utf-8

import numpy as np

a = np.array([1,2,3])
b = np.linspace(0,8,5)
c = np.eye(3)
d = np.zeros(10)

print a.dtype, a.shape, a.size, a.nbytes
print b.dtype, b.shape, b.size, b.nbytes
print c.dtype, c.shape, c.size, c.nbytes
print d.dtype, d.shape, d.size, d.nbytes

e = [1,2]
print e*2
