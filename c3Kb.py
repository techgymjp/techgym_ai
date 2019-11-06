#AI-TECHGYM-1-3-A-2
#教師なし学習 k-mean法

# 可視化ライブラリ
import matplotlib.pyplot as plt
%matplotlib inline

# k-means法を使うためのインポート
from sklearn.cluster import KMeans

#分類データセット生成
from sklearn.datasets import make_blobs

#推定するクラスタ
X_L, y_L = make_blobs(random_state=5)

# エルボー方による推定。クラスター数を1から20に増やして、それぞれの距離の総和を求める
dist_list =[]
for i in range(1,10):
    kmeans= KMeans(n_clusters=i, init='random', random_state=0)
    kmeans.fit(X_L)
    dist_list.append(kmeans.inertia_)
    
# グラフを表示
plt.figure(figsize = (12,12))
plt.subplot(2,2,1)
plt.plot(range(1,10), dist_list,marker='+')
plt.xlabel('Number of clusters')
plt.ylabel('Distortion')

#推定するクラスタ
X_L, y_L = make_blobs(random_state=10)

# エルボー方による推定。クラスター数を1から20に増やして、それぞれの距離の総和を求める
dist_list =[]
for i in range(1,10):
    kmeans= KMeans(n_clusters=i, init='random', random_state=0)
    kmeans.fit(X_L)
    dist_list.append(kmeans.inertia_)
    
# グラフを表示
plt.subplot(2,2,2)
plt.plot(range(1,10), dist_list,marker='+')
plt.xlabel('Number of clusters')
plt.ylabel('Distortion')
