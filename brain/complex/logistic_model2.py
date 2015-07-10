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

    for n in range(1, 5):
        nList.append(n)
        yList.append(func(yList[n-1]))

#    print nList
#    print yList
    plot(nList, yList)


if __name__ == '__main__':

    #ロジスティック成長モデル g(x) = 2x(1-x)
    #こちらは0.0~1.0の任意の値から初めても同じ0.5に収束する

    for initial in np.arange(-0.1, 1.2, 0.1):
        drawModel(lambda x: 2*x*(1-x), initial)

    xlabel("n")
    ylabel("f^n(x)")
    show()
