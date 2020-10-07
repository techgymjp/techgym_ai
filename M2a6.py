#Tech-Gym-13-12-A
#ディープラーニング画像分類器:CNN
#手書き文字データ

#必要なライブラリ
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
%matplotlib inline

#keras
from keras.models import Sequential
from keras.utils.np_utils import to_categorical
from keras.layers import Dense, Activation

#性能評価
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

#MNISTデータ
from keras.datasets import mnist

(X_train, y_train), (X_test, y_test) = mnist.load_data()

#行列の大きさを確認
print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)  

#はじめの6000個を1次元行列の形に変更
X_train = X_train.reshape(X_train.shape[0], 784)[:6000]
X_test = X_test.reshape(X_test.shape[0], 784)[:1000]
y_train = to_categorical(y_train)[:6000]
y_test = to_categorical(y_test)[:1000]

#行列の大きさを確認
print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)    

#モデルのインスタンスを作成
model = Sequential()

# 入力ユニット数は784、1つ目の全結合層の出力ユニット数は256
model.add(Dense(256, input_dim=784))
model.add(Activation("sigmoid"))

# 2つ目の全結合層の出力ユニット数は128
model.add(Dense(128))
model.add(Activation("relu"))

# 3つ目の全結合層（出力層）の出力ユニット数は10
model.add(Dense(10))
model.add(Activation("softmax"))

#モデルの生成
model.compile(optimizer="sgd", loss="categorical_crossentropy", metrics=["accuracy"])

#学習
history = model.fit(X_train, y_train, verbose=0, epochs=10)

#acc、val_accのプロット
plt.plot(history.history["acc"], label="acc", ls="-", marker="o")
plt.ylabel("accuracy")
plt.xlabel("epoch")
plt.legend(loc="best")
plt.show()

#モデル構造
model.summary()

#モデル評価
score = model.evaluate(X_test, y_test, verbose=1)
print("evaluate loss: {0[0]}\nevaluate acc: {0[1]}".format(score))

#混合行列
print('Cross tabulation')
y_pred = model.predict_classes(X_test)
y_test_c = np.argmax(y_test, axis=1)

#性能評価
print(confusion_matrix(y_pred, y_test_c))
print('正解率:{:.3f}'.format(accuracy_score(y_pred, y_test_c)))


