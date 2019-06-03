#AI-TECHGYM-N-19

import pandas as pd
import urllib
import matplotlib.pyplot as plt
%matplotlib inline

#線形重回帰
from sklearn.linear_model import LinearRegression

#データの分割
from sklearn.model_selection import train_test_split

#データの取得
data = "http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
wine = pd.read_csv(data)

#indexを説明からつける
#アルコール,リンゴ酸,灰,灰分のアルカリ度,マグネシウム,総フェノール,フラバノイド
#非フラバノイドフェノール,プロアントシアニン,色の濃さ,色相,希釈ワインのOD 280 / OD 315,プロリン
columns_name = ['class','Alcohol','Malic_acid','Ash',
                'Alcalinity_of_ash','Magnesium','Total_phenols',
                'Flavanoids','Nonflavanoid_phenols','Proanthocyanins',
                'Color_intensity','Hue','OD280_OD315','Proline']
wine.columns = columns_name

#回帰分析用のデータフレーム
wine_n = wine[['Alcohol' , 'Magnesium' , 'Total_phenols' , 'Flavanoids' , 'Color_intensity' , 'Proline']]

#欠損値がないかの確認
wine.isnull().sum()

#目的変数にAlcoholを設定、それ以外を説明変数にする
x = wine_n.drop('Alcohol' , axis=1)
y = wine_n['Alcohol']

#訓練用のデータとテスト用のデータに分ける
x_train,x_test,y_train,y_test = train_test_split(x,y, test_size = 0.5 , random_state=0)

# 重回帰クラスの初期化と学習
model = LinearRegression()
model.fit(x_train,y_train)

#決定係数の計算
k_train = model.score(x_train,y_train)
k_test = model.score(x_test,y_test)

# 決定係数を表示
print('決定係数(train):{:.3f}'.format(k_train))
print('決定係数(test):{:.3f}'.format(k_test))
 
# 回帰係数と切片を表示
print('回帰係数{}'.format(pd.Series(model.coef_, index=x.columns)))
print('切片: {:.3f}'.format(model.intercept_))
