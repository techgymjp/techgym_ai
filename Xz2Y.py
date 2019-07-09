#Tech-Gym-11-12
#アンサンブル学習：特徴量

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

scores = {}
for model_name, model in models.items():
    model.fit(X_train, y_train)
    scores[(model_name, 'train_score')] = model.score(X_train, y_train)
    scores[(model_name, 'test_score')] = model.score(X_test, y_test)

#表示
display(pd.Series(scores).unstack())

#標準化
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

scores_std = {}
for model_name, model in models.items():
    model.fit(X_train_std,y_train)
    scores_std[(model_name, 'train_score_std')] = model.score(X_train_std, y_train)
    scores_std[(model_name, 'test_score_std')] = model.score(X_test_std, y_test)

#表示
display(pd.Series(scores_std).unstack())

# feature_importmnces属性を取得
s = pd.Series(models['RandomForest'].feature_importances_,
              index=cancer.feature_names)

# 取得した値を降順に表示
s.sort_values(ascending=False).plot.bar(color='C0')

