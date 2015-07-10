#coding: utf-8

from scipy import arange, hamming, sin, pi
from scipy.fftpack import fft, ifft, fftshift
from matplotlib import pylab as pl

fs = 1024*8 # Sampling rate
L = 1024 # Signal length

# 矩形波作成
sig = [0] * L

for x in arange(L):
    if x < L / 4:
        sig[x] = 0
    elif x < L * 3 / 4:
        sig[x] = 1
    else:
        sig[x] = 0

# フーリエ変換
spectrum = fft(sig)
#half_spectrum = abs(spectrum[: L/2 + 1])
shift_spectrum = fftshift(spectrum)

#図を表示
fig = pl.figure()
fig.add_subplot(211)
pl.plot(sig)
pl.xlim([0, L])
pl.title("1. Signal", fontsize = 20)

fig.add_subplot(212)
pl.plot(shift_spectrum)
pl.xlim([len(shift_spectrum)*3/8, len(shift_spectrum)*5/8])
#pl.ylim([-10, 100])
pl.title("2. FTT", fontsize = 20)

pl.show()
