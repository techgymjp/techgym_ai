import pandas as pd
# graph
from matplotlib import pylab as plt
import seaborn as sns
# グラフを横長にする
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6
import matplotlib as mpl
mpl.rcParams['font.family'] = ['AppleGothic']

from sklearn.preprocessing import StandardScaler

# データの読み込み
df = pd.read_csv("data.csv")

scaler = StandardScaler()
df[["Age"]] = scaler.fit_transform(df[["Age"]])

print(df["Age"])
