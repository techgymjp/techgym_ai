#AI-TECHGYM-2-3-A-1
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
print("欠損値の数",mean_radius.isnull().sum())
print("データの数",len(mean_radius))
print("平均値",mean_radius.mean())

#リストワイズ削除
mean_radius_drop = mean_radius.dropna()

#欠損値の確認
print("リストワイズ後：欠損値の数",mean_radius_drop.isnull().sum())
print("リストワイズ後：データの数",len(mean_radius_drop))
print("リストワイズ後：平均値",mean_radius_drop.mean())

#0に置き換え
mean_radius_fillna = mean_radius.fillna(0)
print("0に置き換え後：欠損値の数",mean_radius_fillna.isnull().sum())
print("0に置き換え後：データの数",len(mean_radius_fillna))
print("0に置き換え後：平均値",mean_radius_fillna.mean())

#前の値に置き換え
mean_radius_fillna_f = mean_radius.fillna(method='ffill')
print("前の値に置き換え後：欠損値の数",mean_radius_fillna_f.isnull().sum())
print("前の値に置き換え後：データの数",len(mean_radius_fillna_f))
print("前の値に置き換え後：平均値",mean_radius_fillna_f.mean())

#後の値に置き換え
mean_radius_fillna_b = mean_radius.fillna(method='bfill')
print("後の値に置き換え後：欠損値の数",mean_radius_fillna_b.isnull().sum())
print("後の値に置き換え後：データの数",len(mean_radius_fillna_b))
print("後の値に置き換え後：平均値",mean_radius_fillna_b.mean())

#平均値で置き換え
mean_radius_fillna_m = mean_radius.fillna(mean_radius.mean())
print("平均値に置き換え後：欠損値の数",mean_radius_fillna_m.isnull().sum())
print("平均値に置き換え後：データの数",len(mean_radius_fillna_m))
print("平均値に置き換え後：平均値",mean_radius_fillna_m.mean())
