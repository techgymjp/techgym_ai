#AI-TECHGYM-3-3-Q-1
#回帰問題と分類問題

#インポート
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

#データを作成
#0〜1までの乱数を100個つくる

#値の範囲を-2~2に調整
x1 = x1 * 4 - 2
x2 = x2 * 4 - 2

#yの値をつくる

#標準正規分布(平均0,標準偏差1)の乱数を加える
y += np.random.randn(100, 1)

#モデル
#[[x1_1, x2_1], [x1_2, x2_2], ..., [x1_100, x2_100]]という形に変換
x1_x2 =

model = linear_model.LinearRegression()


#係数、切片を表示、決定係数
print('係数', model.coef_)
print('切片', model.intercept_)
print('決定係数', model.score(x1_x2, y))

# 求めた回帰式で予測
y_p = model.predict(x1_x2)

#グラフ表示

plt.scatter(x1, y, marker='x')
plt.scatter(x1, y_p, marker='o')
plt.xlabel('x1')
plt.ylabel('y')


plt.scatter(x2, y, marker='x')
plt.scatter(x2, y_p, marker='o')
plt.xlabel('x2')
plt.ylabel('y')

plt.tight_layout()
plt.show()
