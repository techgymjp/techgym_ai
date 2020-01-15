#AI-TECHGYM-3-20-A-1
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
    'AdaBoost': AdaBoostClassifier(n_estimators=50, learning_rate=1.0),
    'GradientBoost': GradientBoostingClassifier()
}

#正解率
scores = {}
for model_name, model in models.items():
    model.fit(X_train, y_train)
    scores[(model_name, 'train_score')] = model.score(X_train, y_train)
    scores[(model_name, 'test_score')] = model.score(X_test, y_test)

#表示
display(pd.Series(scores).unstack())
