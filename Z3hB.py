#AI-TECHGYM-2-1-A-3
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
sns.set(style = "dark", palette = "colorblind", color_codes = True)
plt.figure(figsize = (15,8))

#プロットするデータ指定
ax = sns.distplot(mean_radius, bins = 58, kde = True, color = 'b')

#ラベル
ax.set_xlabel(xlabel = "Mean of distances for each cell nucleus", fontsize = 16)
ax.set_ylabel(ylabel = 'Density : Number of cell nucleus', fontsize = 16)
ax.set_title(label = 'mean radius', fontsize = 20)
plt.show()
