#coding:utf-8
#はさみうち法

from sympy import *

# 関数定義
x = Symbol('x')
y = x**2 - 2

# 初期値設定
a = 0.0
b = 2.0
w = 0.0

for count in range(1000):

    A = y.subs( [(x, a)] )
    B = y.subs( [(x, b)] )

    w = (B*a - A*b) / (B - A)
    print count, ':', w

    W = y.subs( [(x, w)] )

    if A*W >= 0.0:
        a = w
    else:
        b = w
