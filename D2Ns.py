#AI-TECHGYM-2-3-A-3
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

#欠損値の確認
#print("欠損値の数",mean_radius.isnull().sum())
#print("データの数",len(mean_radius))
#print("平均値",mean_radius.mean())

#欠損値のエンコード
#欠損値をダミー変数に置き換える
mean_radius_d = pd.get_dummies(mean_radius, dummy_na=True)

#NaNを抜き出した
mean_radius_d_nan = mean_radius_d.T.tail(1).T
mean_radius_d_nan_bool = (mean_radius_d_nan == 1)
display(mean_radius_d_nan_bool.sum())
