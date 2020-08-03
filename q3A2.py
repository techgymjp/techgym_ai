#tech-gym-13-3-A
#センサーデータ分析

#必要なものをインポートする
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
%matplotlib inline

from sklearn.model_selection import train_test_split
import sklearn.svm

# 四国電力の電力消費量データを読み込み
elec_data = pd.read_csv(
    'shikoku_electricity_2012.csv',
    skiprows=3,
    names=['DATE', 'TIME', 'consumption'],
    parse_dates={'date_hour': ['DATE', 'TIME']},
    index_col = "date_hour")

#気象データを読み込み
tmp = pd.read_csv(
    u'takamatsu.csv',
    parse_dates={'date_hour': ["日時"]},
    index_col = "date_hour",
    na_values="×"
)

del tmp["時"]  # 「時」の列は使わないので、削除

# 列の名前を英語に変更
columns = {
    "降水量(mm)": "rain",
    "気温(℃)": "temperature",
    "日照時間(h)": "sunhour",
    "湿度(％)": "humid",
}
tmp.rename(columns=columns, inplace=True)

#欠損値を-1にする
tmp.fillna(-1,inplace=True)

# 月, 日, 時の取得
tmp["month"] = tmp.index.month
tmp['day'] = tmp.index.day
tmp['dayofyear'] = tmp.index.dayofyear
tmp['hour'] = tmp.index.hour

# 気象データと電力消費量データをいったん統合して時間軸を合わせたうえで、再度分割
takamatsu = elec_data.join(tmp[["temperature","sunhour","month","hour"]]).dropna().values

takamatsu_elec = takamatsu[:, 0:1]
takamatsu_wthr = takamatsu[:, 1:]

# 学習と性能の評価
model = sklearn.svm.SVR(gamma='scale')

x_train, x_test, y_train, y_test = train_test_split(
    takamatsu_wthr, takamatsu_elec, test_size=0.2)

y_train = y_train.flatten()
y_test = y_test.flatten()

model.fit(x_train, y_train)
date_name = ["気温", "日照時間","月","時間"]

output = "使用項目 = %s, 訓練スコア = %f, 検証スコア = %f" % \
         (", ".join(date_name),
          model.score(x_train, y_train),
          model.score(x_test, y_test)
          )

# 出力
print (output)
predicted = model.predict(x_test)
print(pd.DataFrame(predicted).describe())
print("平年並みの気温であれば、平均345万kW、最大438万kWを出せる電力の設備投資をすればよい")
