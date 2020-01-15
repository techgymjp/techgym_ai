#AI-TECHGYM-4-5-Q-1(AI-TECHGYM-3-18-Q-1)
#回帰問題と分類問題

#インポート
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_breast_cancer

#データロード
cancer =

#データ分割
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, stratify = cancer.target, test_size=0.3)

#モデル
models = {
    'tree1': ,
    'tree2': ,
    'tree3': ,
    'tree4': ,
    'tree5': ,
    'tree6':
}

scores = {}
for model_name, model in models.items():
    model.fit(X_train,y_train)
    scores[(model_name, 'train')] =
    scores[(model_name, 'test')] = 

#表示
display(pd.Series(scores).unstack())
