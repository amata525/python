#coding:utf-8

import numpy as np
import matplotlib.pyplot as plt

N = 128
t = np.arange(0, N, 1)
fc = 2

signal = [1, -1, -1, -1, 1, 1, 1, -1]
psk = []

wave0 = np.cos(2 * np.pi * t / N * fc)
wave1 = np.cos((2 * np.pi * t / N * fc) + np.pi)

for i in signal:
    if i == 1:
        psk.extend(wave0)
    else:
        psk.extend(wave1)


# 復調
demo = []
for i in signal:
    demo.extend(np.cos(2*np.pi*t/N*fc))


psk = np.array(psk)
demo = np.array(demo)
psk *= demo

plt.subplot(3,1,1)
plt.plot(range(len(psk)),psk)

data = []

for i in range(len(signal)):
    data.append(psk[i*N + N/(fc*2)])

print "demo data:", data

plt.show()
