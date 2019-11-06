#AI-TECHGYM-1-4-Q-1
#教師なし学習 k-mean法

# データ加工・処理・分析ライブラリ
import pandas as pd

# データがあるurl の指定
file_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00468/online_shoppers_intention.csv'

# データを取得して展開する
#対象データを読み込み
shoppers= pd.read_csv(file_url)