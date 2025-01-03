#AI-TECHGYM-4-6-Q
#実践ビジネスデータ分析

#インポート
import pandas as pd

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

######

#利用日の曜日を数字に変換、Monday = 0、Sunday = 6の曜日
log_df["weekday"] =

#ユーザー毎に月別と曜日別で集計を行う(lod_idを数える)
log_df_weekday =
log_df_weekday.rename()
display(log_df_weekday.head())

#定期利用フラグをつくる
log_df_weekday =
log_df_weekday["routine_flg"] = 0
log_df_weekday["routine_flg"] =
display(log_df_weekday.head())

#作ったのもを結合する
customer_join = pd.merge()
customer_join = pd.merge()
display(customer_join.head())


######
