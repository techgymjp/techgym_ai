#AI-TECHGYM-2-2-A-3
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

#カラムを取得
mean_radius = df["mean radius"]

#箱ひげ図
plt.figure(figsize = (5,8))
plt.boxplot(mean_radius)
plt.grid(True)
