import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import re
import csv
import numpy as np

# graph
from matplotlib import pylab as plt

# グラフを横長にする
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

import matplotlib as mpl
mpl.rcParams['font.family'] = ['AppleGothic']

# データ加工
df = pd.read_csv("words2vector.csv")
