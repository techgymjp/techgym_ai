#AI-TECHGYM-4-8-Q
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
customer_clustering =

#標準化
sc = StandardScaler()
customer_clustering_sc =

#k-means
kmeans =
clusters =
customer_clustering["cluster"] = clusters.labels_

#クラスタのデータ件数
display()

#結果確認
customer_clustering.columns = ["月内平均値","月内中央値", "月内最大値", "月内最小値","会員期間", "cluster"]
display()
display()

print()

#PCA
X = customer_clustering_sc
pca =
pca.fit(X)
x_pca =
pca_df = pd.DataFrame(x_pca)
pca_df["cluster"] = customer_clustering["cluster"]

#可視化
plt.figure(figsize=(8, 8))
for i in customer_clustering["cluster"].unique():
    clt = 
    plt.scatter(clt[0], clt[1])
