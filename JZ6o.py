#Techgym-6-4-A

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
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

print("母平均",p_mean)
print("母分散",p_var)

#グラフ設定
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

#ヒストグラム
xs = np.arange(101)
rv = stats.norm(p_mean, np.sqrt(p_var))
ax.plot(xs, rv.pdf(xs), color='gray')
ax.hist(scores, bins=100, range=(0, 100), density=True)
plt.show()

#標本データ
np.random.seed(0)
n = 20
sample = np.random.choice(scores, n)
print("標本データ",sample)

#サンプルサイズ20の標本データ
np.random.seed(1111)
n_samples = 10000
samples = np.random.choice(scores, (n_samples, n))


###点推定###

#標本平均を5回試す
for i in range(5):
    s_mean = np.mean(samples[i])
    print(f'{i+1}回目の標本平均: {s_mean:.3f}')

#標本データそれぞれの標本平均を求めて
sample_means = np.mean(samples, axis=1)
print("標本平均の期待値",np.mean(sample_means))

#サンプルサイズを100万にする
print("サンプルサイズ：100万",np.mean(np.random.choice(scores, int(1e6))))

#はじめに選んだ20個の標本
s_mean = np.mean(sample)
print("20個を選んだ標本平均",s_mean)

#標本分散を5回試す
for i in range(5):
    s_var = np.var(samples[i])
    print(f'{i+1}回目の標本分散: {s_var:.3f}')
    
#標本データそれぞれの標本平均を求めて
sample_vars = np.var(samples, axis=1)
print("標本分散の期待値",np.mean(sample_vars))

#自由度を変更
sample_u_vars = np.var(samples, axis=1, ddof=1)
print("不偏分散",np.mean(sample_u_vars))

#サンプルサイズを100万にする
print("サンプルサイズ：100万",np.var(np.random.choice(scores, int(1e6)), ddof=1))

#はじめに選んだ20個の標本
u_var = np.var(sample, ddof=1)
print("20個を選んだ分散",u_var)

