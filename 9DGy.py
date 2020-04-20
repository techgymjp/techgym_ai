#AI-TECHGYM-4-1-A
#実践ビジネスデータ分析

#インポート
import pandas as pd

#利用履歴
log_df = pd.read_csv('log.csv')
display(log_df.head())

#会員データ
customer_df = pd.read_csv('customer.csv')
display(customer_df.head())

#会員区分データ
class_df = pd.read_csv('class.csv')
display(class_df.head())

#キャンペーン区分
campaign_df = pd.read_csv('campaign.csv')
display(campaign_df.head())
