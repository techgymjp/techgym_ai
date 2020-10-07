#tech-gym-13-1-A
#センサーデータ分析

#必要なものをインポートする
import pandas as pd

import matplotlib.pyplot as plt
%matplotlib inline

#気象データを読み込み
tmp = pd.read_csv(
    u'takamatsu.csv',
    parse_dates={'date_hour': ["日時"]},
    index_col = "date_hour",
    na_values="×"
)

# 「時」の列は使わないので削除する
del tmp["時"]

# 列の名前を英語に変える
columns = {
    "降水量(mm)": "rain",
    "気温(℃)": "temperature",
    "湿度(％)": "humid",
}
tmp.rename(columns=columns, inplace=True)

#欠損値を0にする
tmp = tmp.fillna(0)

# ヒストグラム生成
delta = tmp.index - pd.to_datetime('2012/07/01 00:00:00')
tmp['time'] = delta.days + delta.seconds / 3600.0 / 24.0

#必要に応じて表示
#display(tmp)

# 画像サイズを設定する
plt.figure(figsize=(20, 20))

# 表示
plt.subplot(3, 1, 1)
plt.scatter(tmp['time'], tmp['temperature'], s=0.1)
plt.xlabel('days from 2012/7/1')
plt.ylabel('Temperature(C degree)')

plt.subplot(3, 1, 2)
plt.scatter(tmp['time'], tmp['humid'], s=0.1)
plt.xlabel('days from 2012/7/1')
plt.ylabel('humid(%)')

plt.subplot(3, 1, 3)
plt.scatter(tmp['time'], tmp['rain'], s=0.1)
plt.xlabel('days from 2012/7/1')
plt.ylabel('rain(mm)')


# グラフ表示
plt.show()
