#techgym-10-6-A

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

#SSDモデル設定
from ssd import SSD

ssd = SSD("ssd_7")

models_dir = os.path.join(".", "trained_models")
print(os.listdir(models_dir))

model_path = os.path.join(models_dir, "ssd7.h5")
ssd.load_weights(model_path)


##################################################################

# 画像を1枚選択
index = 4
image_path = os.path.join(image_dir, image_files[index])
img = cv2.imread(image_path)
gt = annotation[index]

# 選択した画像に対してbboxの予測を行う
output = ssd.predict(image_path)
#print(output)

# 確信度の閾値
confidence_threshold = 0.25

# スコアが閾値以上のものだけに絞る
output_thresh = [prediction for prediction in output if prediction["score"]>= confidence_threshold]

# スコア順にソート
output_thresh = sorted(output_thresh, key=lambda x:x["score"], reverse=True)
print(output_thresh)

def plot_bbox(img, gt, out):
    # グラフサイズの指定
    plt.figure(figsize=(11,11))

    # 衛星データを表示（BGR->RGB）
    plt.imshow(img[:,:,::-1])

    # 今操作したいaxis（画像）を選択
    current_axis = plt.gca()

    # 正解となるbboxを可視化（赤色で表示）
    for label in gt["labels"]:
        # バウンディングボックスの座標から始点と幅、高さを算出し、四角形を生成
        xmin = label["box2d"]["x1"]
        ymin = label["box2d"]["y1"]
        width = label["box2d"]["x2"] - xmin
        height = label["box2d"]["y2"] - ymin
        rect = plt.Rectangle((xmin, ymin), width, height, color="r", fill=False, linewidth=2)
    
        # 表示名はカテゴリ名とする為、カテゴリ名を取得
        category = label["category"]
    
        # 四角形とカテゴリ名を画像中に表示
        current_axis.add_patch(rect)
        current_axis.text(xmin, ymin-20, category, size="x-large", color="white", bbox={"facecolor":"r"})

    # 予測結果のbboxを可視化（青色で表示）
    for o in out:
        x1, y1, x2, y2 = o["bbox"]
        rect = plt.Rectangle((x1, y1), x2-x1, y2-y1, color="b", fill=False, linewidth=2)
    
        category = "ship"
        score = o["score"]
        label = "{}: {:.2f}".format(category, score)
    
        current_axis.add_patch(rect)
        current_axis.text(x1, y1, label, size="x-large", color="white", bbox={"facecolor":"b"})

#表示
plot_bbox(img, gt, output_thresh)

