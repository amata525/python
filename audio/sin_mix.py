#coding:utf-8

import wave
import struct
import numpy as np
from pylab import *


# freqListの制限はを合成した波を返す
def createCombineWave(A, freqList, fs, length):
    data = []
    amp = float(A) / len(freqList)

    for n in arange(length * fs):
        s = 0.0
        for f in freqList:
            s += amp * np.sin(2 * np.pi * f * n / fs)

        #クリッピング
        if s > 1.0: s = 1.0
        if s < -1.0: s = -1.0
        data.append(s)

    #整数値に変換
    data = [int(x * 32767.0) for x in data]

    #バイナリ変換
    data = struct.pack("h" * len(data), *data)
    return data


# 波形を音声出力
def play(data, fs, bit):
    import pyaudio

    # ストリームを開く
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=int(fs),
                    output=True)
    #チャンク単位でストリームに出力し音声を再生
    chunk = 1024
    sp = 0 #再生位置ポインタ
    buffer = data[sp: sp+chunk]

    while buffer != '':
        stream.write(buffer)
        sp = sp + chunk
        buffer = data[sp: sp+chunk]

    stream.close()
    p.terminate()




if __name__ == "__main__":

    # 和音　ド・ミ・ソ
    freqList = [262, 330, 392]

    buffer = createCombineWave(1.0, freqList, 8000.0, 1.0)
    play(buffer, 8000, 16)

    pdata = frombuffer(buffer, dtype='int16')
    plot(pdata[0:500])
    show()
