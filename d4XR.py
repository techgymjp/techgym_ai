#AI-TECHGYM-N-21

# ライブラリのインポート
import pandas as pd

from sklearn.linear_model import LinearRegression

#データの読み込み
#http://www.kaggle.com/c/house-prices-advanced-regression-techniques/download/train.csv
house_train = pd.read_csv("./train.csv")
#display(house_train)

#http://www.kaggle.com/c/house-prices-advanced-regression-techniques/download/test.csv
house_test = pd.read_csv("./test.csv")
#display(house_test)

#NaNデータ
#print(house_train.isnull().sum())
#print(house_test.isnull().sum())

#データ型の確認
#house_train.info()
#house_test.info()

#データの準備
X = house_train[["OverallQual"]].values
y = house_train['SalePrice'].values

# 線形回帰
slr = LinearRegression()

# fit関数でモデル作成
slr.fit(X,y)

# 回帰係数
print('回帰係数：{0}'.format(slr.coef_[0]))

# 切片(直線とy軸との交点)を出力
print('切片: {0}'.format(slr.intercept_))

#テストデータ、NaNがあるところは前の値で埋める
X_test = house_test[["OverallQual"]].values

# 学習済みのモデルから予測した結果をセット
y_test_pred = slr.predict(X_test)

#必要であれば予測した結果を出力
#display(y_test_pred)

# df_testに SalePrice カラムを追加し、学習済みのモデルから予測した結果をセット
house_test['SalePrice'] = y_test_pred

#提出するデータ形式に出力
house_test[["Id","SalePrice"]].to_csv("submission.csv",index=False)
