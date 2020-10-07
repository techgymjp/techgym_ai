#Tech-Gym-13-17-Q
#ディープラーニング画像分類器:CNN
#手書き文字データ

#必要なライブラリ
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

#MNISTデータ
from keras.datasets import mnist

#keras
from keras.layers import Dense, Dropout, Flatten, Activation
from keras.layers import Conv2D, MaxPooling2D
from keras.models import Sequential, load_model
from keras.utils.np_utils import to_categorical
from keras.utils.vis_utils import plot_model

#性能評価
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

# データをロードします
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# ここでは全データのうち、学習には6000、テストには1000個のデータを使用する
X_train = X_train[:6000].reshape(-1, 28, 28, 1)
X_test = X_test[:1000].reshape(-1, 28, 28, 1)
y_train = to_categorical(y_train)[:6000]
y_test = to_categorical(y_test)[:1000]

# モデルを定義します
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),input_shape=(28,28,1)))
model.add(Activation('relu'))
model.add(Conv2D(filters=64, kernel_size=(3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(10))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adadelta',
              metrics=['accuracy'])

model.fit(X_train, y_train,
          batch_size=128,
          epochs=10,
          verbose=1,
          validation_data=(X_test, y_test))

#モデル評価
score = model.evaluate(X_test, y_test, verbose=1)
print("evaluate loss: {0[0]}\nevaluate acc: {0[1]}".format(score))

###必要なら以下を表示する####
#混合行列
#print('Cross tabulation')
#y_pred = model.predict_classes(X_test)
#y_test_c = np.argmax(y_test, axis=1)

#性能評価
#print(confusion_matrix(y_pred, y_test_c))
#print('正解率:{:.3f}'.format(accuracy_score(y_pred, y_test_c)))

