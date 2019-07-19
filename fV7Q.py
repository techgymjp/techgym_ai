import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("house_train.csv")
train, test = train_test_split(df, test_size=0.2, random_state=25)

# カラムとターゲットを指定
# ターゲットはSalePrice
X = train[["OverallQual"]].values
y = train["SalePrice"].values

# テストデータの特徴量

# 線形回帰の学習

# 回帰直線の図示
