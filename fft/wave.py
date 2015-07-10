# coding: utf-8

from scipy import arange, hamming, sin, pi
from scipy.fftpack import fft, ifft
from matplotlib import pylab as pl

import wave
import struct
import numpy as np
from pylab import *


fs = 1.0 # Sampling rate
L = 100 # Signal length

A = 0.5
f = 20

# Triangle wave
data = []
# [-1.0, 1.0]の小数値が入った波を作成
for n in arange(L * fs): # nはサンプルインデックス
    s = 0.0
    for k in range(0, 10): # サンプルごとに１０個のサイン波を重ねあわせ
        s += (-1.)**k * (A / (2.*k+1.)**2.) * sin((2.*k+1.) * 2. * pi * f + n / fs)

    # 振幅が大きい時はクリッピング
    if s > 1.0 : s = 1.0
    if s < -1.0 : s = -1.0
    data.append(s)

# [-32768, 32767]の整数値に変換
data = [int(x * 32767.0) for x in data]

pl.plot(data)
pl.xlim([0, L])
pl.title("TriangeleWave", fontsize = 20)
pl.show()
