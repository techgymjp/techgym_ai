#Tech-Gym-13-19-Q
#ディープラーニング画像分類器:CNN
#手書き文字データ:モデル保存

import keras
from sklearn import datasets
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense, Dropout
from keras.utils.np_utils import to_categorical


# ラベルデータをone-hotベクトルに直す
x = iris.data
y = to_categorical(iris.target, nb_classes)

# モデルを定義


# コンパイル
model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy'])

# 学習を実行


# モデルを保存


# 学習済み重みデータを保存

# アヤメのサンプルデータを読み込む


# ラベルデータをone-hotベクトルに直す
x = iris.data
y = to_categorical(iris.target, nb_classes)

# モデルを読込


# 重みデータを読込


# モデルを評価
score = model.evaluate(x, y, verbose=1)
print("正解率=", score[1])



