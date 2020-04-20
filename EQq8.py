#Techgym-6-6-Q

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
sample_u_vars =

#変換してYの標本データをつくる
sample_y =
print(sample_y)

#グラフ
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

#ヒストグラムと密度関数
xs = np.linspace(0, 40, 100)
rv =
ax.plot(xs, , color='gray')
hist, _, _ = ax.hist(sample_y, ,
                     range=(0, 40), )

plt.show()

#はじめに選んだ20個の標本の不偏分散
u_var = np.var(sample, ddof=1)

#信頼区間をもとめる
rv = stats.chi2(df=n-1)
lcl =
hcl =

print("分散の信頼区間",lcl, hcl)

#信頼区間の分布をみる
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
rv =
n_samples = 20
ax.vlines()

#20回試行して試行区間を描画する
for i in range(n_samples):
    sample_ = samples[i]
    u_var_ =
    lcl =
    ucl =
    if :
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
    u_var_ =
    lcl =
    ucl =
    if :
        cnt += 1
        
print("信頼区間に母分散が含まれている確率")

