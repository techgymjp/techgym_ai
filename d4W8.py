#Tech-Gym-11-3
#性能評価指標

#データフレーム使用のためインポート
import pandas as pd

#混合行列、性能評価指標を使うためにインポート
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

#0がPositive,1がNegative
y_true = [0,0,1,0,0,0,1,0,0,1,1,1,0,0,1,1,0,0,0,0,0,0,1,0,0]
y_pred = [0,0,0,0,1,0,1,0,0,1,1,1,0,0,1,0,0,0,1,1,1,0,0,0,0]

confmat = confusion_matrix(y_true, y_pred)
print(confmat)

#正解率：全体に対して予測が当たった割合
accuracy = accuracy_score(y_true, y_pred)
print('正解率:{:.3f}'.format(accuracy))

#適合率：1と予測した中で実際にどれだけ1であったかの割合
precision = precision_score(y_true, y_pred)
print('適合率:{:.3f}'.format(precision))

#再現率：実際は1のデータのうち正しく1と予測できた割合
recall = recall_score(y_true, y_pred)
print('再現率:{:.3f}'.format(recall))

# F1スコアの計算：適合率と再現率の調和平均
f1 = f1_score(y_true, y_pred)
print('F1値:{:.3f}'.format(f1))

#caseA:もしWebサービスのレコメンドの購買予測と購買実績だった場合
#レコメンドしたものを買わなかった vs レコメンドしなかったものを買った

reco = {'レコメンドした'        :['○','おすすめの信頼性がない'],
    'レコメンドしなかった'  :['うまくおすすめ出来なかった','×']}

#説明の表示
reco_df = pd.DataFrame(reco,index=['買った','買わなかった'])
display(reco_df)

#caseB:もし癌検診の診断予測と診断結果だった場合
#癌と予測して癌でなかった vs 癌と予測しなくて癌だった

can = {'癌と診断した'        :['○','間違って癌と診断'],
    '癌と診断しなかった'  :['癌の発見を見逃す','×']}

#説明の表示
can_df = pd.DataFrame(can,index=['癌だった','癌でなかった'])
display(can_df)

#考察
print("caseA:うまくおすすめ出来なかったことよりも、おすすめの信頼性がないようにしないので、適合率を重視する")
print("caseB:間違って癌と診断することよりも、癌の発見を見逃さないようにするので、再現率を重視する")

