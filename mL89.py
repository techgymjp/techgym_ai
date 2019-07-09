#Tech-Gym-7-20
#モデル比較（異なるデータ：手書き文字)

#データの準備
import pandas as pd
import numpy as np

#可視化ライブラリ
import matplotlib.pyplot as plt
%matplotlib inline

# 分析対象データ
from sklearn.datasets import load_digits

#データの読み込み
digits = load_digits()

# データの分割（学習データとテストデータ分ける）
from sklearn.model_selection import train_test_split

# 学習モデル
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
import lightgbm as lgb

#評価指標
from sklearn.metrics import accuracy_score

#グリッドサーチ
from sklearn.model_selection import GridSearchCV

# 説明変数
X = digits.data
# 目的変数
Y = digits.target

# 学習データとテストデータの分割
X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=0)

models = {
    'KNN': KNeighborsClassifier(n_neighbors=3),
    'LogisticRegression': LogisticRegression(random_state=0,solver='liblinear',multi_class='auto'),
    'DecisionTree': DecisionTreeClassifier(random_state=0),
    'SVM': SVC(random_state=0,gamma='scale'),
    'RandomForest': RandomForestClassifier(random_state=0,n_estimators=1000),
    'GradientBoost': GradientBoostingClassifier(random_state=0),
    'LightGBM' : lgb.LGBMClassifier(random_state=0,n_estimators=1000)
}

scores = {}
for model_name, model in models.items():
    model.fit(X_train, y_train)
    pred_y = model.predict(X_test)
    confusion_m = confusion_matrix(y_test,pred_y)
    confusion_df = pd.DataFrame(confusion_m)
    
    #必要であれば表示
    #display(confusion_df)
    scores[(model_name, 'train_score')] = model.score(X_train, y_train)
    scores[(model_name, 'test_score')] = model.score(X_test, y_test)

#結果を表示
#display(pd.Series(scores).unstack())

# GridSearchCVクラスに与えるパラメータを準備
param_grid = { 'C': np.logspace(-5, 5, num=11)
    ,'gamma':np.logspace(-5, 5, num=11)}

# GridSearchCVクラスの初期化
gs = GridSearchCV(estimator=SVC(),
                  param_grid=param_grid,
                  cv=5,iid='False')

# ハイパーパラメータの組み合わせの検証とベストモデルの構築
gs.fit(X_train,y_train)

#GridSearchデータの追加
scores[('SVN(GridSearch)', 'train_score')] = gs.score(X_train, y_train)
scores[('SVN(GridSearch)', 'test_score')] = gs.score(X_test, y_test)

#結果の表示
display(pd.Series(scores).unstack())
