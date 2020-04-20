#Techgym-6-5-A

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
p_mean = np.mean(scores)
p_var = np.var(scores)

#標本データ
np.random.seed(0)
n = 20
sample = np.random.choice(scores, n)
s_mean = np.mean(sample)

#サンプルサイズ20の標本データ
np.random.seed(1111)
n_samples = 10000
samples = np.random.choice(scores, (n_samples, n))

#95%信頼区間
rv = stats.norm()
lcl = s_mean - rv.isf(0.025) * np.sqrt(p_var/n)
ucl = s_mean - rv.isf(0.975) * np.sqrt(p_var/n)
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
    lcl = s_mean_ - rv.isf(0.025) * np.sqrt(p_var/n)
    ucl = s_mean_ - rv.isf(0.975) * np.sqrt(p_var/n)
    if lcl <= p_mean <= ucl:
        ax.scatter(s_mean_, n_samples-i, color='gray')
        ax.hlines(n_samples-i, lcl, ucl, color='gray')
    else:
        ax.scatter(s_mean_, n_samples-i, color='b')
        ax.hlines(n_samples-i, lcl, ucl, color='b')

#母平均
ax.set_xticks([p_mean])
ax.set_xticklabels(['母平均'])
plt.show()


#1万回分、信頼区間を計算して母平均が含まれている確率を計算する
rv = stats.norm()
cnt = 0

for sample_ in samples:
    s_mean_ = np.mean(sample_)
    lcl = s_mean_ - rv.isf(0.025) * np.sqrt(p_var/n)
    ucl = s_mean_ - rv.isf(0.975) * np.sqrt(p_var/n)
    if lcl <= p_mean <= ucl:
        cnt += 1
print("信頼区間に何%含まれていたか",cnt / len(samples)*100,"%")

