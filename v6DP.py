#AI-TECHGYM-3-4-Q-1
#回帰問題と分類問題

#インポート
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

#データを作成
#0〜1までの乱数を100個つくる
x = np.random.rand(100, 1)

#値の範囲を-2~2に調整
x = x * 2 - 1

#yの値をつくる


#標準正規分布(平均0,標準偏差1)の乱数を加える
y += np.random.randn(100, 1)

#学習データ30個
x_train = x[:30]
y_train = y[:30]

#テストデータ30個
x_test = x[30:]
y_test = y[30:]

#学習用の入力データ
X_TRAIN =

model = linear_model.LinearRegression()
model.fit(X_TRAIN, y_train)

#係数、切片を表示、決定係数
print('係数（学習データ）', model.coef_)
print('切片（学習データ）', model.intercept_)
print('決定係数（学習データ）', model.score(X_TRAIN, y_train))

#テストデータ
X_TEST =

#決定係数
print('決定係数（テストデータ）', model.score(X_TEST, y_test))

### グラフ表示
plt.figure(figsize=(15,10))
plt.subplot(2, 2, 1)

plt.title('ALL')

plt.subplot(2, 2, 2)
plt.scatter(x_train, y_train, marker='x')

plt.title('TRAIN')

plt.subplot(2, 2, 3)
plt.scatter(x_test, y_test, marker='x')

plt.title('TEST')

plt.tight_layout()
plt.show()
