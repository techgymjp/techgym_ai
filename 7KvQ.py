#Techgym-6-3-A

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
%matplotlib inline

#データフレーム
df = pd.read_csv('./scores400.csv')

#点数
scores = np.array(df['点数'])

#ヒストグラム
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.hist(scores, bins=100, range=(0, 100), density=True)

#ラベル
ax.set_xlim(20, 100)
ax.set_ylim(0, 0.042)
ax.set_xlabel('点数')
ax.set_ylabel('相対度数')
plt.show()

#無作為抽出する
sample = np.random.choice(scores, 500)

#ヒストグラム
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.hist(sample, bins=100, range=(0, 100), density=True)

#ラベル
ax.set_xlim(20, 100)
ax.set_ylim(0, 0.042)
ax.set_xlabel('点数')
ax.set_ylabel('相対度数')
plt.show()

#無作為抽出のサンプルサイズ20にして標本平均
#同じ作業を1000回実施する
num = 5
sample_means = [np.random.choice(scores, num).mean()
                for _ in range(10000)]

#ヒストグラム
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.hist(sample_means, bins=100, range=(0, 100), density=True)

# 母平均を縦線で表示
ax.vlines(np.mean(scores), 0, 1, 'gray')

#ラベル
ax.set_xlim(50, 90)
ax.set_ylim(0, 0.07)
ax.set_xlabel('点数')
ax.set_ylabel('相対度数')
plt.show()

