#AI-TECHGYM-1-2-A-2
#教師なし学習 k-mean法

#1-2
#□データセットを生成して、散布図を書こう(描画するドットは黒色にする)
#□KMeansクラスを初期化しよう、初期化の方法はランダムで、クラスタ数は2とする
#□分類したクラスタ番号を表示してみる

# データ加工・処理・分析ライブラリ
import pandas as pd

# 可視化ライブラリ
import matplotlib.pyplot as plt
%matplotlib inline

# k-means法を使うためのインポート
from sklearn.cluster import KMeans

#分類データセット生成
from sklearn.datasets import make_blobs

X, y = make_blobs(random_state=5)
plt.scatter(X[:,0], X[:,1], color='black')

# クラスター分析
kmeans = KMeans(init='random', n_clusters=2)
kmeans.fit(X)
y_pred = kmeans.predict(X)

# 順にx座標、y座標、cluster番号のデータを横に結合するためconcatでaxis=1を指定
merge_data = pd.concat([pd.DataFrame(X[:,0]), pd.DataFrame(X[:,1]), pd.DataFrame(y_pred)], axis=1)
merge_data.columns = ['X','Y','cluster']

# クラスタリング結果のグラフ化

#display(cluster_df)
df0 = merge_data[merge_data.cluster == 0]
df1 = merge_data[merge_data.cluster == 1]

#グラフのプロット
plt.scatter(df0['X'],df0['Y'],color='blue',label='cluster0')
plt.scatter(df1['X'],df1['Y'],color='red',label='cluster1')

#凡例
plt.legend(loc='upper right')
