#techgym-10-8-Q

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

#SSDインポート
from ssd import SSD

ssd = SSD("ssd_7")

models_dir = os.path.join(".", "trained_models")
#print(os.listdir(models_dir))

model_path = os.path.join(models_dir, "ssd7.h5")
ssd.load_weights(model_path)

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


def horizontal_flip_image(img):
    return img[:,::-1,:]

def horizontal_flip_bbox(bbox, image_size):
    height, width, channel = image_size
    x1, y1, x2, y2 = bbox
    
    x1_new = width - x2
    y1_new = y1
    x2_new = width - x1
    y2_new = y2
    return x1_new, y1_new, x2_new, y2_new

##################################################################

# 画像を1枚選択
index =
image_path =
img =
gt =

# windowをスライドさせて予測
window_size =
stride =
output_sw =

confidence_threshold =
output_sw_thresh =
output_sw_thresh = sorted(output_sw_thresh, key=lambda x:x["score"], reverse=True)
print(output_sw_thresh)
print()
print("bbox size:", len(output_sw_thresh))

plot_bbox(img, gt, output_sw_thresh)

confidence_threshold =
output_sw_thresh =
output_sw_thresh = sorted(output_sw_thresh, key=lambda x:x["score"], reverse=True)
print(output_sw_thresh)
print()
print("bbox size:", len(output_sw_thresh))

plot_bbox(img, gt, output_sw_thresh)
