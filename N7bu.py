#Tech-Gym-11-7
#ハイパーパラメータチューニング

#グラフ描画
import matplotlib.pyplot as plt
%matplotlib inline

#学習モデル
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

#データ準備
from sklearn.datasets import load_breast_cancer
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

# Cの値の範囲を設定します(ここでは1e-5,1e-4,1e-3,0.01,0.1,1,10,100,1000,10000)
C_list = [10 ** i for i in range(-5, 5)]

# グラフ描画用の空リストを用意します
svm_train_accuracy = []
svm_test_accuracy = []
log_train_accuracy = []
log_test_accuracy = []

#
for C in C_list:
    model1 = SVC(C=C, kernel='linear', probability=True, random_state=0)
    model1.fit(X_train, y_train)
    svm_train_accuracy.append(model1.score(X_train, y_train))
    svm_test_accuracy.append(model1.score(X_test, y_test))
    
    model2 = LogisticRegression(C=C,solver='liblinear',random_state=0)
    model2.fit(X_train, y_train)
    log_train_accuracy.append(model2.score(X_train, y_train))
    log_test_accuracy.append(model2.score(X_test, y_test))

#グラフを準備
#semilogx() は x のスケールを 10 の x 乗のスケールに変更します

fig = plt.figure()
plt.subplots_adjust(wspace=0.4, hspace=0.4)
ax = fig.add_subplot(1, 1, 1)
ax.grid(True)
ax.set_title("SVM")
ax.set_xlabel("C")
ax.set_ylabel("accuracy")
ax.semilogx(C_list, svm_train_accuracy, label="accuracy of train_data")
ax.semilogx(C_list, svm_test_accuracy, label="accuracy of test_data")
ax.legend()
ax.plot()
plt.show()
fig2 =plt.figure()
ax2 = fig2.add_subplot(1, 1, 1)
ax2.grid(True)
ax2.set_title("LogisticRegression")
ax2.set_xlabel("C")
ax2.set_ylabel("accuracy")
ax2.semilogx(C_list, log_train_accuracy, label="accuracy of train_data")
ax2.semilogx(C_list, log_test_accuracy, label="accuracy of test_data")
ax2.legend()
ax2.plot()
plt.show()
