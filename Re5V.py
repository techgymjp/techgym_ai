#tech-gym-13-2-A
#センサーデータ分析

#必要なものをインポートする
import pandas as pd

import matplotlib.pyplot as plt
%matplotlib inline

# 四国電力の電力消費量データを読み込み
elec_data = pd.read_csv(
    'shikoku_electricity_2012.csv',
    skiprows=3,
    names=['DATE', 'TIME', 'consumption'],
    parse_dates={'date_hour': ['DATE', 'TIME']},
    index_col = "date_hour")

# 画像のサイズを設定する
plt.figure(figsize=(12, 12))

# 時系列グラフ生成
delta = elec_data.index - pd.to_datetime('2012/07/01 00:00:00')
elec_data['time'] = delta.days + delta.seconds / 3600.0 / 24.0

#電力消費量の時間変化
plt.subplot(2, 1, 1)
plt.scatter(elec_data['time'], elec_data['consumption'], s=1)
plt.xlabel('days from 2012/7/1')
plt.ylabel('electricity consumption(*10000 kWh)')

# ヒストグラム生成
plt.subplot(2, 1, 2)
plt.hist(elec_data['consumption'], bins=100, color="gray")
plt.xlabel('electricity consumption(*10000 kW)')
plt.ylabel(u'count')

# グラフ
plt.show()