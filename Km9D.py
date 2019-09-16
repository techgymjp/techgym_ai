# 1 必要ライブラリの読み込み
import numpy as np
import pandas as pd

import os

# 2 trainデータのセットアップ
# 参照元では10_000_000だが、時間短縮のために、1_000_000に変更
train_df =  pd.read_csv('input/train.csv', nrows = 1_000_000)
# パラメータ名とその型を確認
print(train_df.dtypes)

# 乗った位置と降りた位置の差分をとり、別のカラムとして追加するメソッド
# 今回このカラムを学習用のパラメータとする
def add_travel_vector_features(df):
  df['abs_diff_longitude'] = (df.dropoff_longitude - df.pickup_longitude).abs()
  df['abs_diff_latitude'] = (df.dropoff_latitude - df.pickup_latitude).abs()

add_travel_vector_features(train_df)

# 3 データの確認
# 各データにnullがあるかどうかを確認
print(train_df.isnull().sum())

# nullデータを削除
print('Old size: %d' % len(train_df))
train_df = train_df.dropna(how = 'any', axis = 'rows')
print('New size: %d' % len(train_df))

# 市内のみを基準とするため、lat,lngの差が5.0以上をカット
print('Old size: %d' % len(train_df))
train_df = train_df[(train_df.abs_diff_longitude < 5.0) & (train_df.abs_diff_latitude < 5.0)]
print('New size: %d' % len(train_df))


# 4 学習
# 学習の方針はX・w = yでXをinput、yをターゲットとし、最適な重みのwを決定する

# inputの行列を作成するメソッド
def get_input_matrix(df):
  return np.column_stack((df.abs_diff_longitude, df.abs_diff_latitude, np.ones(len(df))))

train_X = get_input_matrix(train_df)
train_y = np.array(train_df['fare_amount'])

print(train_X.shape)
print(train_y.shape)

# 単純な最小二乗法で重みwを算出
(w, _, _, _) = np.linalg.lstsq(train_X, train_y, rcond = None)
print("重み")
print(w)

# 5 テストデータを使って予測
test_df = pd.read_csv('input/test.csv')

# テストデータに対してもtrainデータと同様の前処理を行う
add_travel_vector_features(test_df)
test_X = get_input_matrix(test_df)

# テストデータのX (inputデータ)とtrainデータから算出したw (重み)の積で予測する
test_y_predictions = np.matmul(test_X, w).round(decimals = 2)

# CSVデータとして吐き出し
submission = pd.DataFrame(
  {'key': test_df.key, 'fare_amount': test_y_predictions},
  columns = ['key', 'fare_amount'])
submission.to_csv('submission.csv', index = False)

