# coding:utf-8

import wave
from numpy import *
from pylab import *

# WAVEファイルの情報を表示
def printWaveInfo(wf):
    print "チャンネル数：", wf.getnchannels()
    print "サンプル幅：", wf.getsampwidth()
    print "サンプリング周波数：", wf.getframerate()
    print "フレーム数：", wf.getnframes()
    print "パラメータ：", wf.getparams()
    print "長さ（秒）：", float(wf.getnframes()) / wf.getframerate()


if __name__ == '__main__':

    wf = wave.open("guitar_A4.wav", "r")
    printWaveInfo(wf)

    buffer = wf.readframes(wf.getnframes())
    print len(buffer) #バイト数 = １フレーム２バイト × フレーム数

    # bufferはバイナリなので２バイトずつ整数(-32768から32767)にまとめる
    data = frombuffer(buffer, dtype='int16')

    # プロット
    plot(data[2000:2200])
    show()
