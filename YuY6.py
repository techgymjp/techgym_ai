#AI-TECHGYM-2-7-A-5
#特徴量エンジニアリング

#インポート
import pandas as pd
import numpy as np
import requests,io
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#自動車価格データの取得
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'
res = requests.get(url).content
auto = pd.read_csv(io.StringIO(res.decode('utf-8')), header=None)
auto.columns =['symboling','normalized-losses','make','fuel-type' ,'aspiration','num-of-doors',
                            'body-style','drive-wheels','engine-location','wheel-base','length','width','height',
                            'curb-weight','engine-type','num-of-cylinders','engine-size','fuel-system','bore',
                            'stroke','compression-ratio','horsepower','peak-rpm','city-mpg','highway-mpg','price']
#データ表示
#display(auto)

# データの前処理
auto_c = pd.get_dummies(auto[['width','engine-size','make','body-style','engine-type','fuel-system']])

auto_c['price'] = auto['price']
auto_c = auto_c.replace('?', np.nan).dropna()

# 学習用/検証用にデータを分割
X = auto_c.drop('price', axis=1)
y = auto_c['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)

# モデルの構築・評価
model = LinearRegression()
model.fit(X_train,y_train)
print('決定係数(train):{:.3f}'.format(model.score(X_train,y_train)))
print('決定係数(test):{:.3f}'.format(model.score(X_test,y_test)))
