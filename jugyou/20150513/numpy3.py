# coding: utf-8

import numpy as np

# 演算
a = np.array([1,2,3])

print a + 2 #aの各要素に2を加算
print a * 3 #aの各要素に3を乗算

print np.log(a) #aの各要素の自然対数
print a.astype(int) #aの各要素をint型にする

a.flat = 110 #aの各要素をすべて110にする
print a

#型変換
b = np.zeros(5)
print b

c = b.tolist() #bをpython標準のリスト型に変換
print c

d = np.array(c) #cをnumpyの配列に変換
print d
