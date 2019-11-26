#AI-TECHGYM-N-13

import pandas as pd
import urllib

#Seaborn(表示のために読み込み)
import seaborn as sns

import matplotlib.pyplot as plt
%matplotlib inline

data = "http://archive.ics.uci.edu/ml/machine-learning-databases/balloons/adult+stretch.data"
balloons = pd.read_csv(data)

#indexを説明からつける
columns_name = ['color','size','act','age','inflated']
balloons.columns = columns_name

#表示確認
#display(balloons)

#カテゴリーごとの集計


# グラフの大きさを指定
plt.figure(figsize=(10, 10))

#colorのヒストグラムを表示
plt.subplot(2,2,1)


#colorカテゴリごとのage件数



#colorカテゴリごとのsize件数


