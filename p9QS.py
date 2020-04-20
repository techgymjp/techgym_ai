#Techgym-6-6-A

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

#サンプルサイズ20の標本データを1万組
np.random.seed(1111)
n_samples = 10000
samples = np.random.choice(scores, (n_samples, n))

#不偏分散
sample_u_vars = np.var(samples, axis=1, ddof=1)

#変換してYの標本データをつくる
sample_y = sample_u_vars * (n-1) / p_var
print(sample_y)

#グラフ
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

#ヒストグラムと密度関数
xs = np.linspace(0, 40, 100)
rv = stats.chi2(df=n-1)
ax.plot(xs, rv.pdf(xs), color='gray')
hist, _, _ = ax.hist(sample_y, bins=100,
                     range=(0, 40), density=True)

plt.show()

#はじめに選んだ20個の標本の不偏分散
u_var = np.var(sample, ddof=1)

#信頼区間をもとめる
rv = stats.chi2(df=n-1)
lcl = (n-1) * u_var / rv.isf(0.025)
hcl = (n-1) * u_var / rv.isf(0.975)

print("分散の信頼区間",lcl, hcl)

#信頼区間の分布をみる
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
rv = stats.chi2(df=n-1)
n_samples = 20
ax.vlines(p_var, 0, 21)

#20回試行して試行区間を描画する
for i in range(n_samples):
    sample_ = samples[i]
    u_var_ = np.var(sample_, ddof=1)
    lcl = (n-1) * u_var_ / rv.isf(0.025)
    ucl = (n-1) * u_var_ / rv.isf(0.975)
    if lcl <= p_var <= ucl:
        ax.scatter(u_var_, n_samples-i, color='gray')
        ax.hlines(n_samples-i, lcl, ucl, 'gray')
    else:
        ax.scatter(u_var_, n_samples-i, color='b')
        ax.hlines(n_samples-i, lcl, ucl, 'b')

#グラフタイトル
ax.set_xticks([p_var])
ax.set_xticklabels(['母分散'])
plt.show()

#1万回試行して、信頼区間に含まれているか
rv = stats.chi2(df=n-1)
cnt = 0
for sample_ in samples:
    u_var_ = np.var(sample_, ddof=1)
    lcl = (n-1) * u_var_ / rv.isf(0.025)
    ucl = (n-1) * u_var_ / rv.isf(0.975)
    if lcl <= p_var <= ucl:
        cnt += 1
        
print("信頼区間に母分散が含まれている確率",cnt / len(samples)*100,"%")

