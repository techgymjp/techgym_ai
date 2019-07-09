#Tech-Gym-11-4
#性能評価指標

#データフレーム使用のためインポート
import pandas as pd

# 可視化ライブラリ
import matplotlib.pyplot as plt
%matplotlib inline

#0がPositive,1がNegative
y_true  = [0,0,1,0,0,0,1,0,0,1,1,1,0,0,1,1,0,0,0,0,0,0,1,0,0]
y_pred  = [0,0,0,0,1,0,1,0,0,1,1,1,0,0,1,0,0,0,1,1,1,0,0,0,0]
y_pred2 = [0,0,1,0,0,1,1,0,0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0]

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
