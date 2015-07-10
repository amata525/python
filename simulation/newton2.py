# #coding:utf-8
# ニュートン法

import sympy as sym
from sympy.plotting import plot
from math import *


# 関数定義
x = sym.Symbol('x')
y = 3.0 * sym.atan(x-1.0) + x / 4.0
dy = sym.diff(y, x)

# 初期値設定
a = [3.0]
t = 0
s = 0

dif = 0.00000000000001

while(fabs(y.subs( [(x, a[t])] )) > dif):
    s = a[t] - y.subs( [(x, a[t])] ) / dy.subs( [(x, a[t])] )
    t += 1
    a.append(s)

    print s, y.subs( [(x, s)])

    if t >= 100 :
        break

plot(y, (x,-20, 20))
