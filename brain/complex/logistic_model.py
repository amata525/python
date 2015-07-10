#coding:utf-8

import numpy as np
from pylab import *

# 指数的成長モデルとロジスティック成長モデル

#写像funcで初期値をinitialとしたときの起動を描画
def drawModel(func, initial):
    nList = []
    yList = []

    nList.append(0)
    yList.append(initial)

    for n in range(1, 10):
        nList.append(n)
        yList.append(func(yList[n-1]))

    print nList
    print yList
    plot(nList, yList)


if __name__ == '__main__':

    #初期値
    initial = 0.01

    #指数的成長モデル f(x) = 2x
    #lambda式
    #func = lambda x, y, z: x+y+z
    #func(2, 3, 4) -> 9
    drawModel(lambda x: 2*x, initial)

    #ロジスティック成長モデル g(x) = 2x(1-x)
    drawModel(lambda x: 2*x*(1-x), initial)

    xlabel("n")
    ylabel("f^n(x)")
    show()
