#AI-TECHGYM-N-2

import pandas as pd

#操作する数
head_num = 3
tail_num = 6

hand = {'性別'  :['男性','男性','女性','男性','女性','男性','女性','女性','男性','男性'],
        '年齢'  :['30代','20代','10代','10代','40代','50代','40代','10代','20代','10代'],
        '勝ち'  :[20,21, 4,60,14,10,12,19,12,14],
        '負け'  :[24,15,35, 3,35,29, 2,12,11,43],
        'あいこ':[15,40,34,29,14, 4,22,17,12,10]}

#データフレームの生成
hand_df = pd.DataFrame(hand)

#表示
display(hand_df)

#転置
display(hand_df.T)

#indexを変更して先頭三行の表示
hand_df2 = pd.DataFrame(hand,index=['e','b','a','d','c','f','g','h','i','j'])
display(hand_df2.head(head_num))

#末尾6行を転置、先頭3行にしてさらに転置する
display(hand_df2.tail(tail_num).T.head(head_num).T)
