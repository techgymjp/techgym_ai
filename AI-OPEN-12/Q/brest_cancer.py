import joblib
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

#乳がんデータの取得
cancer = load_breast_cancer()
X, Y = cancer.data, cancer.target
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)

#決定木のモデル
clf = DecisionTreeClassifier(max_depth=5)
clf.fit(X_train, y_train)

with open("brest_cancer.pkl", "wb") as f:  
  joblib.dump(clf, f, compress=3)