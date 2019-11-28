#AI-TECHGYM-2-6-Q
#特徴量エンジニアリング

#インポート
import pandas as pd

#読み込みデータ(2-6-A-1,2-6-A-2)
pg_data = {'0':['Python'],'1':['Ruby'],'2':['PHP'],'3':['Java'],'4':['JavaScript']}
df_row = pd.DataFrame(pg_data)
df = df_row.T
#display(df)

#読み込みデータ(2-6-A-3,2-6-A-4)
columns = ['Python','Ruby','PHP','Java','JavaScript']
D = [{"Label": "Python"},{"Label": "Ruby"},{"Label": "PHP"},{"Label": "Java"},{"Label": "JavaScript"}]
df_D = pd.DataFrame(D)
