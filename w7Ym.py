#AI-TECHGYM-N-12

import pandas as pd

#スクレイピングのために読み込み
import urllib

#データをCSVファイルから読み込む
data = "http://archive.ics.uci.edu/ml/machine-learning-databases/balloons/adult+stretch.data"


#データの説明文をダウンロードする
txt= "http://archive.ics.uci.edu/ml/machine-learning-databases/balloons/balloons.names"


#説明文の表示(必要であれば表示)
#f = open("./balloons.names","r")
#for line in f:
#    print(line)
#f.close()

#データの個数や型を確認


#説明文からindexをつける
columns_name = ['color','size','act','age','inflated']


#表示
display(balloons)

