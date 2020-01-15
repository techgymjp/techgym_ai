#AI-TECHGYM-3-10-Q-1
#回帰問題と分類問題

#インポート
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
%matplotlib inline

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error

#データフレーム
data_added_dummies =

#ヒストグラムの表示
plt.hist(data_added_dummies["取引価格（総額）"])
plt.show()

#6000万円未満の不動産に絞って表示
tmp_data =
plt.hist(tmp_data["取引価格（総額）"])
plt.show()

#6000万円以下のデータに絞る
data_added_dummies =

#モデル
lr =

#目的変数、説明変数(単回帰)
x_column_list =
y_column_list =

x = data_added_dummies[x_column_list]
y = data_added_dummies[y_column_list]

#学習
lr.fit(x, y)

#必要なら係数、切片を表示
#print('係数(単回帰)',lr.coef_)
#print('切片(単回帰)',lr.intercept_)

#目的変数、説明変数(重回帰)
x =
y =

#モデル、学習
lr_multi = LinearRegression()
lr_multi.fit(x, y)

#必要なら係数、切片を表示
#print('係数(重回帰)',lr_multi.coef_)
#print('切片(重回帰)',lr_multi.intercept_)

#各係数を必要なら表示
print(x.columns[1], lr_multi.coef_[1])
print(x.columns[2], lr_multi.coef_[2])
print(x.columns[3], lr_multi.coef_[3])


#目的変数、説明変数(単回帰)
x_column_list =
y_column_list =

#学習データとテストデータの分割
X_train, X_test, y_train, y_test = train_test_split(data_added_dummies[x_column_list], data_added_dummies[y_column_list], test_size=0.3)

#モデル、学習、予測
lr_single = LinearRegression()
lr_single.fit(X_train, y_train)
y_pred = lr_single.predict(X_test)

#MAE
print('MAE(単回帰)')

#決定係数
print('決定係数(単回帰)')

#目的変数、説明変数(重回帰)
x =
y =

#学習データとテストデータの分割
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

#モデル、学習、予測
lr_multi2 = LinearRegression()
lr_multi2.fit(X_train, y_train)
y_pred = lr_multi2.predict(X_test)

#MAE
print('MAE(重回帰)')

#決定係数
print('決定係数(重回帰)')

#予測値とテストデータの差分
diff = 
display(diff.head())

