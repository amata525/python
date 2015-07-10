#coding:utf-8

import random
from PIL import Image

#キャンバスを作成
width = 500
height = 500
canvas = Image.new("RGB", (width+1, height+1), (0,0,0))


#描画範囲(aの最小値と最大値)
a1 = 2.0
a2 = 4.0

for i in range(width):
    #aの増分はキャンバスサイズによって決める
    a = a1 + (a2 - a1) * float(i) / width

    # [0, 1]からランダムに初期値を決める
    #x = random.random()
    x = 0.2
    for j in range(1000):
        #ロジスティック方程式
        x = a*x*(1-x)

        #101回目から軌道をプロット
        #収束を待つため
        if j > 100:
            #キャンバスの座標は上下逆なので注意
            canvas.putpixel((i, height - int(x*height)), (255,255,255))

canvas.save("bifurcation.png")
