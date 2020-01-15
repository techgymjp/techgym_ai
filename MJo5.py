#AI-TECHGYM-3-23-A-1
#回帰問題と分類問題

#インポート
import math

import numpy as np
import matplotlib.pyplot as plt

from sklearn import linear_model
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor

#WARNING OFF
import warnings
warnings.filterwarnings('ignore')

#データを作成
#0〜1までの乱数を100個つくる
x = np.random.rand(1000, 1)

#値の範囲を-10~10に調整
x = x * 20 - 10

#正弦波カーブ
y = np.array([math.sin(v) for v in x])

#標準正規分布(平均0,標準偏差1)の乱数を加える
y += np.random.randn(1000)

#学習:最小二乗法
model = linear_model.LinearRegression()
model.fit(x, y)

#係数、切片、決定係数を表示
print('係数', model.coef_)
print('切片', model.intercept_)

r2 = model.score(x, y)
print('決定係数(単回帰)', r2)

### グラフ表示
plt.scatter(x, y, marker='+')
plt.scatter(x, model.predict(x), marker='o')
plt.show()

#SVM(回帰)
model = SVR()
model.fit(x, y)

#決定係数を表示
r2 = model.score(x, y)
print('決定係数(SVM)', r2)

#グラフ表示
plt.scatter(x, y, marker='+')
plt.scatter(x, model.predict(x), marker='o')
plt.show()

#k近傍法
model = KNeighborsRegressor()
model.fit(x, y)

#決定係数を表示
r2 = model.score(x, y)
print('決定係数(k近傍法)', r2)

#グラフ表示
plt.scatter(x, y, marker='+')
plt.scatter(x, model.predict(x), marker='o')
plt.show()

#ランダムフォレスト
model = RandomForestRegressor()
model.fit(x, y)

#決定係数を表示
r2 = model.score(x, y)
print('決定係数(ランダムフォレスト)', r2)

#グラフ表示
plt.scatter(x, y, marker='+')
plt.scatter(x, model.predict(x), marker='o')
plt.show()
