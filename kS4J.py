#Tech-Gym-11-17
#モデル比較（異なるデータ)

#データの準備
import pandas as pd
from sklearn.datasets import load_wine
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
import lightgbm as lgb

#性能評価
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score

wine = load_wine()
X_train, X_test, y_train, y_test = train_test_split(
                                                    wine.data, wine.target, stratify = wine.target, random_state=0)

models = {
    'KNN': KNeighborsClassifier(),
    'LogisticRegression': LogisticRegression(random_state=0,solver='liblinear',multi_class='auto'),
    'DecisionTree': DecisionTreeClassifier(random_state=0),
    'SVM': SVC(random_state=0,gamma='scale'),
    'RandomForest': RandomForestClassifier(random_state=0,n_estimators=1000),
    'GradientBoost': GradientBoostingClassifier(random_state=0),
    'LightGBM' : lgb.LGBMClassifier()
}

scores = {}
for model_name, model in models.items():
    model.fit(X_train, y_train)
    scores[(model_name, 'train_score')] = model.score(X_train, y_train)
    scores[(model_name, 'test_score')] = model.score(X_test, y_test)

#表示
display(pd.Series(scores).unstack())

# feature_importmnces属性を取得
s = pd.Series(models['LightGBM'].feature_importances_,index=wine.feature_names)

# 取得した値を降順に表示
s.sort_values(ascending=False).plot.bar(color='C0')
