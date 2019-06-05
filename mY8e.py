#AI-TECHGYM-N-E
import numpy as np

#表示のためのライブラリの読み込み
import matplotlib.pyplot as plt
%matplotlib inline

#ヘルプの表示
#help(plt.hist)

#乱数
import numpy.random as random

#設定値
init_seed = 0
hist_bin = 40

# シードの固定
random.seed(init_seed)

# グラフの大きさ
plt.figure(figsize = (20, 6))

#プロットデータ
data = np.random.randn(10 ** 5) * 10 + 50

# ヒストグラム
plt.hist(data, bins=hist_bin, range=(10, 90))

plt.grid(True)
