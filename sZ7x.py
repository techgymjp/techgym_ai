#Tech-Gym-11-15
#モデル比較:random seed averaging

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

#random seed averaging:Voting
from sklearn.ensemble import VotingClassifier

#KFoldで10分割
kf = KFold(n_splits=10,shuffle=True,random_state=0)

#データの読み出し
cancer = load_breast_cancer()
X_set = cancer.data
y_set = cancer.target

n_set = 1000

estimators = [
              ("rf1",RandomForestClassifier(random_state=1,n_estimators=n_set)),
              ("rf2",RandomForestClassifier(random_state=2,n_estimators=n_set)),
              ("rf3",RandomForestClassifier(random_state=3,n_estimators=n_set)),
              ("rf4",RandomForestClassifier(random_state=4,n_estimators=n_set)),
              ("rf5",RandomForestClassifier(random_state=5,n_estimators=n_set))
              ]

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
    
    #ランダムフォレストのvotingでの学習
    voting = VotingClassifier(estimators)
    voting.fit(X_train_std,y_train)
    
    scores_std[(i, 'train_score')] = voting.score(X_train_std, y_train)
    scores_std[(i, 'test_score')] = voting.score(X_test_std, y_test)

#結果を表示
df = pd.Series(scores_std).unstack()
display(df)

#最大を表示
print('Score:{:.3f}'.format(df['test_score'].max()))
