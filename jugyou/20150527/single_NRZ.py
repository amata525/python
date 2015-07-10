# coding:utf-8

import numpy as np
import matplotlib.pyplot as plt
import random

""" 単流NRZ方式 """

# 元となる信号の生成 ビット数bit
def createSignal(bit):
    sig = []
    random.seed(10)

    for x in range(bit):
        s = random.randint(0, 1)
        sig.append(s)

    return sig


# 伝送信号の生成 周期T 電位E
# 単流NRZ方式
def createTransSignal(sig, T, E):

    trans = []

    for i in range(len(sig)):
        t = sig[i]

        if t == 0:
            for j in range(T):
                trans.append(0)
        else:
            for j in range(T):
                trans.append(E)

    return trans

# 信号の幅T倍にする
def changeWidth(sig, T):

    trans = []

    for i in range(len(sig)):
        t = sig[i]

        for j in range(T):
            trans.append(t)

    return trans

# 周波数特性を求める
def fftSignal(sig):

    F = np.fft.fft(sig)
    F = np.abs(F)

    return F

if __name__ == "__main__":

    bit = 256
    T = 4
    E = 1

    signal = createSignal(bit)
    transSignal = createTransSignal(signal, T, E)
    signalSource = fftSignal(transSignal)


    # 元の信号を描画用に幅を変更する
    pltSignal = changeWidth(signal, T)

    plt.subplot(3,1,1)
    plt.plot(pltSignal)
    plt.title("Signal")
    plt.xlim(0, bit)
    plt.ylim(-1, 1.5)

    plt.subplot(3,1,2)
    plt.plot(transSignal)
    plt.title("Trans Signal")
    plt.xlim(0, bit)
    plt.ylim(-E-0.5, E+0.5)

    plt.subplot(3,1,3)
    plt.plot(signalSource)
    plt.title("Signal Source")
    plt.xlim(0, len(signalSource)/2)
    plt.ylim(0.01, 100)

    plt.tight_layout()



    plt.show()
