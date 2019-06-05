#AI-TECHGYM-N-A
import numpy as np

#配列
data = np.array([9, 2, 3, 4, 10, 6, 7, 8, 1, 5])

#配列、次元数、要素数の表示
print(data)
print('次元数:', data.ndim)
print('要素数:', data.size)

#要素同士での演算(for文がなくていい)
print('掛け算:', data * data)
print('累乗:', data ** 3)
print('割り算:', data / 2)

#スライス、[n:m:s]「n番目からm-1番目を、sずつ飛ばして取り出す」
#nやmを省略したときは「すべて」という意味
#sが負のときは先頭からではなく、末尾から取り出すことを意味

#昇順
data.sort()
print('ソート後：', data)

#降順
data[::-1].sort()
print('ソート後：', data)

# 最小値
print('Min:', data.min())

# 最大値
print('Max:', data.max())

# 合計
print('Sum:', data.sum())

# 積み上げ
print('Cum:', data.cumsum())

# 積み上げ割合
print('Ratio:', data.cumsum() / data.sum())
