#AI-TECHGYM-3-6-A-1
#回帰問題と分類問題

#インポート
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston

#データのロード
boston = load_boston()

#必要であれば表示
#display(boston.DESCR)

#データフレーム
data_boston = pd.DataFrame(boston.data, columns=boston.feature_names)
data_boston['PRICE'] = boston.target

#データを表示
display(data_boston.head())
display(data_boston.tail())

#変数の相関
sns.jointplot('RM', 'PRICE', data=data_boston)

#変数の相関
sns.pairplot(data_boston, vars=["PRICE", "RM", "DIS"])

#単回帰モデル
lr = LinearRegression()

#目的変数、説明変数
x_column_list = ['RM']
y_column_list = ['PRICE']

data_boston_x = data_boston[x_column_list]
data_boston_y = data_boston[y_column_list]

#学習
lr.fit(data_boston_x, data_boston_y)

#係数、切片
print('係数', lr.coef_)
print('切片', lr.intercept_)
