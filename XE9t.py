#Techgym-6-2-A

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
%matplotlib inline

#桁の精度を指定
%precision 3

#イカサマしたサイコロの定義
dice = [1, 2, 3, 4, 5, 6]
prob = [1/21, 2/21, 3/21, 4/21, 5/21, 6/21]

#試行
print("試行したサイコロの目：",np.random.choice(dice, p=prob))

#100回の試行
num_trial = 100
sample = np.random.choice(dice, num_trial, p=prob)
print("100回試行したサイコロの目")
print(sample)

#度数分布表
freq, _ = np.histogram(sample, bins=6, range=(1, 7))
df_d = pd.DataFrame({'度数':freq,
                     '相対度数':freq / num_trial},
                      index = pd.Index(np.arange(1, 7), name='出目'))
display(df_d)

#グラフ化
fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111)
ax.hist(sample, bins=6, range=(1, 7), density=True, rwidth=0.8)

# 真の確率分布を横線で表示
ax.hlines(prob, np.arange(1, 7), np.arange(2, 8), colors='black')

# 棒グラフの[1.5, 2.5, ..., 6.5]の場所に目盛りをつける
ax.set_xticks(np.linspace(1.5, 6.5, 6))

# 目盛りの値は[1, 2, 3, 4, 5, 6]
ax.set_xticklabels(np.arange(1, 7))
ax.set_xlabel('出目')
ax.set_ylabel('相対度数')
plt.show()


#10000回の試行
num_trial = 10000
sample = np.random.choice(dice, num_trial, p=prob)

#グラフ化
fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111)
ax.hist(sample, bins=6, range=(1, 7), density=True, rwidth=0.8)

# 真の確率分布を横線で表示
ax.hlines(prob, np.arange(1, 7), np.arange(2, 8), colors='black')

# 棒グラフの[1.5, 2.5, ..., 6.5]の場所に目盛りをつける
ax.set_xticks(np.linspace(1.5, 6.5, 6))

# 目盛りの値は[1, 2, 3, 4, 5, 6]
ax.set_xticklabels(np.arange(1, 7))
ax.set_xlabel('出目')
ax.set_ylabel('相対度数')
plt.show()
