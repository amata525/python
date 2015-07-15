# coding:utf-8

import numpy as np
import matplotlib.pyplot as plt
import math

def QAM64_mod(signal):
    N = 128
    t = np.arange(0, N, 1)
    fc = 2

    qam64 = []

    I = 0.0
    Q = 0.0
    theta = 0.0
    wave = np.cos(2 * np.pi * t / N * fc)

    for i in range(0, len(signal), 6):
        if signal[i+3] == 0 and signal[i+5] == 0:
            I = 0.25
        elif signal[i+3] == 0 and signal[i+5] == 1:
            I = 0.5
        elif signal[i+3] == 1 and signal[i+5] == 1:
            I = 0.75
        elif signal[i+3] == 1 and signal[i+5] == 0:
            I = 1.0

        if signal[i+2] == 0 and signal[i+4] == 0:
            Q = 0.25
        elif signal[i+2] == 0 and signal[i+4] == 1:
            Q = 0.5
        elif signal[i+2] == 1 and signal[i+4] == 1:
            Q = 0.75
        elif signal[i+2] == 1 and signal[i+4] == 0:
            Q = 1.0

        theta = math.atan2(Q,I)

        if signal[i+1] == 0 and signal[i] == 0:
            theta += 0
        elif signal[i+1] == 0 and signal[i] == 1:
            theta += np.pi / 2
        elif signal[i+1] == 1 and signal[i] == 1:
            theta += np.pi
        elif signal[i+1] == 1 and signal[i] == 0:
            theta += np.pi * (3.0/2.0)

        wave = np.sqrt(I*I + Q*Q) * np.sin(2 * np.pi * t / N * fc + theta)
        qam64.extend(wave)

    return qam64

if __name__ == "__main__":

    signal = [0,0,1, 1,0,0, 0,0,0, 0,1,1, 1,0,1, 1,1,0]

    QAM64 = QAM64_mod(signal)

    plt.subplot(3,1,1)
    plt.plot(range(len(QAM64)),QAM64)

    plt.show()
