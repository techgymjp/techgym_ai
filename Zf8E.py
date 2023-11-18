#AI-TECHGYM-3-7-Q-1
#回帰問題と分類問題

#インポート
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

#データのロード
#データのロード & データフレーム の作成
boston.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT','MEDV']
data_boston = boston.drop('MEDV', axis=1)
data_boston['PRICE'] = boston["MEDV"]

#重回帰モデル
lr_multi = LinearRegression()

#目的変数、説明変数
x_column_list_for_multi =
y_column_list_for_multi =

data_boston_x = data_boston[x_column_list_for_multi]
data_boston_y = data_boston[y_column_list_for_multi]

#学習


#係数、切片
print('係数',lr_multi.coef_)
print('切片',lr_multi.intercept_)

#テストデータ、学習データの分割
X_train, X_test, y_train, y_test =

#データサイズ
print(X_train)
print(X_test)
print(y_train)
print(y_test)

#モデル(分割した学習データ)
lr_multi2 =

#学習
lr_multi2.fit(X_train, y_train)

#係数、切片
print('係数',lr_multi2.coef_)
print('切片')

#予測
y_pred =

#差分
diff = y_pred - y_test
print(diff.head())

#MAE


#単回帰分析でのMAE
x_column_list = ['RM']
y_column_list = 

X_train, X_test, y_train, y_test =

lr_single =

lr_single.fit(X_train, y_train)
y_pred = lr_single.predict(X_test)

#MAE

