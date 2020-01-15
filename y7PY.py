#AI-TECHGYM-3-2-A-1
#回帰問題と分類問題

#インポート
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

#データを作成
#0〜1までの乱数を100個つくる
x = np.random.rand(100, 1)

#値の範囲を-2~2に調整
x = x * 4 - 2

#yの値をつくる
y = 3 * x - 2

#標準正規分布(平均0,標準偏差1)の乱数を加える
y += np.random.randn(100, 1)

#モデル
model = linear_model.LinearRegression()
model.fit(x, y)

#係数、切片を表示
print('係数', model.coef_)
print('切片', model.intercept_)

#決定係数
r2 = model.score(x, y)
print('決定係数', r2)

#グラフ表示
plt.scatter(x, y, marker='o')
plt.scatter(x, model.predict(x), marker='x')
plt.show()
