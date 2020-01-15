#AI-TECHGYM-3-4-A-1
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
y = 4 * x**3 - 3 * x**2 + 2 * x - 1

#標準正規分布(平均0,標準偏差1)の乱数を加える
y += np.random.randn(100, 1)

#学習データ30個
x_train = x[:30]
y_train = y[:30]

#テストデータ30個
x_test = x[30:]
y_test = y[30:]

#学習用の入力データ
X_TRAIN = np.c_[x_train**9, x_train**8, x_train**7, x_train**6, x_train**5,
                x_train**4, x_train**3, x_train**2, x_train]

model = linear_model.LinearRegression()
model.fit(X_TRAIN, y_train)

#係数、切片を表示、決定係数
print('係数（学習データ）', model.coef_)
print('切片（学習データ）', model.intercept_)
print('決定係数（学習データ）', model.score(X_TRAIN, y_train))

#テストデータ
X_TEST = np.c_[x_test**9, x_test**8, x_test**7, x_test**6, x_test**5,
               x_test**4, x_test**3, x_test**2, x_test]

#決定係数
print('決定係数（テストデータ）', model.score(X_TEST, y_test))

### グラフ表示
plt.figure(figsize=(15,10))
plt.subplot(2, 2, 1)
plt.scatter(x, y, marker='x')
plt.title('ALL')

plt.subplot(2, 2, 2)
plt.scatter(x_train, y_train, marker='x')
plt.scatter(x_train, model.predict(X_TRAIN), marker='o')
plt.title('TRAIN')

plt.subplot(2, 2, 3)
plt.scatter(x_test, y_test, marker='x')
plt.scatter(x_test, model.predict(X_TEST), marker='o')
plt.title('TEST')

plt.tight_layout()
plt.show()
