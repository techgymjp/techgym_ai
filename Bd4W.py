#AI-TECHGYM-3-12-A-1
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
from sklearn.preprocessing import minmax_scale

#データのロード
boston = pd.read_csv("BostonHousing.csv")

#必要であれば表示
#display(boston.DESCR)

boston.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT','MEDV']

#データフレーム
data_boston = boston.drop('MEDV', axis=1)
data_boston['PRICE'] = boston["MEDV"]

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
#スケーリング
y_pred_s = minmax_scale(y_pred, feature_range=(0,1))
y_test_s = minmax_scale(y_test, feature_range=(0,1))
MSLE = mean_squared_log_error(y_pred_s, y_test)
print('RMSLE(重回帰)',np.sqrt(MSLE))

###ここから###
#Lasso回帰
lasso = Lasso(alpha=0.001)
lasso.fit(X_train, y_train)

y_pred_lasso = lasso.predict(X_test)

#MAE
print('MAE  (重回帰:lasso)',mean_absolute_error(y_pred_lasso, y_test))

#RMSE
MSE = mean_squared_error(y_pred_lasso, y_test)
print('RMSE (重回帰:lasso)',np.sqrt(MSE))

#RMSLE
y_pred_lasso_s = minmax_scale(y_pred_lasso, feature_range=(0,1))
y_test_s = minmax_scale(y_test, feature_range=(0,1))
MSLE = mean_squared_log_error(y_pred_lasso_s, y_test_s)
print('RMSLE(重回帰:lasso)',np.sqrt(MSLE))

#Ridge回帰
ridge = Ridge(alpha=0.01)
ridge.fit(X_train, y_train)

y_pred_ridge = ridge.predict(X_test)

#MAE
print('MAE  (重回帰:ridge)',mean_absolute_error(y_pred_ridge, y_test))

#RMSE
MSE = mean_squared_error(y_pred_ridge, y_test)
print('RMSE (重回帰:ridge)',np.sqrt(MSE))

#RMSLE
y_pred_ridge_s = minmax_scale(y_pred_ridge, feature_range=(0,1))
y_test_s = minmax_scale(y_test, feature_range=(0,1))
MSLE = mean_squared_log_error(y_pred_ridge_s, y_test_s)
print('RMSLE(重回帰:ridge)',np.sqrt(MSLE))
