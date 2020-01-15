#AI-TECHGYM-4-7-Q-1(AI-TECHGYM-3-20-Q-1)
#回帰問題と分類問題

#インポート
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, stratify = iris.target, random_state=0)

models = {
    'AdaBoost': ,
    'GradientBoost':
}

#正解率
scores = {}
for model_name, model in models.items():
    model.fit(X_train, y_train)
    scores[(model_name, 'train_score')] =
    scores[(model_name, 'test_score')] =

#表示
display(pd.Series(scores).unstack())
