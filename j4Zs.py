#AI-TECHGYM-N-14

import pandas as pd
import urllib

#Seaborn
import seaborn as sns

import matplotlib.pyplot as plt
%matplotlib inline

#データの取得
data = "https://archive.ics.uci.edu/ml/machine-learning-databases/tic-tac-toe/tic-tac-toe.data"
TTT = 

txt= "https://archive.ics.uci.edu/ml/machine-learning-databases/tic-tac-toe/tic-tac-toe.names"


#説明文の表示(必要であれば表示)
#f = open("./tic-tac-toe.names","r")
#for line in f:
#    print(line)
#f.close()

#データの個数や型を確認


#indexを説明からつける
columns_name = ['top-left','top-middle','top-right',
                'middle-left','middle-middle','middle-right',
                'bottom-left','bottom-middle','bottom-right','P-N']


#必要であれば表示して確認
#display(TTT)



# グラフの大きさを指定
plt.figure(figsize=(10, 10))

#真ん中をとったときの調査

