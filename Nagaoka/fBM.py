# coding:utf-8

import struct
import numpy as np
from pylab import *
import matplotlib.pyplot as plt
import random

# 生成条件
time = 20 #信号の長さ
fs = 2000.0 #サンプリング周波数

# ホワイトノイズ生成
white_noise = []
time_axis = []

n = int(time * fs)
f = 0

for x in range(n):
    f = random.randint(1,n)
    white_noise.append(f)
    time_axis.append(x/fs)


plt.subplot(3,1,1)
plt.plot(time_axis, white_noise)
plt.ylim(-10000, 50000)
#plt.xlim(0, 1)

# パワースペクトルを得る
F = np.fft.fft(white_noise)
freq_axis = np.array(time_axis)
freq_axis = freq_axis/n*fs

Power_F = F * F.conjugate()


plt.subplot(3,1,2)
plt.plot(freq_axis, F)
#plt.ylim(-10000, 50000)
plt.xlim(0, 0.01)

plt.subplot(3,1,3)
plt.plot(freq_axis, Power_F)
#plt.ylim(-10000, 50000)
plt.xlim(0, 0.01)

plt.show()
