#AI-TECHGYM-N-18

import pandas as pd
import urllib
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

#相関係数のために読み込み
import scipy as sp

#線形単回帰
from sklearn import linear_model

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

# 線形回帰インスタンス
REG = linear_model.LinearRegression()

#すべての相関係数の表示


#相関係数のヒートマップを表示
plt.figure(figsize=(8, 8))

plt.savefig('wine_data_heatmap.png')

#相関係数の並び替え


wine_corr_list = pd.DataFrame(wine_corr_sort)

#総関係数上位を表示
ra_low, ra_hi = 14, 25

