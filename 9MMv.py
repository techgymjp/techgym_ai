#AI-TECHGYM-2-4-A-1
#特徴量エンジニアリング

#インポート
import pandas as pd
import scipy.stats as sp
from sklearn.preprocessing import StandardScaler

#行列
matrix = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

#標準化
sc = StandardScaler()
sc.fit(matrix)
matrix_std = sc.transform(matrix)
df_matrix_std = pd.DataFrame(matrix_std)
display(df_matrix_std)

#データフレーム
df = pd.DataFrame(matrix)

#標準化 : 各変数 - 平均 / 標準偏差
df_std = (df - df.mean())/df.std(ddof=False)
display(df_std)

#scipyでの計算
x = matrix

x_std = sp.stats.zscore(x, axis=0)
display(pd.DataFrame(x_std))

x_std = sp.stats.zscore(x, axis=1)
display(pd.DataFrame(x_std))

x_std = sp.stats.zscore(x, axis=None)
display(pd.DataFrame(x_std))

x_std = sp.stats.zscore(x, axis=0, ddof=True)
display(pd.DataFrame(x_std))

#検算
display(df_std.mean())
display(df_std.std(ddof=False))
