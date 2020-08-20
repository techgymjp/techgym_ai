#AI-TECHGYM-2-8-A-1
#特徴量エンジニアリング

#インポート
import pandas as pd
import os
import urllib.request

#ファイルがなければダウンロードする
title = "FIFA_df.csv"
if not os.path.exists(title):
    print(title + " DOWNLOAD.")
    url = "https://raw.githubusercontent.com/amanthedorkknight/fifa18-all-player-statistics/master/2019/data.csv"
    urllib.request.urlretrieve(url,"{0}".format(title))
else :
    print(title + " EXIST.")

df=pd.read_csv('./FIFA_df.csv')

#必要に応じて表示
display(df.head())

#欠損値があるcolumnsの確認
FIFA_isnull_sum = df.isnull().sum()
df_nan = pd.DataFrame(FIFA_isnull_sum[FIFA_isnull_sum > 0])

#NaNがあるcolumnsを表示
display(df_nan.index)
