#AI-TECHGYM-3-18-A-1
#回帰問題と分類問題

#インポート
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_breast_cancer

#データロード
cancer = load_breast_cancer()

#データ分割
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, stratify = cancer.target, test_size=0.3)

#モデル
models = {
    'tree1': DecisionTreeClassifier(criterion='entropy', max_depth=3),
    'tree2': DecisionTreeClassifier(criterion='entropy', max_depth=5),
    'tree3': DecisionTreeClassifier(criterion='entropy', max_depth=10),
    'tree4': DecisionTreeClassifier(criterion='gini', max_depth=3),
    'tree5': DecisionTreeClassifier(criterion='gini', max_depth=5),
    'tree6': DecisionTreeClassifier(criterion='gini', max_depth=10)
}

scores = {}
for model_name, model in models.items():
    model.fit(X_train,y_train)
    scores[(model_name, 'train')] = model.score(X_train, y_train)
    scores[(model_name, 'test')] = model.score(X_test, y_test)

#表示
display(pd.Series(scores).unstack())
