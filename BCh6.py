#AI-TECHGYM-2-6-A-1
#特徴量エンジニアリング

#インポート
import pandas as pd

#読み込みデータ
pg_data = {'0':['Python'],'1':['Ruby'],'2':['PHP'],'3':['Java'],'4':['JavaScript']}
df_row = pd.DataFrame(pg_data)
df = df_row.T
#display(df)

#one hot encoding
df_c = pd.get_dummies(df)

#表示用並び替え
df_d = df_c.iloc[:,[3,4,2,0,1]]
display(df_d)

#columnを設定して、値を取得
new_df = pd.DataFrame(columns=["row", "vector"])
values = df[0].values

#one hot encoding
for i, row in enumerate(values):
    vector    = [0] * len(values)
    vector[i] = 1
    tmp_se    = pd.Series([row, vector], index=new_df.columns)
    new_df    = new_df.append(tmp_se, ignore_index=True)

#表示
display(new_df)
