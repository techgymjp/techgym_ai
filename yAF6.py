#Techgym-6-4-Q

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

%precision 3
%matplotlib inline

#データフレーム
df =

#点数
scores =

#母平均、母分散
p_mean =
p_var =

print("母平均",p_mean)
print("母分散",p_var)

#グラフ設定
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

#ヒストグラム
xs = np.arange(101)
rv =
ax.plot(xs, rv.pdf(xs), color='gray')
ax.hist()
plt.show()

#標本データ
np.random.seed(0)
n = 20
sample =
print("標本データ",sample)

#サンプルサイズ20の標本データ
np.random.seed(1111)
n_samples = 10000
samples =


###点推定###

#標本平均を5回試す
for i in range(5):
    s_mean =
    print(f'{i+1}回目の標本平均: {s_mean:.3f}')

#標本データそれぞれの標本平均を求めて
sample_means =
print("標本平均の期待値",np.mean(sample_means))

#サンプルサイズを100万にする
print("サンプルサイズ：100万")

#はじめに選んだ20個の標本
s_mean =
print("20個を選んだ標本平均",s_mean)

#標本分散を5回試す
for i in range(5):
    s_var =
    print(f'{i+1}回目の標本分散: {s_var:.3f}')
    
#標本データそれぞれの標本平均を求めて
sample_vars =
print("標本分散の期待値",np.mean(sample_vars))

#自由度を変更
sample_u_vars =
print("不偏分散",np.mean(sample_u_vars))

#サンプルサイズを100万にする
print("サンプルサイズ：100万"))

#はじめに選んだ20個の標本
u_var =
print("20個を選んだ分散",u_var)
