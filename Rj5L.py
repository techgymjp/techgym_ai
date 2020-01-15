#AI-TECHGYM-3-13-A-1
#回帰問題と分類問題

#インポート
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

#WARNING OFF
import warnings
warnings.filterwarnings('ignore')

#データロード
iris = load_iris()

#必要なら表示
#print(iris.DESCR)

#データフレーム
tmp_data = pd.DataFrame(iris.data, columns=iris.feature_names)
tmp_data["target"] = iris.target

#Setosa(0),Versicolour(1)のみのデータにする
data_iris = tmp_data[tmp_data['target'] <= 1]

#必要なら表示
#print(data_iris.head())
#print(data_iris.shape)

#グラフサイズ
plt.figure(figsize=(5,15))

plt.subplot(4, 1, 1)
plt.scatter(data_iris.iloc[:, 0], data_iris.iloc[:, 1], c=data_iris["target"])
plt.title('sepal length (cm) vs sepal width (cm)')

plt.subplot(4, 1, 2)
plt.scatter(data_iris.iloc[:, 1], data_iris.iloc[:, 2], c=data_iris["target"])
plt.title('sepal width (cm) vs petal length (cm)')

plt.subplot(4, 1, 3)
plt.scatter(data_iris.iloc[:, 2], data_iris.iloc[:, 3], c=data_iris["target"])
plt.title('petal length (cm) vs petal width (cm)')

plt.subplot(4, 1, 4)
plt.scatter(data_iris.iloc[:, 0], data_iris.iloc[:, 3], c=data_iris["target"])
plt.title('sepal length (cm) vs petal width (cm)')

plt.tight_layout()
plt.show()

#ロジスティック回帰
logit = LogisticRegression(solver='liblinear')

#説明変数、目的変数
x_column_list = ['sepal length (cm)']
y_column_list = ['target']

x = data_iris[x_column_list]
y = data_iris[y_column_list]

#学習
logit.fit(x, y)

#学習されたパラメータ
print('w1',logit.coef_)
print('w0',logit.intercept_)

#変数の確認
print(data_iris.columns)

#複数の説明変数があるモデル
logit_multi = LogisticRegression(solver='liblinear')

x_column_list = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
y_column_list = ['target']

x = data_iris[x_column_list]
y = data_iris[y_column_list]

#学習
logit_multi.fit(x, y)

#学習されたパラメータ
print('w1',logit_multi.coef_)
print('w0',logit_multi.intercept_)

#目的変数、説明変数
x_column_list = ['sepal width (cm)']
y_column_list = ['target']

#学習データ、テストデータ
X_train, X_test, y_train, y_test = train_test_split(data_iris[x_column_list], data_iris[y_column_list], test_size=0.2)

#モデル、学習
logit2 = LogisticRegression(solver='liblinear')
logit2.fit(X_train, y_train)

#学習パラメータ(必要なら表示)
#print(logit2.coef_)
#print(logit2.intercept_)

#正解率
y_pred = logit2.predict(X_test)
print('正解率(単数)',accuracy_score(y_test, y_pred))

#目的変数、説明変数
x_column_list = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
y_column_list = ['target']

#学習データ、テストデータ
X_train, X_test, y_train, y_test = train_test_split(data_iris[x_column_list], data_iris[y_column_list], test_size=0.2)

#モデル、学習
logit_multi2 = LogisticRegression(solver='liblinear')
logit_multi2.fit(X_train, y_train)

#学習パラメータ(必要なら表示)
#print(logit_multi2.coef_)
#print(logit_multi2.intercept_)

#正解率
y_pred = logit_multi2.predict(X_test)
print('正解率(複数)',accuracy_score(y_test, y_pred))
