#Tech-Gym-11-13
#交差検証

#データの準備
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

#可視化ライブラリ
import matplotlib.pyplot as plt
%matplotlib inline

#学習モデル
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import  DecisionTreeClassifier
from sklearn.neighbors import  KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import cross_val_score

#性能評価
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score

# 標準化のためのモジュール
from sklearn.preprocessing import StandardScaler

cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
                                                    cancer.data, cancer.target,test_size=0.5, random_state=66)

models = {
    'KNN': KNeighborsClassifier(),
    'LogisticRegression': LogisticRegression(random_state=0,solver='liblinear',multi_class='auto'),
    'DecisionTree': DecisionTreeClassifier(random_state=0),
    'SVM': SVC(random_state=0,gamma='scale'),
    'RandomForest': RandomForestClassifier(random_state=0,n_estimators=1000),
    'GradientBoost': GradientBoostingClassifier(random_state=0)
}

#標準化
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

scores_std = {}
scores_raw = {}
for model_name, model in models.items():
    model.fit(X_train_std,y_train)
    scores = cross_val_score(model, cancer.data, cancer.target, cv=10)
    scores_raw[(model_name, 'scores')] = scores
    scores_std[(model_name, 'scores:mean')] = scores.mean()
    scores_std[(model_name, 'scores:std')] = scores.std()

#結果を表示
df = pd.DataFrame(scores_raw)
display(df.T)

#平均と標準偏差を表示
display(pd.Series(scores_std).unstack())

