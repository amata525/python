# coding:utf-8

import numpy as np
from pylab import *
import matplotlib.lines as lines

# クモの巣図法を描画

# 関数funcを描画
def drawGraph(func):
    xList = []
    yList = []

    for x in np.arange(-0.1, 1.0, 0.01):
        xList.append(x)
        yList.append(func(x))

    plot(xList, yList)

# funcの起動に対するクモの巣図法を描画
def drawCobweb(func, initial):

    #vertices:頂点の数
    vertices = []

    #初期座標
    x = initial
    y = 0
    vertices.append([x, y])

    for n in range(1, 13):
        #垂直方向
        y = func(x)
        vertices.append([x, y])

        #水平方向
        x = y
        vertices.append([x, y])

    vertices = np.array(vertices)
    plot(vertices[:,0], vertices[:,1], '--')

if __name__ == "__main__":
    #ロジスティック成長モデルの場合

    #y = xを描画
    drawGraph(lambda x: x)

    #y = 2x(1-x)を描画
    drawGraph(lambda x: 2*x*(1-x))

    #初期値を変えてクモの巣図法を描画
    for initial in np.arange(0.0, 1.0, 0.1):
        drawCobweb(lambda x: 2*x*(1-x), initial)

    axis([0.0, 1.0, 0.0, 0.6])
    grid(True)
    show()
