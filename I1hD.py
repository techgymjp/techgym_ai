#AI-TECHGYM-4-8-A
#実践ビジネスデータ分析

#インポート
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

from sklearn.decomposition import PCA

# 警告(worning)の非表示化
import warnings
warnings.filterwarnings('ignore')

#利用履歴
log_df = pd.read_csv('log.csv')

#作成した顧客データ
customer = pd.read_csv('customer_join.csv')

#####

#クラスタリングの変数
customer_clustering = customer[["mean", "median","max", "min", "membership_period"]]

#標準化
sc = StandardScaler()
customer_clustering_sc = sc.fit_transform(customer_clustering)

#k-means
kmeans = KMeans(n_clusters=4, random_state=0)
clusters = kmeans.fit(customer_clustering_sc)
customer_clustering["cluster"] = clusters.labels_

#クラスタのデータ件数
display(customer_clustering.head())

#結果確認
customer_clustering.columns = ["月内平均値","月内中央値", "月内最大値", "月内最小値","会員期間", "cluster"]
display(customer_clustering.groupby("cluster").count().head(1))
display(customer_clustering.groupby("cluster").mean())

print("グループ0は会員期間は短いが利用回数が多い顧客である")
print("グループ2は会員期間は短く利用回数も少ないい顧客である")

#PCA
X = customer_clustering_sc
pca = PCA(n_components=2)
pca.fit(X)
x_pca = pca.transform(X)
pca_df = pd.DataFrame(x_pca)
pca_df["cluster"] = customer_clustering["cluster"]

#可視化
plt.figure(figsize=(8, 8))
for i in customer_clustering["cluster"].unique():
    clt = pca_df.loc[pca_df["cluster"]==i]
    plt.scatter(clt[0], clt[1])
