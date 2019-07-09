#Tech-Gym-11-9
#グリッドサーチ

# データやモデルを構築するためのライブラリ等のインポート
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

#学習モデル
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

#性能評価
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

#グリッドサーチ
from sklearn.model_selection import GridSearchCV

# 乳がんのデータを読み込み
cancer = load_breast_cancer()

# 訓練データとテストデータに分ける
X_train, X_test, y_train, y_test = train_test_split(
                                                    cancer.data, cancer.target, test_size=0.5, random_state=66)

# GridSearchCVクラスに与えるパラメータを準備
param_grid = { 'C': np.logspace(-5, 5, num=11)
    ,'gamma':np.logspace(-5, 5, num=11)}

# GridSearchCVクラスの初期化
gs = GridSearchCV(estimator=SVC(),
                  param_grid=param_grid,
                  cv=5,iid='False')

# ハイパーパラメータの組み合わせの検証とベストモデルの構築
gs.fit(X_train,y_train)

# 表示
print('Best cross validation score:{:.3f}'.format(gs.best_score_))
print('Best parameters:{}'.format(gs.best_params_))
print('Test score:{:.3f}'.format(gs.score(X_test,y_test)))

#テストデータの予測値
y_pred = gs.predict(X_test)

#性能評価指標
print('Confution matrix:\n{}'.format(confusion_matrix(y_test, y_pred)))
print('正解率:{:.3f}'.format(accuracy_score(y_test, y_pred)))
print('適合率:{:.3f}'.format(precision_score(y_test, y_pred)))
print('再現率:{:.3f}'.format(recall_score(y_test, y_pred)))
print('F1値:{:.3f}'.format(f1_score(y_test, y_pred)))


