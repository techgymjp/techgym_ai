#AI-TECHGYM-3-7-A-1
#回帰問題と分類問題

#インポート
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

#データのロード
boston = load_boston()

#必要であれば表示
#display(boston.DESCR)

#データフレーム
data_boston = pd.DataFrame(boston.data, columns=boston.feature_names)
data_boston['PRICE'] = boston.target

#重回帰モデル
lr_multi = LinearRegression()

#目的変数、説明変数
x_column_list_for_multi = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
y_column_list_for_multi = ['PRICE']

data_boston_x = data_boston[x_column_list_for_multi]
data_boston_y = data_boston[y_column_list_for_multi]

#学習
lr_multi.fit(data_boston_x,  data_boston_y)

#係数、切片
print('係数',lr_multi.coef_)
print('切片',lr_multi.intercept_)

#テストデータ、学習データの分割
X_train, X_test, y_train, y_test = train_test_split(data_boston_x, data_boston_y, test_size=0.3)

#データサイズ
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

#モデル(分割した学習データ)
lr_multi2 = LinearRegression()

#学習
lr_multi2.fit(X_train, y_train)

#係数、切片
print('係数',lr_multi2.coef_)
print('切片',lr_multi2.intercept_)

#予測
y_pred = lr_multi2.predict(X_test)

#差分
diff = y_pred - y_test
print(diff.head())

#MAE
print('MAE(重回帰)',mean_absolute_error(y_pred, y_test))

#単回帰分析でのMAE
x_column_list = ['RM']
y_column_list = ['PRICE']

X_train, X_test, y_train, y_test = train_test_split(data_boston[x_column_list], data_boston[y_column_list], test_size=0.3)

lr_single = LinearRegression()

lr_single.fit(X_train, y_train)
y_pred = lr_single.predict(X_test)

#MAE
print('MAE(単回帰)',mean_absolute_error(y_pred, y_test))

