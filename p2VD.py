#Techgym-6-1-A

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

#桁の精度を指定
%precision 3

#表示
df = pd.read_csv('./scores400.csv')
display(df.head())

#先頭10個のarray
scores = np.array(df['点数'])
print("先頭10個",scores[:10])

#復元抽出：何度か実行してみる
num = 5
num_array = [1, 2, 3, 4, 5]
print("復元抽出",np.random.choice(num_array, num))

#非復元抽出：何度か実行してみる
print("非復元抽出",np.random.choice(num_array, num, replace=False))

#毎回結果が変わるのを防ぐ
np.random.seed(0)

#点数を20個抽出する
num = 20
sample = np.random.choice(scores, num)
print("標本平均",sample.mean())

#母平均
print("母平均",scores.mean())

#10回抽出してみる
n = 10
for i in range(n):
    sample = np.random.choice(scores, num)
    print(f'{i+1}回目の無作為抽出:標本平均', sample.mean())

