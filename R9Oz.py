#AI-TECHGYM-2-7-A-3
#特徴量エンジニアリング

#インポート
import pandas as pd
import requests,io
import category_encoders as ce

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

#===one-hot-encoding===
#Eoncodeしたい列をリストで指定(複数も指定可能)
list_cols = ['body-style','engine-type']
auto_c = auto[['body-style','engine-type']]

#OneHotEncodeしたい列を指定(Nullや不明の場合の補完方法も指定)
ce_ohe = ce.OneHotEncoder(cols=list_cols)

#変換後のデータフレーム
auto_ce = ce_ohe.fit_transform(auto_c)

#表示
display(auto_ce)
