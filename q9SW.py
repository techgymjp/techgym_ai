#AI-TECHGYM-N-22

# ライブラリのインポート
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt
%matplotlib inline

from sklearn.linear_model import LinearRegression

#データの読み込み
#http://www.kaggle.com/c/house-prices-advanced-regression-techniques/download/train.csv
house_train = 
#display(house_train)

#http://www.kaggle.com/c/house-prices-advanced-regression-techniques/download/test.csv
house_test = 
#display(house_test)

#数値型のみ抜き出す、NaNがあるところは削除する
house_train_num = 

#相関係数を表示
house_corr = 

#必要に応じて表示して確認
#display(house_corr)

#相関係数の上位14個を表示
display(              ('SalePrice', ascending=False)['SalePrice'].head(15))

#回帰分析用のデータフレーム
df_col = ['SalePrice','OverallQual' , 'GrLivArea' , 'GarageCars' , 'GarageArea',
          'TotalBsmtSF' , '1stFlrSF' , 'FullBath' , 'TotRmsAbvGrd' , 'YearBuilt',
          'YearRemodAdd' , 'GarageYrBlt','MasVnrArea','Fireplaces','BsmtFinSF1']

house_train_num_df = 

#データの準備
X = 
y = 

# 線形回帰
slr = 

# fit関数でモデル作成


# 回帰係数
print('回帰係数：{0}'.format())

# 切片(直線とy軸との交点)を出力
print('切片: {0}'.format())

#統計的データ分析と可視化

plt.grid(True)

df_col_test = ['OverallQual' , 'GrLivArea' , 'GarageCars' , 'GarageArea',
               'TotalBsmtSF' , '1stFlrSF' , 'FullBath' , 'TotRmsAbvGrd' , 'YearBuilt',
               'YearRemodAdd' , 'GarageYrBlt','MasVnrArea','Fireplaces','BsmtFinSF1']

#テストデータ、NaNがあるところは前の値で埋める
X_test = 

# 学習済みのモデルから予測した結果をセット
y_test_pred = 

#予測した結果を出力
display(y_test_pred)

# df_testに SalePrice カラムを追加し、学習済みのモデルから予測した結果をセット
house_test['SalePrice'] = 

#提出するデータ形式に出力


