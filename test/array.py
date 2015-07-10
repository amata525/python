# -*- coding: utf-8 -*-
from scipy import rand

ar = rand(100, 200) # (100 * 200) の配列

print ar

# 属性・メソッド

# Tuple of array dimensions
# 要素数を求める
shape = ar.shape
dim1 = shape[0] # 100
dim2 = shape[1] # 200

print "\n"
print shape
print dim1
print dim2

# 転置
ar_T = ar.T

print "\n"
print ar_T

# 配列のコピー(deepcopy : ar　と　ar_copy は別の参照を持つ)
ar_copy = ar.copy()

print "\n"
print ar_copy

# Reshape
ar_reshape = ar.reshape(50, 400) # (50 * 400)　の配列

# その他

# n個ごと（n-1個飛ばし？）
ar_step3 = ar[::3] # 2個飛ばし（第１次元）

print "\n"
print ar_step3

# Reverse
ar_rv1 = ar[::-1] # 第１次元をリバース
ar_rv2 = ar[:, ::-1] # 第２次元をリバース

print "\n"
print ar_rv1
print ar_rv2
