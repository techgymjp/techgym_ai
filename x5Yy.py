#Tech-Gym-7-21
#回帰モデルの性能評価指標
#
#平均二乗誤差（Mean Squared Error：MSE）
#平均絶対誤差（Mean Absolute Error：MAE)
#Median Absolute Error（MedAE）: 残差の絶対値の中央値
#決定係数（R2）:　二乗誤差をどれだけ削れたかを示す指標
#                 誤差をすべてなくせば1.0

#データの準備
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split

#学習モデル
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import LinearSVR

#標準化
from sklearn.preprocessing import StandardScaler

#性能評価
from sklearn.metrics import mean_squared_error, mean_absolute_error, median_absolute_error, r2_score

# Housingデータセットを読み込み
california = fetch_california_housing()

# DataFrameにデータを格納
X = pd.DataFrame(california.data, columns=california.feature_names)

# 住宅価格の中央値（MEDV）のデータを用意
y = pd.Series(california.target, name='MEDV')

# 訓練データとテストデータに分ける
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)

# 標準化処理
sc = StandardScaler()
sc.fit(X_train)
X_train = sc.transform(X_train)
X_test = sc.transform(X_test)

# モデルの設定
models = {
    'LinearRegression': LinearRegression(),
    'Ridge': Ridge(random_state=0),
    'DecisionTreeRegressor': DecisionTreeRegressor(random_state=0),
    'LinearSVR': LinearSVR(random_state=0)
}

# 評価値の計算
scores = {}
for model_name, model in models.items():
    model.fit(X_train, y_train)
    scores[(model_name, 'MSE')] = mean_squared_error(y_test, model.predict(X_test))
    scores[(model_name, 'MAE')] = mean_absolute_error(y_test, model.predict(X_test))
    scores[(model_name, 'MedAE')] = median_absolute_error(y_test, model.predict(X_test))
    scores[(model_name, 'R2')] = r2_score(y_test, model.predict(X_test))

#表示
pd.Series(scores).unstack()

