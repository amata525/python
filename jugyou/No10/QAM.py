# coding:utf-8

import numpy as np
import matplotlib.pyplot as plt


#QAM変調
def QAM_mod(signal):
    N = 128
    t = np.arange(0, N, 1)
    fc = 2

    qam = []

    wave00 = np.sin(2 * np.pi * t / N * fc)
    wave01 = np.cos(2 * np.pi * t / N * fc)
    wave10 = -np.sin(2 * np.pi * t / N * fc)
    wave11 = -np.cos(2 * np.pi * t / N * fc)

    for i in range(0, len(signal), 3):
        if signal[i] == 0 and signal[i+1] == 0:
            if signal[i+2] == 0:
                qam.extend(wave00*0.5)
            else:
                qam.extend(wave00)

        elif signal[i] == 0 and signal[i+1] == 1:
            if signal[i+2] == 0:
                qam.extend(wave01*0.5)
            else:
                qam.extend(wave01)

        elif signal[i] == 1 and signal[i+1] == 0:
            if signal[i+2] == 0:
                qam.extend(wave10*0.5)
            else:
                qam.extend(wave10)

        elif signal[i] == 1 and signal[i+1] == 1:
            if signal[i+2] == 0:
                qam.extend(wave11*0.5)
            else:
                qam.extend(wave11)

    return qam


if __name__ == "__main__":

    signal = [0,1,1, 1,1,1, 0,1,0, 1,0,1, 1,1,0, 1,1,0, 1,0,0]

    QAM = QAM_mod(signal)

    plt.subplot(3,1,1)
    plt.plot(range(len(QAM)),QAM)

    plt.show()
