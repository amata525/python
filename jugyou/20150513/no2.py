#coding : utf-8

import numpy as np

a = np.array([1,2,3])

print a * 2

b = a.tolist()
b = b * 2
print b

a = np.array(b)
print a * 2
