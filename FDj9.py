#AI-TECHGYM-4-4-Q-1(AI-TECHGYM-3-17-Q-1)
#回帰問題と分類問題

#インポート
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_breast_cancer

#データロード
cancer = load_breast_cancer()

#データ分割
X, Y =
X_train, X_test, y_train, y_test =

#決定木のモデル
clf =

# 学習
clf.fit(X_train, y_train)

# 評価
y_pred =
print('正解率(決定木)')

###分割ルールの可視化###

###インストールしていないときは以下を実行(MaxOSの場合)###
#!conda install -c conda-forge python-graphviz
#!pip install graphviz
#!pip install dtreeviz

from dtreeviz.trees import dtreeviz

viz = dtreeviz(clf, X, Y,
  feature_names = cancer.feature_names,
  target_name = 'judge',
  class_names=[str(i) for i in cancer.target_names],
  )

display(viz)

#保存する場合
viz.save("cancer.svg")
