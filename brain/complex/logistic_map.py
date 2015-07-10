# coding: utf-8
import numpy as np
from pylab import *
import matplotlib.lines as lines

# ロジスティック写像

# 関数funcを描画
def drawGraph(func):
    xList = []
    yList = []

    for x in np.arange(-0.1, 1.0, 0.01):
        # append:リストの最後に引数を要素として加える
        xList.append(x)
        yList.append(func(x))

    plot(xList, yList)

#funcの軌道に対する出力の遷移とクモの巣図法を描画
def drawCobweb(func, initial):
    vertices = []
    nList = []
    yList = []

    #初期座標
    x = initial
    y = 0
    vertices.append([x, y])
    nList.append(0)
    yList.append(x)

    for n in range(1, 100):
        #垂直方向
        y = func(x)
        vertices.append([x, y])
        nList.append(n)
        yList.append(y)
        print n, y

        #水平方向
        x = y
        vertices.append([x, y])

    vertices = np.array(vertices)

    plot(vertices[:,0], vertices[:,1], '--')

    #2つ目のグラフを描画
    subplot(212)
    plot(nList, yList)

if __name__ == "__main__":

    #1つ目のグラフを描画
    subplot(211)

    # y = x を描画
    drawGraph(lambda x: x)

    # y = ax(1-x)を描画
    # ロジスティック方程式
    a = 3.3
    drawGraph(lambda x: a*x*(1-x))

    #初期値を変えてクモの巣図法を描画
    initial = 0.9
    drawCobweb(lambda x: a*x*(1-x), initial)

    subplot(211)
    axis([0.0, 1.0, 0.0, 1.0])
    xlabel("x")
    ylabel("y")

    subplot(212)
    axis([0,100,0,1.0])
    xlabel("n")
    ylabel("y")

    show()
