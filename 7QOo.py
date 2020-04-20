#Techgym-6-5-Q

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

#母平均、母分散
p_mean =
p_var =

#標本データ
np.random.seed(0)
n = 20
sample =
s_mean = np.mean(sample)

#サンプルサイズ20の標本データ
np.random.seed(1111)
n_samples = 10000
samples =

#95%信頼区間
rv = stats.norm()
lcl =
ucl =
print("信頼区間",lcl, ucl)

#グラフ設定
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)

#信頼区間を20回計算してみる
rv = stats.norm()
n_samples = 20
ax.vlines(p_mean, 0, 21)

for i in range(n_samples):
    sample_ = samples[i]
    s_mean_ = np.mean(sample_)
    lcl =
    ucl =
    if :
        ax.scatter()
        ax.hlines()
    else:
        ax.scatter()
        ax.hlines()

#母平均
ax.set_xticks([p_mean])
ax.set_xticklabels(['母平均'])
plt.show()


#1万回分、信頼区間を計算して母平均が含まれている確率を計算する
rv = stats.norm()
cnt = 0

for sample_ in samples:
    s_mean_ = np.mean(sample_)
    lcl =
    ucl =
    if :
        cnt += 1
print("信頼区間に何%含まれていたか")

