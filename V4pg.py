#Tech-Gym-11-1
#混同行列

#モデルの予測と実績の組み合わせを考えてみる
confusion = {'正例(予測)'  :['True Positive（TP）','False Positive（FP）'],
    '負例(予測)'  :['False Negative（FN）','True Negative（TN）']}

#説明の表示
conf_df = pd.DataFrame(confusion,index=['正例(実績)','負例(実績)'])
display(conf_df)

#0がPositive,1がNegative
y_true = [0,0,1,0,0,0,1,0,0,1,1,1,0,0,1,1,0,0,0,0,0,0,1,0,0]
y_pred = [0,0,0,0,1,0,1,0,0,1,1,1,0,0,1,0,0,0,1,1,1,0,0,0,0]

