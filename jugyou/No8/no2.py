#coding:utf-8

import numpy as np
import matplotlib.pyplot as plt

# 振幅変調
def ASK_make(signal):
    N = 128
    t = np.arange(0, N, 1)
    fc = 4 # 搬送波周波数

    ask = []

    wave0 = np.sin(2*np.pi*t/N * fc) * 0  #for 0
    wave1 = np.sin(2*np.pi*t/N * fc)      #for 1

    for i in signal:
        if i == 0:
            ask.extend(wave0)
        else:
            ask.extend(wave1)

    return ask

# 周波数変調
def FSK_make(signal):
    N = 128
    t = np.arange(0, N, 1)
    f0 = 1 # 0の時の周波数
    f1 = 4 # 1の時の周波数

    fsk = []

    wave0 = np.sin(2*np.pi*t/N * f0)      #for 0
    wave1 = np.sin(2*np.pi*t/N * f1)      #for 1

    for i in signal:
        if i == 0:
            fsk.extend(wave0)
        else:
            fsk.extend(wave1)

    return fsk

# 位相変調
def PSK_make(signal):
    N = 128
    t = np.arange(0, N, 1)
    fc = 2 # 搬送波周波数

    psk = []

    wave0 = np.sin(2*np.pi*t/N * fc)            #for 0
    wave1 = np.sin(2*np.pi*t/N * fc + np.pi)    #for 1

    for i in signal:
        if i == 0:
            psk.extend(wave0)
        else:
            psk.extend(wave1)


    return psk


if __name__ == "__main__":

    s = raw_input("signal:")
    signal = list(map(int, s))

    ask = ASK_make(signal)
    fsk = FSK_make(signal)
    psk = PSK_make(signal)

    plt.subplot(3,1,1)
    plt.plot(range(len(ask)), ask)

    plt.subplot(3,1,2)
    plt.plot(range(len(fsk)), fsk)

    plt.subplot(3,1,3)
    plt.plot(range(len(psk)), psk)


    plt.show()
