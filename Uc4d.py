import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("house_train.csv")

# カラムとターゲットを指定
# ターゲットはSalePrice
X = df[["OverallQual"]].values
y = df["SalePrice"].values

# 線形回帰の学習
slr = LinearRegression()
slr.fit(X,y)

# 回帰直線の図示
plt.scatter(X,y)
plt.plot(X,slr.predict(X),color='red')
plt.show()
