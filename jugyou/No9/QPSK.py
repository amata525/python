# coding:utf-8

import numpy as np
import matplotlib.pyplot as plt

# QPSK変調
def QPSK_mod(signal):
    N = 128
    t = np.arange(0, N, 1)
    fc = 2

    qpsk = []

    wave00 = np.cos(2 * np.pi * t / N * fc)
    wave01 = np.sin(2 * np.pi * t / N * fc)
    wave10 = -np.cos(2 * np.pi * t / N * fc)
    wave11 = -np.sin(2 * np.pi * t / N * fc)

    a = 0
    b = 0
    count = 0;

    for i in signal:
        if count == 0:
            a = i
            count = 1
        else:
            b = i
            count = 0

            if a == 0 and b == 0:
                print "00"
                qpsk.extend(wave00)
            elif a == 0 and b == 1:
                print "01"
                qpsk.extend(wave01)
            elif a == 1 and b == 0:
                print "10"
                qpsk.extend(wave10)
            else:
                print "11"
                qpsk.extend(wave11)

    return qpsk

if __name__ == "__main__":

    signal = [0,0,0,1,1,0,1,1]

    QPSK = QPSK_mod(signal)

    plt.subplot(3,1,1)
    plt.plot(range(len(QPSK)),QPSK)

    plt.show()
