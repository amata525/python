# #coding:utf-8
# ニュートン法

from sympy import *

# 関数定義
x = Symbol('x')
y = x**2 - 2
dy = diff(y, x)

# 初期値設定
a = [2.0]
t = 0
s = 0

dif = 0.00000000000001

while(y.subs( [(x, a[t])] ) > dif):
    s = a[t] - y.subs( [(x, a[t])] ) / dy.subs( [(x, a[t])] )
    t += 1
    a.append(s)

    print s, y.subs( [(x, s)])
