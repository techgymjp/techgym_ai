#AI-TECHGYM-3-12-Q-1
#回帰問題と分類問題

#インポート
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_squared_log_error

#データのロード
boston = load_boston()

#必要であれば表示
#display(boston.DESCR)

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
lr_multi2.fit(X_train, y_train)

#予測
y_pred = lr_multi2.predict(X_test)

#MAE
print('MAE  (重回帰)',mean_absolute_error(y_pred, y_test))

#RMSE
MSE = mean_squared_error(y_pred, y_test)
print('RMSE (重回帰)',np.sqrt(MSE))

#RMSLE
MSLE = mean_squared_log_error(y_pred, y_test)
print('RMSLE(重回帰)',np.sqrt(MSLE))

###ここから###
#Lasso回帰
lasso = 
lasso.fit(X_train, y_train)

y_pred_lasso =

#MAE
print('MAE  (重回帰:lasso)')

#RMSE

print('RMSE (重回帰:lasso)')

#RMSLE

print('RMSLE(重回帰:lasso)')

#Ridge回帰
ridge =
ridge.fit(X_train, y_train)

y_pred_ridge =

#MAE
print('MAE  (重回帰:ridge)')

#RMSE

print('RMSE (重回帰:ridge)')

#RMSLE

print('RMSLE(重回帰:ridge)')
