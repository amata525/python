# coding:utf-8

import numpy as np
import pandas as pd
from statsmodels.tsa.arima_process import arma_generate_sample
import matplotlib.pyplot as plt

# 期間の設定
nobs = 365

# 時系列インデックスの作成
dates = pd.date_range(start='2014-01-01', periods=nobs)

# MAパラメーターの設定:今回はARモデルなのでMA(0)
maparams = np.array([1])

# φ=1.01として，サンプルデータ生成
arparams = np.array([1, 0.1])

y1 = pd.TimeSeries(arma_generate_sample(arparams, maparams, nobs), index = dates)
y1.plot()


plt.show()
