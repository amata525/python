# coding:utf-8

import wave
import struct
import numpy as np
from pylab import *
import random

# 作った波をWAVEファイルへ出力
def save(data, fs, bit, filename):
    wf = wave.open(filename, "w")
    wf.setnchannels(1)
    wf.setsampwidth(bit/8)
    wf.setframerate(fs)
    wf.writeframes(data)
    wf.close()

if __name__ == "__main__":
    freq = 8000 # サンプリング周波数8kHz 44.1kはおもすぎる！
    sec = 2      # 生成時間
    gain = 0.001   # ひとつの波形の振幅

    step = 2.0 * np.pi / freq # 点間ステップ

    phase = 0.0
    white = [0] * freq * sec

    # ホワイトノイズ生成 1Hzからナイキスト周波数まで合成
    for i in range(freq/2):

        if i % 1000 == 0:
            print i

        phase = random.random() * 2.0 * np.pi

        for j in range(freq*sec):
            white[j] += gain * np.sin(i*j*step+phase)

    """
    for n in arange(sec * freq):
        s = 0.0
        phase = random.random() * 2.0 * np.pi


        for k in range(1, freq/2):
            s += gain * np.sin(n*k*step+phase)

        if s > 1.0: s = 1.0
        if s < -1.0: s = -1.0
        white.append(s)
    """

    # とりあえずプロットしてみる
    plot(white)

    white = [int(x*32767.0) for x in white]
    white = struct.pack("h" * len(white), *white)

    save(white, freq, 16, "white_noise.wav")


    show()
