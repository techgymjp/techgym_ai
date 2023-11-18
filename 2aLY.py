#AI-TECHGYM-3-8-Q-1
#回帰問題と分類問題

#インポート
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

#データのロード
boston = pd.read_csv("BostonHousing.csv")
boston.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT','MEDV']
data_boston = boston.drop('MEDV', axis=1)
data_boston['PRICE'] = boston["MEDV"]

#データフレーム
data_boston = pd.DataFrame(boston.data, columns=boston.feature_names)
data_boston['PRICE'] = boston.target

#目的変数、説明変数
x_column_list_for_multi = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
y_column_list_for_multi = ['PRICE']

data_boston_x = data_boston[x_column_list_for_multi]
data_boston_y = data_boston[y_column_list_for_multi]

#テストデータ、学習データの分割
X_train, X_test, y_train, y_test = train_test_split(data_boston_x, data_boston_y, test_size=0.3)

#モデル(分割した学習データ)
lr_multi2 = LinearRegression()

#学習


#係数、切片
print('係数',lr_multi2.coef_)
print('切片',lr_multi2.intercept_)

#予測


#MAE
print('MAE(重回帰)',mean_absolute_error(y_pred, y_test))

###ここから###
#Lasso回帰
lasso =
lasso.fit(X_train, y_train)
print('係数',lasso.coef_)
print('切片')

y_pred_lasso =

#MAE



#Ridge回帰
ridge =
ridge.fit(X_train, y_train)
print('係数')
print('切片',ridge.intercept_)

y_pred_ridge = ridge.predict(X_test)

#MAE

