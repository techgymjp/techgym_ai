#AI-TECHGYM-4-6-Q-1(AI-TECHGYM-3-19-Q-1)
#回帰問題と分類問題

#インポート
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

#データロード
iris = load_iris()

#データ分割
X, Y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)

#モデル
clf =

#学習
clf.fit(X_train, y_train)

#評価
y_pred =
print('正解率(test)')

#特徴量の重要度
importances =
print('特徴量',importances)

#特徴
features = np.array(iris.feature_names)

#プロット
indices = np.argsort(importances)
plt.figure(figsize=(8,6))
plt.barh(range(len(indices)), importances[indices], color='b', align='center')
plt.yticks(range(len(indices)), features[indices])
