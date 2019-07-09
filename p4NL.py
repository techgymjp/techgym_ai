#Tech-Gym-11-14
#交差検証:KFold
#k-fold法は、データをk個に分割し、うちk-1個で訓練し、1個でテストする。
#そのk通りの訓練およびテストを試して、Scoreの平均値をその分類器のScoreとする

#データの準備
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

#可視化ライブラリ
import matplotlib.pyplot as plt
%matplotlib inline

#学習モデル
from sklearn.ensemble import RandomForestClassifier

#性能評価
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score

# 標準化のためのモジュール
from sklearn.preprocessing import StandardScaler

#KFold
from sklearn.model_selection  import KFold

#KFoldで分割
kf = KFold(n_splits=20,shuffle=True,random_state=0)

#データの読み出し
cancer = load_breast_cancer()
X_set = cancer.data
y_set = cancer.target

scores_std = {}

for i,(train_index,test_index) in enumerate(kf.split(X_set,y_set)):
    #訓練データ、テストデータの分割
    #print("TRAIN:", train_index, "TEST:", test_index)
    X_train,X_test = X_set[train_index],X_set[test_index]
    y_train,y_test = y_set[train_index],y_set[test_index]
    
    #標準化
    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)
    
    #ランダムフォレストでの学習
    model = RandomForestClassifier(random_state=0,n_estimators=1000)
    model.fit(X_train_std,y_train)
    
    scores_std[(i, 'train_score')] = model.score(X_train_std, y_train)
    scores_std[(i, 'test_score')] = model.score(X_test_std, y_test)

#結果を表示
df = pd.Series(scores_std).unstack()
display(df)

#平均を表示
print('Score:{:.3f}'.format(df['test_score'].mean()))
