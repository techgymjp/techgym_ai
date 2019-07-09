#Tech-Gym-7-6
#ロジスティクス回帰の性能評価

# データやモデルを構築するためのライブラリ等のインポート
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

#性能評価
from sklearn.metrics import roc_auc_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

# 乳がんのデータを読み込み
cancer = load_breast_cancer()

# 訓練データとテストデータに分ける
X_train, X_test, y_train, y_test = train_test_split(
                                                    cancer.data, cancer.target, test_size=0.5, random_state=66)

# ロジスティクス回帰による予測確率の取得
model = LogisticRegression(random_state=0,solver='liblinear')
model.fit(X_train, y_train)

# 予測確率を取得
y_pred_rate = model.predict_proba(X_test)[:,1]

#ACUの計算
auc = roc_auc_score(y_test, y_pred_rate)

#ACU表示
print('{} AUC:{:.3f}'.format(model.__class__.__name__ , auc))

#テストデータの予測値
y_pred = model.predict(X_test)

#性能評価指標
print('Confution matrix:\n{}'.format(confusion_matrix(y_test, y_pred)))
print('正解率:{:.3f}'.format(accuracy_score(y_test, y_pred)))
print('適合率:{:.3f}'.format(precision_score(y_test, y_pred)))
print('再現率:{:.3f}'.format(recall_score(y_test, y_pred)))
print('F1値:{:.3f}'.format(f1_score(y_test, y_pred)))
