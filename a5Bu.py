import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("house_train.csv")

# カラムとターゲットを指定
# ターゲットはSalePrice
X = df[["OverallQual"]].values
y = df["SalePrice"].values

# 線形回帰の学習

# 回帰直線の図示
