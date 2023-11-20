#Techgym-6-0-Q

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
pd.set_option('display.precision', 3)

#データフレーム
df =

#点数
scores =
scores_df =

#平均
mean =

#偏差
deviation =
print("英語：偏差",deviation)

#別のテストの偏差(数学)
another_scores = [52, 59, 58, 54, 51, 57, 56, 53, 52, 59]
another_mean =
another_deviation =
print("数学：偏差",another_deviation)

#偏差の平均
dev_m =
print()

#偏差の平均
dev_am =
print()

#分散
print("分散")
print("分散")
print("分散")

#まとめ
summary_df = scores_df.copy()
summary_df['偏差'] = deviation
summary_df['偏差二乗'] = np.square(deviation)
display(summary_df)

#標本偏差
sd =
print("標本偏差",sd)

sd_df =
print("標本偏差",sd_df)

#度数分布
scores_all = np.array(df['点数'])
freq, _ =
print(freq)

# 0~10, 10~20, ... といった文字列のリストを作成
freq_class = 
# freq_classをインデックスにしてfreqでDataFrameを作成
freq_dist_df = pd.DataFrame({'度数':freq},
                            index=pd.Index(freq_class,
                                           name='階級'))
display(freq_dist_df)

#階級値
class_value =
print(class_value)

#相対度数
rel_freq =
print(rel_freq)

#累積相対度数
cum_rel_freq =
print(cum_rel_freq)

#まとめ
freq_dist_df['階級値'] = class_value
freq_dist_df['相対度数'] = rel_freq
freq_dist_df['累積相対度数'] = cum_rel_freq
freq_dist_df = freq_dist_df[['階級値', '度数',
                             '相対度数', '累積相対度数']]

display(freq_dist_df)

