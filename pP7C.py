import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

import numpy as np
from sklearn.metrics import mean_squared_error

df = pd.read_csv("house_train.csv")
train, test = train_test_split(df, test_size=0.2, random_state=25)

# テストデータと一致する正解データを定義
true = test

# カラムとターゲットを指定
# ターゲットはSalePrice
X = train[["OverallQual"]].values
y = train["SalePrice"].values

# 正解データの比較用
true_y = true["SalePrice"].values

# テストデータの特徴量
test_X = test[["OverallQual"]].values

# 線形回帰の学習
slr = LinearRegression()
slr.fit(X,y)

# 予測と評価
test_y = slr.predict(test_X)
rmse = np.sqrt(mean_squared_error(true_y, test_y))
print("RMSEの結果")
print(rmse)
