#Tech-Gym-11-4
#性能評価指標

#ROC曲線の形状は、閾値を（1.0を超える値から）徐々に小さくしたとき、
#原点から真陽性率だけが上昇するのが理想
#座標 (1,1)に水平移動するものが最適理想曲線
#より膨らみを持つことが期待

#AUC : Area Under Curves
#ROC曲線と横軸で囲まれる面積の値
#最適理想曲線では1.0、予測確率がランダムな場合は0.5となる

#データフレーム使用のためインポート
import pandas as pd

# 可視化ライブラリ
import matplotlib.pyplot as plt
%matplotlib inline

#混合行列、性能評価指標を使うためにインポート
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score

#0がPositive,1がNegative
y_true  = [0,0,1,0,0,0,1,0,0,1,1,1,0,0,1,1,0,0,0,0,0,0,1,0,0]
y_pred  = [0,0,0,0,1,0,1,0,0,1,1,1,0,0,1,0,0,0,1,1,1,0,0,0,0]
y_pred2 = [0,0,1,0,0,1,1,0,0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0]

# 偽陽性率と真陽性率の算出
fpr, tpr, thresholds = roc_curve(y_true, y_pred)

# AUCの算出：
auc = roc_auc_score(y_true, y_pred)

# ROC曲線の描画
plt.figure(figsize=(10,10))
plt.plot(fpr, tpr, color='red', label='ROC curve (area = %.3f)' % auc)
plt.plot([0, 1], [0, 1], color='black', linestyle='--')

plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False positive rate')
plt.ylabel('True positive rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="best")

# 偽陽性率と真陽性率の算出
fpr, tpr, thresholds = roc_curve(y_true, y_pred2)

# AUCの算出
auc = roc_auc_score(y_true, y_pred2)

# ROC曲線の描画
plt.plot(fpr, tpr, color='blue', label='ROC curve (area = %.3f)' % auc)

plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False positive rate')
plt.ylabel('True positive rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="best")

# 偽陽性率と真陽性率の算出
fpr, tpr, thresholds = roc_curve(y_true, y_true)

# AUCの算出
auc = roc_auc_score(y_true, y_true)

# ROC曲線の描画
plt.plot(fpr, tpr, color='green', label='ROC curve (area = %.3f)' % auc)

plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False positive rate')
plt.ylabel('True positive rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="best")

