# coding: utf-8

from scipy import identity
from scipy import dot, roll
from scipy.linalg import inv

I = identity(10) # (10*10)　の単位行列

print I, "\n"

# 行列積
I_ar = dot(I, I.T)

print I_ar, "\n"

# 行列の回転（シフト）
I_roll_3 = roll(I, 3, axis = 1) # 第２次元を３つシフト

print I_roll_3, "\n"

# 逆行列
I_inv = inv(I) # 単位行列の逆行列は単位行列

print I_inv, "\n"
