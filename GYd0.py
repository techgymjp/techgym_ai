#techgym-10-5-A

import os
import cv2
import json
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
%matplotlib inline

#エラー回避のための記述
import tensorflow as tf
tf.to_float = lambda x: tf.cast(x, tf.float32)

#ディレクトリ設定
image_dir = os.path.join("competition_data", "val_images")

# フォルダ内のファイル名のリストを取得
image_files = sorted(os.listdir(image_dir))

#画像データの読み込みと可視化
annotations_dir = os.path.join('competition_data', 'val_annotations')
annotations_files = sorted(os.listdir(annotations_dir))

annotation = []
for file in annotations_files:
    with open(os.path.join(annotations_dir,file)) as f:
        data = json.load(f)
        annotation.append(data)

##################################################################

#インポート
from ssd import SSD

#インスタンス化
ssd = SSD("ssd_7")

#名前とサイズ
print(ssd.model_name)
print(ssd.image_size)

#モデル表示
print(ssd.model.summary())

#学習済みモデルの読み込み
models_dir = os.path.join(".", "trained_models")
print(os.listdir(models_dir))

model_path = os.path.join(models_dir, "ssd7.h5")
ssd.load_weights(model_path)

