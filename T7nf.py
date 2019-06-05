#AI-TECHGYM-N-15

import pandas as pd
import urllib

#Seaborn
import seaborn as sns

import matplotlib.pyplot as plt
%matplotlib inline

#データの読み込み
data = "http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
wine = pd.read_csv(data)

txt= "http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.names"
urllib.request.urlretrieve(txt, './wine.names')

#説明文の表示(必要であれば表示)
#f = open("./wine.names","r")
#for line in f:
#    print(line)
#f.close()

#データの個数や型を確認
display(wine.info())

#indexを説明からつける
#アルコール,リンゴ酸,灰,灰分のアルカリ度,マグネシウム,総フェノール,フラバノイド
#非フラバノイドフェノール,プロアントシアニン,色の濃さ,色相,希釈ワインのOD 280 / OD 315,プロリン
columns_name = ['class','Alcohol','Malic_acid','Ash',
                'Alcalinity_of_ash','Magnesium','Total_phenols',
                'Flavanoids','Nonflavanoid_phenols','Proanthocyanins',
                'Color_intensity','Hue','OD280_OD315','Proline']
wine.columns = columns_name

#データ表示して確認する
display(wine)

#ヒストグラム
plt.hist(wine['Alcohol'])

#x軸とy軸のそれぞれのラベル
plt.xlabel('Alcohol')
plt.ylabel('[%]')

#要約統計量
display(wine['Alcohol'].describe())

#統計的データ分析と可視化
sns.pairplot(wine[['Alcohol', 'Malic_acid', 'Ash', 'Total_phenols', 'Color_intensity']])
plt.grid(True)

