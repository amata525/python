# coding:utf-8

import scipy.signal as sig
import numpy as np
import matplotlib.pyplot as pl

# 矩形の信号を作る
t = np.arange(-1.0, 1.0, 0.001)
t2 = np.arange(-2.0, 2.0-0.001, 0.001)
signal = np.zeros(t.size)

for i in range(t.size):
    if t[i] >= -0.5 and t[i] <= 0.5:
        signal[i] = 1


pl.subplot(2,2,1)
pl.plot(t, signal)
pl.ylim([-0.5, 1.5])


# 自己相関関数
cor = sig.correlate(signal, signal, mode="full")

# 値がでかすぎるので小さく
cor /= 1000

pl.subplot(2,2,2)
pl.plot(t2, cor)
pl.ylim([-0.5, 1.5])


# 自己相関関数をフーリエ変換
fcor = np.fft.fft(cor)
fcor = np.abs(fcor)

pl.subplot(2,2,3)
pl.plot(fcor)
pl.ylim([-0.01, 100])
pl.xlim([0, 50])




pl.show()
