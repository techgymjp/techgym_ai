import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression

df = pd.read_csv("train.csv")

# カラムとターゲットを指定
# ターゲットはSalePrice
X = df[["OverallQual"]].values
y = df["SalePrice"].values

# 線形回帰の学習
slr = LinearRegression()
slr.fit(X,y)

# 回帰係数と切片の表示
print("Coefficient : {0}".format(slr.coef_))
a1 = slr.coef_
print("intercepts : {0}".format(slr.intercept_))
b = slr.intercept_

# 回帰直線の図示
plt.scatter(X,y)
plt.plot(X,slr.predict(X),color='red')
plt.show()

