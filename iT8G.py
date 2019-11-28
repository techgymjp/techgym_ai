#AI-TECHGYM-2-9-Q
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

#必要に応じて表示
#display(df.head())
#display(df.columns)
