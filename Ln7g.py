#Tech-Gym-13-23-Q
#ディープラーニング画像分類器:CNN
#移転学習:

#必要なものをインポート
import os
import json
import numpy as np
import urllib.request
from keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
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
    title = "keras-model_01.jpg"
    if not os.path.exists(title):
        print("DOWNLOAD image file.")
        urllib.request.urlretrieve(url,"{0}".format(title))

# モデルを構築する
model = MobileNetV2()

#必要に応じて表示
#model.summary()

#インプットの形を確認する
# model.input_shape (None, 224, 224, 3)
print('model.input_shape', model.input_shape)  

# 画像を読み込み、モデルの入力サイズでリサイズ
download_image()
img_path = 'keras-model_01.jpg'
img = image.load_img(img_path, target_size=model.input_shape[1:3])

# PIL.Image オブジェクトを np.float32 型の numpy 配列に変換
x = image.img_to_array(img)
print('x.shape: {}, x.dtype: {}'.format(x.shape, x.dtype))
# x.shape: (224, 224, 3), x.dtype: float32

# 配列の形状を (Height, Width, Channels) から (1, Height, Width, Channels) に変更
x = np.expand_dims(x, axis=0)
print('x.shape: {}'.format(x.shape))  # x.shape: (1, 224, 224, 3)

# 前処理
x = preprocess_input(x)

# preds.shape: (1, 1000)
preds = model.predict(x)
print('preds.shape: {}'.format(preds.shape))

#画像を予測する
result = decode_predictions(preds, top=5)[0]

#予測した名前を表示
for _, name, score in result:
    print('{}: {:.2%}'.format(name, score))

#日本語ファイルをダウンロード
download_json()
    
# ImageNet のラベル一覧を読み込む
with open('./imagenet_class_index.json',encoding="utf-8") as f:
    data = json.load(f)
    class_names = np.array([row['ja'] for row in data])

# 推論する
scores = model.predict(x)[0]
top5_classes = scores.argsort()[-5:][::-1]

plt.axis('off')
plt.imshow(img)

# 推論結果を表示
for name, score in zip(class_names[top5_classes], scores[top5_classes]):
    print('{}: {:.2%}'.format(name, score))


