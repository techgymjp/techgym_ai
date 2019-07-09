#Tech-Gym-11-7
#ハイパーパラメータチューニング

#グラフ描画
import matplotlib.pyplot as plt
%matplotlib inline

#データ準備
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

# グラフ描画用の空リストを用意します
svm_train_accuracy = []
svm_test_accuracy = []
log_train_accuracy = []
log_test_accuracy = []

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
