#AI-TECHGYM-1-3-Q-1
#教師なし学習 k-mean法

#1-3
#□データセットを生成して、散布図を書こう(描画するドットは黒色にする)

# 可視化ライブラリ
import matplotlib.pyplot as plt
%matplotlib inline

# k-means法を使うためのインポート
from sklearn.cluster import KMeans

#分類データセット生成
from sklearn.datasets import make_blobs

plt.figure(figsize = (12,12))

X, y = make_blobs(random_state=1)
plt.subplot(3,3,1)
plt.scatter(X[:,0], X[:,1], color='black')
