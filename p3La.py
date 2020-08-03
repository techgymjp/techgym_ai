#Tech-Gym-13-19-A
#ディープラーニング画像分類器:CNN
#手書き文字データ:モデル保存

import keras
from sklearn import datasets
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense, Dropout
from keras.utils.np_utils import to_categorical

# アヤメのサンプルデータを読み込む
iris = datasets.load_iris()
in_size = 4
nb_classes=3

# ラベルデータをone-hotベクトルに直す
x = iris.data
y = to_categorical(iris.target, nb_classes)

# モデルを定義
model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(in_size,)))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(nb_classes, activation='softmax'))

# コンパイル
model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy'])

# 学習を実行
model.fit(x, y, batch_size=20, epochs=50)

# モデルを保存
model.save('iris_model.h5')

# 学習済み重みデータを保存
model.save_weights('iris_weight.h5')

# アヤメのサンプルデータを読み込む
iris = datasets.load_iris()
in_size = 4
nb_classes=3

# ラベルデータをone-hotベクトルに直す
x = iris.data
y = to_categorical(iris.target, nb_classes)

# モデルを読込
model = load_model('iris_model.h5')

# 重みデータを読込
model.load_weights('iris_weight.h5')

# モデルを評価
score = model.evaluate(x, y, verbose=1)
print("正解率=", score[1])


