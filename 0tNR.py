#AI-TECHGYM-4-7-A
#実践ビジネスデータ分析

#インポート
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

#利用履歴
log_df = pd.read_csv('log.csv')

#会員データ
customer_df = pd.read_csv('customer.csv')

#会員区分データ
class_df = pd.read_csv('class.csv')

#キャンペーン区分
campaign_df = pd.read_csv('campaign.csv')

#顧客データ
customer_join = pd.merge(customer_df, class_df, on="class", how="left")
customer_join = pd.merge(customer_join, campaign_df, on="campaign_id", how="left")

#datatimeに変換、年月のみの時間データにする
log_df["usedate"] = pd.to_datetime(log_df["usedate"])
log_df["年月"] = log_df["usedate"].dt.strftime("%Y%m")

#年月と顧客IDで集計、Columnの付け直し
log_df_months = log_df.groupby(["年月","customer_id"],as_index=False).count()
log_df_months.rename(columns={"log_id":"count"}, inplace=True)

#不要なusedataは削除
del log_df_months["usedate"]

#顧客毎の利用回数：平均値、中央値、最大値、最小値
log_df_customer = log_df_months.groupby("customer_id").agg(["mean", "median", "max", "min" ])["count"]
log_df_customer = log_df_customer.reset_index(drop=False)

#利用日の曜日を数字に変換、Monday = 0、Sunday = 6の曜日
log_df["weekday"] = log_df["usedate"].dt.weekday

#ユーザー毎に月別と曜日別で集計を行う(lod_idを数える)
log_df_weekday = log_df.groupby(["customer_id","年月","weekday"], as_index=False).count()[["customer_id","年月", "weekday","log_id"]]
log_df_weekday.rename(columns={"log_id":"count"}, inplace=True)

#定期利用フラグをつくる
log_df_weekday = log_df_weekday.groupby("customer_id",as_index=False).max()[["customer_id", "count"]]
log_df_weekday["routine_flg"] = 0
log_df_weekday["routine_flg"] = log_df_weekday["routine_flg"].where(log_df_weekday["count"]<4, 1)

#作ったのもを結合する
customer_join = pd.merge(customer_join, log_df_customer, on="customer_id", how="left")
customer_join = pd.merge(customer_join, log_df_weekday[["customer_id", "routine_flg"]], on="customer_id", how="left")

#datetime形式に変換
customer_join["end_date"] = pd.to_datetime(customer_join["end_date"])
customer_join["start_date"] = pd.to_datetime(customer_join["start_date"])

# 警告(worning)の非表示化
import warnings
warnings.filterwarnings('ignore')

######

#まだ退会していない人は2019年4月30日とする
from dateutil.relativedelta import relativedelta
customer_join["calc_date"] = customer_join["end_date"]
customer_join["calc_date"] = customer_join["calc_date"].fillna(pd.to_datetime("20190430"))
customer_join["membership_period"] = 0

#差を計算した後で月単位にしている
for i in range(len(customer_join)):
    delta = relativedelta(customer_join["calc_date"].iloc[i], customer_join["start_date"].iloc[i])
    customer_join["membership_period"].iloc[i] = delta.years*12 + delta.months
display(customer_join.head())

#全体の数を把握する
display(customer_join[["mean", "median", "max", "min"]].describe())

#定期利用フラグ
print(customer_join.groupby("routine_flg").count()["customer_id"])

#会員期間
plt.hist(customer_join["membership_period"])
plt.show()

#退会ユーザー
customer_end = customer_join.loc[customer_join["is_deleted"]==1]
display(customer_end.describe())

#継続ユーザー
customer_stay = customer_join.loc[customer_join["is_deleted"]==0]
display(customer_stay.describe())

#書き出す
customer_join.to_csv("customer_join.csv", index=False)

######
