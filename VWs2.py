#AI-TECHGYM-2-6-A-2
#特徴量エンジニアリング

#インポート
import pandas as pd

#読み込みデータ
pg_data = {'0':['Python'],'1':['Ruby'],'2':['PHP'],'3':['Java'],'4':['JavaScript']}
df_row = pd.DataFrame(pg_data)
df = df_row.T

#===OneHotEncoder====
from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder()
array_enc = enc.fit_transform(df).toarray()

columns = ['Java','JavaScript','PHP','Python','Ruby']
df1 = pd.DataFrame(data = array_enc, columns = columns,dtype=int)

#表示用の入れ替え
df1_d = df1.iloc[:,[3,4,2,0,1]]
display(df1_d)
