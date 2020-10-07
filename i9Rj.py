#Tech-Gym-13-13-A
#ディープラーニング画像分類器:CNN
#手書き文字データ

###ハイパーパラメータ###
#活性化関数
#隠れ層の数、隠れ層のチャンネル数
#ドロップアウトする割合（rate）
#学習率（Ir）★
#最適化関数（optimizer）
#誤差関数（loss）
#バッチサイズ（batch_size）
#エポック数（epochs）

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
from keras import optimizers

#性能評価
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

#MNISTデータ
from keras.datasets import mnist

(X_train, y_train), (X_test, y_test) = mnist.load_data()

#行列の大きさを確認
#print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)  

#はじめの6000個を1次元行列の形に変更
X_train = X_train.reshape(X_train.shape[0], 784)[:6000]
X_test = X_test.reshape(X_test.shape[0], 784)[:1000]
y_train = to_categorical(y_train)[:6000]
y_test = to_categorical(y_test)[:1000]

#行列の大きさを確認
#print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)    

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

#学習率を変えて、正解率の変化を調べる
SGD_list = [0.001,0.01,0.1,1,10,100,1000,10000,100000]

#グラフ描画用の空リスト
acc = []

for LR in SGD_list:
    #学習率
    sgd = optimizers.SGD(lr=LR)
    
    #モデルの生成
    model.compile(optimizer="sgd", loss="categorical_crossentropy", metrics=["accuracy"])
    
    #学習
    history = model.fit(X_train, y_train, verbose=0, epochs=3)

    #モデル評価
    score = model.evaluate(X_test, y_test, verbose=0)
    acc.append(score[1])

#グラフを準備
fig = plt.figure()
plt.subplots_adjust(wspace=0.4, hspace=0.4)
ax = fig.add_subplot(1, 1, 1)
ax.grid(True)
ax.set_title("Parameter:LR")
ax.set_xlabel("LR")
ax.set_ylabel("acc")
ax.semilogx(SGD_list, acc, label="acc")
ax.legend()
ax.plot()
plt.show()


