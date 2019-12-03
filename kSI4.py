#AI-TECHGYM-2-9-A-2
#特徴量エンジニアリング

#インポート
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

#ファイルがなければ前の問題を実施する
title = "FIFA_data_pre.csv"
if not os.path.exists(title):
    print("Run Previous problem.")
else :
    print(title + " EXIST.")
    df=pd.read_csv('./FIFA_data_pre.csv')

#スタイルの指定
plt.style.use('fivethirtyeight')
sns.set(style = "dark", palette = "colorblind", color_codes = True)


#lbsの単位と取り除く
def extract_value_from(value):
  out = value.replace('lbs', '')
  return float(out)

#定義した処理を適用する
df['Weight'] = df['Weight'].apply(lambda x : extract_value_from(x))

#必要に応じて表示
#display(df['Weight'].head())

#体重
plt.figure(figsize = (15, 5))
sns.distplot(df['Weight'], color = 'green')
plt.xlabel('Weight for Players', fontsize = 16)
plt.ylabel('Count of the Players', fontsize = 16)
plt.title('Distribution of Weight of Players', fontsize = 20)
plt.tick_params(labelsize = 16)
plt.show()

def extract_value_from(Value):
    out = Value.replace('€', '')
    if 'M' in out:
        out = float(out.replace('M', ''))*1000000
    elif 'K' in Value:
        out = float(out.replace('K', ''))*1000
    return float(out)

df['Value'] = df['Value'].apply(lambda x: extract_value_from(x))
df['Wage'] = df['Wage'].apply(lambda x: extract_value_from(x))
df['Release Clause'] = df['Release Clause'].apply(lambda x: extract_value_from(x))

#収入
plt.figure(figsize = (15, 5))
sns.distplot(df['Wage'], color = 'blue')
plt.xlabel('Wage Range for Players', fontsize = 16)
plt.ylabel('Count of the Players', fontsize = 16)
plt.title('Distribution of Wages of Players', fontsize = 20)
plt.tick_params(labelsize = 16)
plt.show()

#CSVに書き出し
df.to_csv('./FIFA_data_pre2.csv')
