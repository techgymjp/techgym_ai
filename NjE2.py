#AI-TECHGYM-4-9-Q
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

#クラスタリングの変数
customer_clustering = customer[["mean", "median","max", "min", "membership_period"]]

#標準化
sc = StandardScaler()
customer_clustering_sc = sc.fit_transform(customer_clustering)

#k-means
kmeans = KMeans(n_clusters=4, random_state=0)
clusters = kmeans.fit(customer_clustering_sc)
customer_clustering["cluster"] = clusters.labels_

#####

#クラスタごとの継続ユーザーと退会ユーザー
customer_clustering =
c_is_del_df =
display(c_is_del_df)

#クラスタごとの定期利用フラグ
c_r_f_df =
display(c_r_f_df)

#年月ごと顧客ごとに集計する
log_df["usedate"] = pd.to_datetime(log_df["usedate"])
log_df["年月"] = log_df["usedate"].dt.strftime("%Y%m")
uselog_months = log_df.groupby(["年月","customer_id"],as_index=False).count()
uselog_months.rename(columns={"log_id":"count"}, inplace=True)
del uselog_months["usedate"]

#過去6ヶ月の利用データを集計する
year_months =
predict_data =
for :
    tmp =
    tmp.rename()
    for :
        tmp_before =
        del tmp_before["年月"]
        tmp_before.rename()
        tmp =
    predict_data =
display(predict_data.head())

#退会してしまったユーザーは欠損値になる
predict_data =
predict_data = predict_data.reset_index(drop=True)


#特徴量として会員期間を付与する
predict_data =
predict_data["now_date"] =
predict_data["start_date"] =
from dateutil.relativedelta import relativedelta
predict_data["period"] = None
for i in range(len(predict_data)):
    delta =
    predict_data["period"][i] =
display(predict_data.head())
