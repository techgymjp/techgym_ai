#AI-TECHGYM-2-8-Q
#特徴量エンジニアリング

#インポート
import pandas as pd
import os
import urllib.request

#ファイルがなければダウンロードする
title = "FIFA_data.csv"
if not os.path.exists(title):
    print(title + " DOWNLOAD.")
    url = "https://raw.githubusercontent.com/amanthedorkknight/fifa18-all-player-statistics/master/2019/data.csv"
    urllib.request.urlretrieve(url,"{0}".format(title))
else :
    print(title + " EXIST.")

df=pd.read_csv('./FIFA_data.csv')
