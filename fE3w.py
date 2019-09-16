# 1 必要ライブラリの読み込み
import numpy as np
import pandas as pd

import os

# tensorflowの読み込み
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# 2 trainデータのセットアップ
# 参照元では10_000_000だが、時間短縮のために、1_000_000に変更
train_df =  pd.read_csv('input/train.csv', nrows = 20_000)

# 乗った位置と降りた位置の差分をとり、別のカラムとして追加するメソッド
# 今回このカラムを学習用のパラメータとする
def add_travel_vector_features(df):
  df['abs_diff_longitude'] = (df.dropoff_longitude - df.pickup_longitude).abs()
  df['abs_diff_latitude'] = (df.dropoff_latitude - df.pickup_latitude).abs()

add_travel_vector_features(train_df)

# 3 データの確認
# 各データにnullがあるかどうかを確認

# nullデータを削除
train_df = train_df.dropna(how = 'any', axis = 'rows')

# 市内のみを基準とするため、lat,lngの差が5.0以上をカット
train_df = train_df[(train_df.abs_diff_longitude < 5.0) & (train_df.abs_diff_latitude < 5.0)]


# 4 学習
# 学習の方針はX・w = yでXをinput、yをターゲットとし、最適な重みのwを決定する

# inputの行列を作成するメソッド
def get_input_matrix(df):
  return np.column_stack((df.abs_diff_longitude, df.abs_diff_latitude, np.ones(len(df))))

train_X = get_input_matrix(train_df)
train_y = np.array(train_df['fare_amount'])

# tensorflowを利用

# 5 テストデータを使って予測
test_df = pd.read_csv('input/test.csv')

# テストデータに対してもtrainデータと同様の前処理を行う
add_travel_vector_features(test_df)
test_X = get_input_matrix(test_df)

# テストデータのX (inputデータ)とtrainデータから算出したw (重み)の積で予測する
test_y_predictions = model.predict(test_X) 

# CSVデータとして吐き出し
submission = pd.DataFrame(
  {'key': test_df.key, 'fare_amount': np.array(test_y_predictions).flatten()},
  columns = ['key', 'fare_amount'])
submission.to_csv('submission_4.csv', index = False)

