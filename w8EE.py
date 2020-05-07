##Techgym-6-3-Q

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
ax.hist()

#ラベル
ax.set_xlim(20, 100)
ax.set_ylim(0, 0.042)
ax.set_xlabel('点数')
ax.set_ylabel('相対度数')
plt.show()

#無作為抽出する
sample =

#ヒストグラム
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.hist()

#ラベル
ax.set_xlim(20, 100)
ax.set_ylim(0, 0.042)
ax.set_xlabel('点数')
ax.set_ylabel('相対度数')
plt.show()

#無作為抽出のサンプルサイズ20にして標本平均
#同じ作業を1000回実施する
num = 20
sample_means =

#ヒストグラム
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.hist()

# 母平均を縦線で表示


#ラベル
ax.set_xlim(50, 90)
ax.set_ylim(0, 0.07)
ax.set_xlabel('点数')
ax.set_ylabel('相対度数')
plt.show()
