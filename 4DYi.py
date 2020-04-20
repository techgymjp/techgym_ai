#Techgym-6-7-Q

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
from scipy import stats

%precision 3
%matplotlib inline

#データフレーム
df = pd.read_csv('./scores400.csv')

#点数
scores = np.array(df['点数'])

#標本データ
np.random.seed(0)
n = 20
sample = np.random.choice(scores, n)
s_mean = np.mean(sample)

#はじめに選んだ20個の標本の不偏分散
u_var =

#母分散が未知の場合の区間推定
rv =
lcl =
ucl =

print("区間推定(母分散が未知の場合)",lcl, ucl)

#ベルヌーイ分布
enquete_df = pd.read_csv('./enquete.csv')
enquete = np.array(enquete_df['知っている'])
n = len(enquete)
print(enquete[:10])

#平均
s_mean = 
print("平均",s_mean)

#区間推定
rv = stats.norm()
lcl =
ucl =

print("区間推定(ベルヌーイ分布)",lcl, ucl)

#ポアソン分布
n_access_df = pd.read_csv('./access.csv')
n_access = np.array(n_access_df['アクセス数'])
n = len(n_access)
print(n_access[:10])

#平均
s_mean =
print("平均",s_mean)

#区間推定
rv = stats.norm()
lcl =
ucl =

print("区間推定(ポアソン分布)",lcl, ucl)


