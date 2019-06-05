#AI-TECHGYM-N-14

import pandas as pd
import urllib

#Seaborn
import seaborn as sns

import matplotlib.pyplot as plt
%matplotlib inline

#データの取得
data = "https://archive.ics.uci.edu/ml/machine-learning-databases/tic-tac-toe/tic-tac-toe.data"
TTT = pd.read_csv(data)

txt= "https://archive.ics.uci.edu/ml/machine-learning-databases/tic-tac-toe/tic-tac-toe.names"
urllib.request.urlretrieve(txt, './tic-tac-toe.names')

#説明文の表示(必要であれば表示)
#f = open("./tic-tac-toe.names","r")
#for line in f:
#    print(line)
#f.close()

#データの個数や型を確認
display(TTT.info())

#indexを説明からつける
columns_name = ['top-left','top-middle','top-right',
                'middle-left','middle-middle','middle-right',
                'bottom-left','bottom-middle','bottom-right','P-N']
TTT.columns = columns_name

#必要であれば表示して確認
#display(TTT)

display(pd.crosstab(TTT['middle-middle'], TTT['P-N']))

# グラフの大きさを指定
plt.figure(figsize=(10, 10))

#真ん中をとったときの調査
sns.countplot(x='P-N', hue='middle-middle', hue_order=['x','o','b'],data=TTT)
