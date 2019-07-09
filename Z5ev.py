#Tech-Gym-11-2
#混合行列

#データフレーム使用のためインポート
import pandas as pd

#混合行列を使うためにインポート
from sklearn. metrics import confusion_matrix

#0がPositive,1がNegative
y_true = [0,0,1,0,0,0,1,0,0,1,1,1,0,0,1,1,0,0,0,0,0,0,1,0,0]
y_pred = [0,0,0,0,1,0,1,0,0,1,1,1,0,0,1,0,0,0,1,1,1,0,0,0,0]

confmat = confusion_matrix(y_true, y_pred)
print(confmat)

#正解率：全体に対して予測が当たった割合
accuracy = (confmat[0, 0] + confmat[1, 1]) / confmat.sum()
print('正解率:{:.3f}'.format(accuracy))

#適合率：1と予測した中で実際にどれだけ1であったかの割合
#例えば、非常ベルが鳴ったときに、実際に火事だった場合を知りたい
precision = (confmat[1,1])/confmat[:, 1].sum()
print('適合率:{:.3f}'.format(precision))

#再現率：実際は1のデータのうち正しく1と予測できた割合
recall = (confmat[1,1])/confmat[1, :].sum()
print('再現率:{:.3f}'.format(recall))

# F1スコアの計算：適合率と再現率の調和平均
f1 = 2 * (precision * recall)/(precision + recall)
print('F1値:{:.3f}'.format(f1))

