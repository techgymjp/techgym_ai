#Tech-Gym-13-21-Q
#ディープラーニング画像分類器:CNN
#画像分類

from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
import numpy as np

# カテゴリの指定
categories = ["chair","camera","butterfly","elephant","flamingo"]
nb_classes = len(categories)

# 画像サイズを指定
image_w = 64 
image_h = 64

# データをロード

# データを正規化する


# モデルを構築 


model.compile(loss='binary_crossentropy',
    optimizer='rmsprop',
    metrics=['accuracy'])

# モデルを訓練する


# モデルを評価する

