#AI-TECHGYM-2-2-A-2
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
#display(df)

#カラムを取得
mean_radius = df["mean radius"]

#===オリジナルのメソッド===
#平均値
def original_mean(series):
    n     = len(series)
    sum_s = sum(series)
    return sum_s/n

#中央値
def original_median(series):
    n = len(series)
    return sorted(series)[int(n/2)]

#最頻値
def original_mode(series):
    count_hash = {}
    for s in series:
        if str(s) not in count_hash:
            count_hash[str(s)] = 1
        else:
            count_hash[str(s)] = count_hash[str(s)] + 1
    
    return max(count_hash, key=count_hash.get)

#平均からの偏差
def find_difference(series):
    mean = original_mean(series)
    diff = []

    for num in series:
        diff.append(num - mean)
    return diff

def original_var(series):
    diff = find_difference(series)
    
    #差の２乗
    squared_diff = []
    for d in diff:
        squared_diff.append(d**2)

    #分散
    return sum(squared_diff)/len(series)

#標準偏差
def original_std(series):
    return np.sqrt(original_var(series))

#平均
print("平均値(自前)",original_mean(mean_radius))

#中央値
print("中央値(自前)",original_median(mean_radius))

#最頻値
print("最頻値(自前)",original_mode(mean_radius))

#分散
print("分散(自前)",original_var(mean_radius))

#標準偏差
print("標準偏差(自前)",original_std(mean_radius))
