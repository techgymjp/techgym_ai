#AI-TECHGYM-4-5-Q
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

#datatimeに変換、年月のみの時間データにする
log_df["usedate"] =
log_df["年月"] =

#年月と顧客IDで集計、Columnの付け直し
log_df_months =
log_df_months.rename()

#不要なusedataは削除
del

#表示
display()

#顧客毎の利用回数：平均値、中央値、最大値、最小値
log_df_customer =
log_df_customer =
display(log_df_customer.head())

######
