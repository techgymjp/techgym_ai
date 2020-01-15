#AI-TECHGYM-3-21-A-1
#回帰問題と分類問題

#インポート
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

#データロード
iris = load_iris()

#データ分割
X, Y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)

#モデル
svm = SVC(C=1.0, gamma=0.001)

#学習
svm.fit(X_train, y_train)

#評価
print('正解率(train):', svm.score(X_train, y_train))
print('正解率(test):', svm.score(X_test, y_test))
