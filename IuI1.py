#AI-TECHGYM-3-6-Q-1
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
data_boston =
data_boston['PRICE'] =

#データを表示



#変数の相関
sns.jointplot()

#変数の相関
sns.pairplot()

#単回帰モデル
lr = LinearRegression()

#目的変数、説明変数
x_column_list =
y_column_list = 

data_boston_x = data_boston[x_column_list]
data_boston_y = data_boston[y_column_list]

#学習


#係数、切片
print('係数', lr.coef_)
print('切片', lr.intercept_)
