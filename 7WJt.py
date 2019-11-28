#AI-TECHGYM-2-1-A-4
#特徴量エンジニアリング

#インポート
import pandas as pd
import matplotlib.pyplot as plt

#乳がんデータを読み込むためのインポート
from sklearn.datasets import load_breast_cancer

#乳がんデータの取得
cancer = load_breast_cancer()

#データフレーム
df = pd.DataFrame(data=cancer.data , columns=cancer.feature_names)
#display(df)

from pylab import rcParams
rcParams['figure.figsize'] = 18, 18 # グラフのサイズを大きくする

#ヒストグラム
df.hist()
plt.tight_layout() # グラフ同士が重ならないようにする
plt.show()
