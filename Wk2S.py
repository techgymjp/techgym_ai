#AI-TECHGYM-3-11-A-1
#回帰問題と分類問題

#インポート
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
%matplotlib inline

from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error

#データフレーム
data_added_dummies = pd.read_csv("./data_added_dummies.csv")

#6000万円以下のデータに絞る
data_added_dummies = data_added_dummies[data_added_dummies["取引価格（総額）"] < 60000000]

#目的変数、説明変数(重回帰)
x = data_added_dummies.drop("取引価格（総額）", axis=1)
y = data_added_dummies["取引価格（総額）"]

#学習データとテストデータの分割
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

#モデル、学習、予測(Lasso),WARNINGが出るのでtol=0.1と指定する
lr_multi2 = Lasso(alpha=1, tol=0.1)
lr_multi2.fit(X_train, y_train)
y_pred = lr_multi2.predict(X_test)

#MAE
print('MAE(Lasso)',mean_absolute_error(y_pred, y_test))

#決定係数
print('決定係数(Lasso)',r2_score(y_test, y_pred))


#モデル、学習、予測(Ridge)
lr_multi2 = Ridge(alpha=0.1, normalize=True)
lr_multi2.fit(X_train, y_train)
y_pred = lr_multi2.predict(X_test)

#MAE
print('MAE(Ridge)',mean_absolute_error(y_pred, y_test))

#決定係数
print('決定係数(Ridge)',r2_score(y_test, y_pred))
