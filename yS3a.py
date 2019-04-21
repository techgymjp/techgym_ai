import pandas as pd
# graph
from matplotlib import pylab as plt
import seaborn as sns
# グラフを横長にする
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6
import matplotlib as mpl
mpl.rcParams['font.family'] = ['AppleGothic']

# データの読み込み
df = pd.read_csv("data.csv")

# 年齢のカラムを取得
age = df["Age"]

plt.hist(age, bins=10)
plt.show()
