#AI-TECHGYM-N-7

import pandas as pd

num = ['0','1','2','3','4','5','6','7','8','9']
add_num = ['10']
feature =['id','gender','age','address','hobby','job','win','lose','draw']

hand1 = {'番号'  :['100','101','102','103','104','105','106','107','108','109'],
         '性別'  :['男性','男性','女性','男性','女性','男性','女性','女性','男性','男性'],
         '年齢'  :['30代','20代','10代','10代','40代','50代','40代','10代','20代','10代'],
         '住所'  :['東京','大阪','名古屋','北海道','東京','鹿児島','大阪','名古屋','東京','大阪'],
         '趣味'  :['野球','ルーレット','じゃんけん','野球','ルーレット','野球','じゃんけん','ルーレット','野球','じゃんけん'],
         '仕事'  :['IT','医療','弁護士','事務','事務','弁護士','IT','IT','IT','事務'],
         '勝ち'  :[20,21, 4,60,14,10,12,19,12,14],
         '負け'  :[24,15,35, 3,35,29, 2,12,11,43],
         'あいこ':[15,40,34,29,14, 4,22,17,12,10]}
hand_df1 = pd.DataFrame(hand1)

#index,columnsの指定
hand_df1.index = num
hand_df1.index.names = ['NUM']
hand_df1.columns = [feature]
hand_df1.columns.names = ['feature']

#必要であれば表示して確認する
#display(hand_df1)

hand2 = {'id':['104'],
         'gender':['女性'],
         'age':['40代'],
         'address':['東京'],
         'hobby':['ルーレット'],
         'job':['事務'],
         'win':[14],
         'lose':[35],
         'draw':[14]}

#index,columnsの指定
hand_df2 = pd.DataFrame(hand2)
hand_df2.index = add_num
hand_df2.index.names = ['NUM']
hand_df2.columns = [feature]
hand_df2.columns.names = ['feature']
hand_df2 = hand_df1.append(hand_df2)

