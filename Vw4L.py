#AI-TECHGYM-2-6-A-4
#特徴量エンジニアリング

#インポート
import pandas as pd
from sklearn.feature_extraction import FeatureHasher

n_features = 5
h = FeatureHasher(n_features=n_features)

#読み込みデータ
columns = ['Python','Ruby','PHP','Java','JavaScript']
D = [{"Label": "Python"},{"Label": "Ruby"},{"Label": "PHP"},{"Label": "Java"},{"Label": "JavaScript"}]
df_D = pd.DataFrame(D)
#display(df_D)

f_array = h.transform(D).toarray()
df_a = pd.DataFrame(f_array,dtype=int,index=columns)
display(df_a)
