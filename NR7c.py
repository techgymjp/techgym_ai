#AI-TECHGYM-4-9-A
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
customer_clustering = pd.concat([customer_clustering, customer], axis=1)
c_is_del_df = customer_clustering.groupby(["cluster","is_deleted"],as_index=False).count()[["cluster","is_deleted","customer_id"]]
display(c_is_del_df)

#クラスタごとの定期利用フラグ
c_r_f_df = customer_clustering.groupby(["cluster","routine_flg"],as_index=False).count()[["cluster","routine_flg","customer_id"]]
display(c_r_f_df)

#年月ごと顧客ごとに集計する
log_df["usedate"] = pd.to_datetime(log_df["usedate"])
log_df["年月"] = log_df["usedate"].dt.strftime("%Y%m")
uselog_months = log_df.groupby(["年月","customer_id"],as_index=False).count()
uselog_months.rename(columns={"log_id":"count"}, inplace=True)
del uselog_months["usedate"]

#過去6ヶ月の利用データを集計する
year_months = list(uselog_months["年月"].unique())
predict_data = pd.DataFrame()
for i in range(6, 11):
    tmp = uselog_months.loc[uselog_months["年月"]==year_months[i]]
    tmp.rename(columns={"count":"count_pred"}, inplace=True)
    for j in range(1, 7):
        tmp_before = uselog_months.loc[uselog_months["年月"]==year_months[i-j]]
        del tmp_before["年月"]
        tmp_before.rename(columns={"count":"count_{}".format(j-1)}, inplace=True)
        tmp = pd.merge(tmp, tmp_before, on="customer_id", how="left")
    predict_data = pd.concat([predict_data, tmp], ignore_index=True)
display(predict_data.head())

#退会してしまったユーザーは欠損値になる
predict_data = predict_data.dropna()
predict_data = predict_data.reset_index(drop=True)


#特徴量として会員期間を付与する
predict_data = pd.merge(predict_data, customer[["customer_id","start_date"]], on="customer_id", how="left")
predict_data["now_date"] = pd.to_datetime(predict_data["年月"], format="%Y%m")
predict_data["start_date"] = pd.to_datetime(predict_data["start_date"])
from dateutil.relativedelta import relativedelta
predict_data["period"] = None
for i in range(len(predict_data)):
    delta = relativedelta(predict_data["now_date"][i], predict_data["start_date"][i])
    predict_data["period"][i] = delta.years*12 + delta.months
display(predict_data.head())
