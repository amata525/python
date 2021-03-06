#coding:utf-8

# 二分法のプログラム

from sympy import *

# 関数定義
x = Symbol('x')
y = 3.0 * atan(x-1.0) + x / 4.0

# 初期値設定
a = -3.0
b = 3.0
c = 0.0;

for count in range(1000):

    c = (a + b) / 2
    print count, ':', c

    A = y.subs( [(x, a)] )
    B = y.subs( [(x, b)] )
    C = y.subs( [(x, c)] )

    if A*C <= 0.0:
        b = c
    else:
        a = c
