#Techgym8-8-A-1

# ライブラリのインポート
from keras.models import Sequential
from keras.layers import Dense, Flatten, Activation
from keras.layers import Conv2D, MaxPooling2D
from keras import optimizers
from keras.utils import to_categorical

#CIFAR-10のデータセットのインポート
from keras.datasets import cifar10
(X_train, y_train), (X_test, y_test) = cifar10.load_data()

# 特徴量の正規化
X_train = X_train/255.
X_test = X_test/255.
 
# クラスラベルの1-hotベクトル化
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# モデルの定義
model = Sequential()
model.add(Conv2D(filters=6, kernel_size=(3,3), input_shape=(32,32,3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(filters=12, kernel_size=(3,3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

# A. 畳み込み層(フィルタサイズ=36, カーネルサイズ=(3,3))
model.add(Conv2D(filters=36, kernel_size=(3,3)))
# B. 活性化関数(ReLU)
model.add(Activation("relu"))
# C. プーリング層(プーリングサイズ=(2,2))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(units=120))
model.add(Activation("relu"))
model.add(Dense(units=60))
model.add(Activation("relu"))
model.add(Dense(units=10))
model.add(Activation("softmax"))

# モデルの確認
#model.summary()

#学習
model.compile(loss="categorical_crossentropy",
             optimizer=optimizers.SGD(lr=0.5),
             metrics=["accuracy"])

history_log = model.fit(X_train, y_train, batch_size=10, epochs=5, validation_data=(X_test, y_test))


#グラフ化
from matplotlib import pyplot as plt

def learning_plot(history, epochs):
    fig = plt.figure(figsize=(15,5))
    # Lossの可視化
    plt.subplot(1,2,1)
    plt.plot(range(1,epochs+1), history.history['loss'])
    plt.plot(range(1,epochs+1), history.history['val_loss'])
    plt.title('model loss')
    plt.xlabel('epoch')
    plt.xticks(range(1,epochs+1))
    plt.ylabel('loss')
    plt.legend(['train', 'test'], loc='upper right')
    
    # 正解率(accuracy)の可視化
    plt.subplot(1,2,2)
    plt.plot(range(1,epochs+1), history.history['accuracy'])
    plt.plot(range(1,epochs+1), history.history['val_accuracy'])
    plt.title('model accuracy')
    plt.xlabel('epoch')
    plt.xticks(range(1,epochs+1))
    plt.ylabel('accuracy')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()

#グラフ描画
learning_plot(history_log,epochs=5)
