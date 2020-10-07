#Tech-Gym-13-24-Q
#ディープラーニング画像分類器:CNN
#移転学習:VGG16

#必要なものをインポート
import os
import json
import numpy as np
import urllib.request
from keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from keras.preprocessing import image

#画像を表示するためにインポート
import matplotlib.pyplot as plt
%matplotlib inline

def download_json():
    url = "https://gist.githubusercontent.com/PonDad/4dcb4b242b9358e524b4ddecbee385e9/raw/dda9454f74aa4fafee991ca8b848c9ab6ae0e732/imagenet_class_index.json"
    title = "imagenet_class_index.json"
    if not os.path.exists(title):
        print("DOWNLOAD Japanese Name json file.")
        urllib.request.urlretrieve(url,"{0}".format(title))

def download_image():
    url = "http://up.gc-img.net/post_img_web/2013/08/DYe8z4FT1xTCFeE_17563_20.jpeg"
    title = "keras-vgg16-model_01.jpg"
    if not os.path.exists(title):
        print("DOWNLOAD image file.")
        urllib.request.urlretrieve(url,"{0}".format(title))

# モデルを構築する
model = VGG16()
model.summary()

#インプットの形を確認する
# model.input_shape (None, 224, 224, 3)


# 画像を読み込み、モデルの入力サイズでリサイズ


# PIL.Image オブジェクトを np.float32 型の numpy 配列に変換


# 配列の形状を (Height, Width, Channels) から (1, Height, Width, Channels) に変更


# 前処理


# preds.shape: (1, 1000)


#画像を予測する


#予測した名前を表示


#日本語ファイルをダウンロード

    
# ImageNet のラベル一覧を読み込む
)

# 推論する


# 推論結果を表示


