#AI-TECHGYM-2-3-Q
#特徴量エンジニアリング

#インポート
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#乳がんデータを読み込むためのインポート
from sklearn.datasets import load_breast_cancer

#乳がんデータの取得
cancer = load_breast_cancer()

#データフレーム
df = pd.DataFrame(data=cancer.data , columns=cancer.feature_names)

#カラムを取得
mean_radius = df["mean radius"]

#NaNを挿入する場所
nan_list = np.random.randint(0,len(mean_radius),30)

#欠損値を埋め込み
for nan in nan_list:
    df.iloc[nan,0] = np.nan

