#coding:utf-8

import wave
import struct
import numpy as np
from pylab import *

def createSawtoothWave(A, f0, fs, length):
    data = []

    # [-1.0, 1.0]の小数値が入った波を作成
    for n in arange(length * fs):
        s = 0.0

        for k in range(1, 10): #サンプルごとに１０個のサイン波を重ね合わせ
            s += (A/k) * np.sin(2*np.pi*k*f0*n/fs)

        if s > 1.0: s = 1.0
        if s < -1.0: s = -1.0
        data.append(s)

    data = [int(x*32767.0) for x in data]

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

# 作った波をWAVEファイルへ出力
def save(data, fs, bit, filename):
    wf = wave.open(filename, "w")
    wf.setnchannels(1)
    wf.setsampwidth(bit/8)
    wf.setframerate(fs)
    wf.writeframes(data)
    wf.close()

if __name__ == "__main__":

        # ド，レ，ミ，ファ，ソ，ラ，シ，ド
        freqList = [262, 294, 330, 349, 392, 440, 494, 523]

        buffer = createSawtoothWave(1.0, freqList[6], 8000.0, 1.0)
        #pdata = frombuffer(buffer, dtype='int16')
        #plot(pdata[0:100])
        #show()

        allData = ""

        for f in freqList:
            data = createSawtoothWave(1.0, f, 8000.0, 1.0)
            play(data, 8000, 16)
            allData += data

        save(allData, 8000, 16, "sawtooth_wave.wav")
