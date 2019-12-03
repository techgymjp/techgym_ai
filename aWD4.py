#AI-TECHGYM-2-1-A-2
#特徴量エンジニアリング

#インポート
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#乳がんデータを読み込むためのインポート
from sklearn.datasets import load_breast_cancer

#乳がんデータの取得
cancer = load_breast_cancer()

#データフレーム
df = pd.DataFrame(data=cancer.data , columns=cancer.feature_names)
#display(df)

#カラムを取得
mean_radius = df["mean radius"]

#設定
sns.set()
sns.set_style('whitegrid')

#ヒストグラム
sns.distplot(mean_radius, bins=16,label='mean radius',kde=True)
plt.legend() 
plt.show()
