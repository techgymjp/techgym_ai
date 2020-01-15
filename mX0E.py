#AI-TECHGYM-3-1-A-1
#回帰問題と分類問題

#インポート
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

#データを作成
#0〜1までの乱数を100個つくる
x = np.random.rand(100, 1)
y = 3 * x - 2

#モデル
model = linear_model.LinearRegression()
model.fit(x, y)

#係数、切片を表示
print('係数', model.coef_)
print('切片', model.intercept_)

#グラフ表示
plt.scatter(x, y, marker='o')
plt.show()
