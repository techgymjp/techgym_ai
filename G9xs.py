#AI-TECHGYM-1-2-Q
#教師なし学習 k-mean法

#1-2
#□データセットを生成して、散布図を書こう(描画するドットは黒色にする)
#□KMeansクラスを初期化しよう、初期化の方法はランダムで、クラスタ数は2とする
#□分類したクラスタ番号を表示してみる

# データ加工・処理・分析ライブラリ
import numpy as np
import numpy.random as random
import pandas as pd

# 可視化ライブラリ
import matplotlib.pyplot as plt
%matplotlib inline

# k-means法を使うためのインポート
from sklearn.cluster import KMeans

#分類データセット生成
from sklearn.datasets import make_blobs
