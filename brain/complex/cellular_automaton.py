#coding:utf-8
import Image, ImageDraw, ImageFont

# 一次元セルオートマトン

OFF, ON = 0, 1


# １０進数を２進数の01リストに変換
#　８ビットまで
def dec2bin(n):
    #下位ビットから順に並べる
    bit_list = []
    for i in range(8):
        bit_list.append(n%2)
        n /= 2

    return bit_list


#　１次元セルオートマトンの図を描画
def ca(width, height, rulenum):
    results = []

    #初期状態（中央のセルだけON）
    first_row = [0] * width
    first_row[width / 2] = ON
    results.append(first_row)

    #ルールの番号から次の状態のビット列を得る
    rule = dec2bin(rulenum)

    for i in range(height - 1):
        old_row = results[-1]
        new_row = []

        for j in range(width):
            #widthの剰余を取るのは，端同士がつながっているため
            n = 4*old_row[(j-1)%width] + 2 * old_row[j] + old_row[(j+1)%width]
            new_row.append(rule[n])

        results.append(new_row)

    return results

# セルオートマトンを描画
def render(results, width, height, filename="ca.png"):

    img = Image.new("RGB", (width, height), (255,255,255))
    draw = ImageDraw.Draw(img)
    for y in range(height):
        for x in range(width):
            if results[y][x] == ON:
                draw.point((x,y), (0,0,0))

    img.save(filename, "PNG")

if __name__ == "__main__":
    width, height = 300, 150
    rulenum = 62
    results = ca(width, height, rulenum)
    render(results, width, height)
