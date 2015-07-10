# coding:utf-8

import numpy as np
from pylab import *
import matplotlib.lines as lines

# クモの巣図法を描画

# 関数funcを描画
def drawGraph(func):
    xList = []
    yList = []

    for x in np.arange(-1.0, 1.0, 0.01):
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
    #y = xを描画
    drawGraph(lambda x: x)

    #y = 2xを描画
    drawGraph(lambda x: 2*x)

    #初期値を変えてクモの巣図法を描画
    drawCobweb(lambda x: 2*x, 0.01)

    axis([-0.2, 1.0, -1.0, 1.0])
    grid(True)
    show()
