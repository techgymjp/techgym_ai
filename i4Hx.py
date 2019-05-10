import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression

df = pd.read_csv("train.csv")

# カラムとターゲットを指定
# ターゲットはSalePrice
X = df[["OverallQual", "GrLivArea"]].values
y = df["SalePrice"].values

# 線形回帰の学習
slr = LinearRegression()
slr.fit(X,y)

# 回帰係数とy切片の表示
print("Coefficient : {0}".format(slr.coef_))
a1, a2 = slr.coef_
print("intercepts : {0}".format(slr.intercept_))
b = slr.intercept_


# 3D描画（回帰平面の描画）
x, y, z = np.array(df["OverallQual"]), np.array(df["GrLivArea"]), np.array(df["SalePrice"].values)
fig     = plt.figure()
ax      = Axes3D(fig)
ax.scatter3D(np.ravel(x), np.ravel(y), np.ravel(z))

# np.arange(0, 10, 2)は# 初項0,公差2で終点が10の等差数列(array([ 2,  4,  6,  8, 10]))
X, Y = np.meshgrid(np.arange(0, 12, 2), np.arange(0, 6000, 1000))
Z = a1 * X + a2 * Y + b 
ax.plot_surface(X, Y, Z, alpha = 0.5, color = "red") #alphaで透明度を指定
ax.set_xlabel("OverallQual")
ax.set_ylabel("GrLivArea")
ax.set_zlabel("SalePrice")

plt.show()

