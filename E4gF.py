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

#plt.hist(age, bins=10)
#plt.show()

# 各種統計データの表示
print("mean : ", age.mean())
print("median : ", age.median())
print("mode : ", age.mode().tolist()[0])

# オリジナルのメソッド
def original_mean(series):
    n     = len(series)
    sum_s = sum(series)
    return sum_s/n 

def original_median(series):
    n = len(series)
    return sorted(series)[int(n/2)]

def original_mode(series):
    count_hash = {}
    for s in series:
        if str(s) not in count_hash:
            count_hash[str(s)] = 1
        else:
            count_hash[str(s)] = count_hash[str(s)] + 1
    
    return max(count_hash, key=count_hash.get)

print("original_mean : ",  original_mean(age))
print("original_median : ", original_median(age))
print("original_mode : ", original_mode(age))
