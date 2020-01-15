#AI-TECHGYM-3-9-Q-1
#回帰問題と分類問題

#インポート
import re
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import pandas as pd

#最大表示
pd.set_option('display.max_rows', 500)

#データフレーム
data_from_csv = pd.read_csv("13_Tokyo_20171_20184.csv", encoding='cp932')

#データサイズ、一行目を表示



#どんな不動産かを確認
print(data_from_csv["種類"].unique())

#中古マンションのみ
data_used_apartment =

#必要であれば表示
#print(data_used_apartment.shape)
#print(data_used_apartment.head())

#欠損値の確認
#print(data_used_apartment.isnull().sum())

#説明変数を選択
columns_name_list =
data_selected = data_used_apartment[columns_name_list]

#必要であれば表示
#print(data_selected.shape)

#一つでもNANデータを含む行を削除
data_selected_dropna =

#必要であれば表示
#print(data_selected_dropna.shape)
#print(data_selected_dropna.iloc[0])

#######築年数の変換#######

#築年数を確認
data_selected_dropna["建築年"].unique()

data_selected_dropna = data_selected_dropna[data_selected_dropna["建築年"].str.match('^平成|昭和')]

#和暦ー西暦
wareki_to_seireki = {'昭和': 1926-1, '平成': 1989-1}

#築年数のリスト
building_year_list = data_selected_dropna["建築年"]

building_age_list = []
for building_year in building_year_list:
    #昭和○年 → 昭和, ○ に変換、平成○年 → 平成, ○ に変換
    building_year_split = re.search(r'(.+?)([0-9]+|元)年', building_year)
    #西暦に変換
    seireki = wareki_to_seireki[building_year_split.groups()[0]] + int(building_year_split.groups()[1])
   
    building_age = 2018 - seireki # 築年数に変換
    building_age_list.append(building_age)

#築年数列を追加
data_selected_dropna["築年数"] = building_age_list

# もう使わないので、建築年列は削除
data_added_building_age = data_selected_dropna.drop("建築年", axis=1)

#########################

# ダミー変数化しないもののリスト
columns_name_list = ["最寄駅：距離（分）", "面積（㎡）","築年数", "建ぺい率（％）", "容積率（％）", "取引価格（総額）"]

# ダミー変数化するリスト
dummy_list =

# ダミー変数を追加
data_added_dummies =


#必要であれば表示:データの確認
#print(data_added_dummies.shape)
#print(data_added_dummies.iloc[0])
#print(data_added_dummies.dtypes)

#文字列を変換、不要なデータを取り除く
data_added_dummies["面積（㎡）"] =
data_added_dummies = data_added_dummies[~data_added_dummies['最寄駅：距離（分）'].str.contains('\?')]
data_added_dummies["最寄駅：距離（分）"] =

#必要ならデータタイプの確認
#print(data_added_dummies.dtypes)

#CSVに書き出し

