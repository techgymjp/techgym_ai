#Techgym-6-0-A

#インポート
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
%matplotlib inline
import japanize_matplotlib

from scipy import stats

#Jupyter Notebookの出力を小数点以下3桁に抑える
%precision 3
#Dataframeの出力を小数点以下3桁に抑える
pd.set_option('precision', 3)

#データフレーム
df = pd.read_csv('./scores400.csv')

#点数
scores = np.array(df['点数'])[:10]
scores_df = pd.DataFrame({'点数':scores},
                         index=pd.Index(['A','B','C','D','E','F','G','H','I','J'],
                         name='生徒'))

#平均
mean = np.mean(scores)

#偏差
deviation = scores - mean
print("英語：偏差",deviation)

#別のテストの偏差(数学)
another_scores = [52, 59, 58, 54, 51, 57, 56, 53, 52, 59]
another_mean = np.mean(another_scores)
another_deviation = another_scores - another_mean
print("数学：偏差",another_deviation)

#偏差の平均
dev_m = np.mean(deviation)
print("英語：偏差の平均{0:.3f}".format(dev_m))

#偏差の平均
dev_am = np.mean(another_deviation)
print("数学：偏差の平均{0:.3f}".format(dev_am))

#分散
print("分散",np.mean(deviation ** 2))
print("分散",np.var(scores))
print("分散",scores_df.var())

#まとめ
summary_df = scores_df.copy()
summary_df['偏差'] = deviation
summary_df['偏差二乗'] = np.square(deviation)
display(summary_df)

#標本偏差
sd = np.sqrt(np.var(scores, ddof=0))
print("標本偏差",sd)

sd_df = np.std(scores, ddof=0)
print("標本偏差",sd_df)

#度数分布
scores_all = np.array(df['点数'])
freq, _ = np.histogram(scores_all, bins=10, range=(0, 100))
print(freq)

# 0~10, 10~20, ... といった文字列のリストを作成
freq_class = [f'{i}~{i+10}' for i in range(0, 100, 10)]
# freq_classをインデックスにしてfreqでDataFrameを作成
freq_dist_df = pd.DataFrame({'度数':freq},
                            index=pd.Index(freq_class,
                                           name='階級'))
display(freq_dist_df)

#階級値
class_value = [(i+(i+10))//2 for i in range(0, 100, 10)]
print(class_value)

#相対度数
rel_freq = freq / freq.sum()
print(rel_freq)

#累積相対度数
cum_rel_freq = np.cumsum(rel_freq)
print(cum_rel_freq)

#まとめ
freq_dist_df['階級値'] = class_value
freq_dist_df['相対度数'] = rel_freq
freq_dist_df['累積相対度数'] = cum_rel_freq
freq_dist_df = freq_dist_df[['階級値', '度数',
                             '相対度数', '累積相対度数']]

display(freq_dist_df)
