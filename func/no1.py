#coding:utf-8

#関数の定義には def を使う
#引数・戻り値なしの関数定義
def func1():
    print "Hello World!!"

#引数２つ，戻り値なしの関数定義
def func2(a, b):
    print "Print" , "a:" , a , "b:" , b

#引数１つ（デフォルト値あり）の関数定義
#デフォルト値 引数が指定されてない場合にこの値が代入される
def func3(d = 3):
    print d*10

#シーケンス型の可変長引数
#任意の数の引数を指定できる * を付けるだけ
#複数の引数がタプル型で受け入れられる
def func4(*args):
    for x in args:
        print x

#戻り値あり 定義は変わらない returnで戻せばok
def func5(x, y):
    return x + y

#これはメイン関数の始まりのようなもの
if __name__ == "__main__":

    #関数の呼び出し
    print "Start"

    func1()

    func2(5, 10)

    func3(1)
    func3()

    func4('a', 'b', 'c')

    print func5(5, 7)
