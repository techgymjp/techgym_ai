#AI-TECHGYM-2-7-A-1
#特徴量エンジニアリング

#インポート
import pandas as pd
import requests,io
from sklearn.preprocessing import LabelEncoder

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

#LabelEncoderのインスタンスを生成
le = LabelEncoder()

#ラベルを覚えさせる,ラベルを整数に変換
le_a = le.fit_transform(auto['make'])
auto['label_make'] = le_a

#count encoding
count = auto.groupby('make').label_make.count()
auto['count_make'] = auto['make'].map(count)

display(auto[['make','label_make','count_make']])
