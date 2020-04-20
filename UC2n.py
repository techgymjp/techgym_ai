#AI-TECHGYM-4-3-A
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

######

#集計
print(customer_join.groupby("class_name").count()["customer_id"])
print(customer_join.groupby("campaign_name").count()["customer_id"])
print(customer_join.groupby("gender").count()["customer_id"])
print(customer_join.groupby("is_deleted").count()["customer_id"])

#入会人数の集計
customer_join["start_date"] = pd.to_datetime(customer_join["start_date"])
customer_start = customer_join.loc[customer_join["start_date"]>pd.to_datetime("20180401")]
print('入会人数',len(customer_start))

######
