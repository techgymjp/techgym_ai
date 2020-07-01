#techgym-10-10-A

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

from tqdm import tqdm
from evaluation import f1_scores

ans = []
for a1 in annotation:
    tmp = []
    for a2 in a1["labels"]:
        tmp.append((a2["box2d"]["x1"], a2["box2d"]["y1"], a2["box2d"]["x2"], a2["box2d"]["y2"]))
    ans.append(tmp)
ans

##################

#1つ目「特に工夫をせずに予測」した時の精度を評価
preds = []
for image_file in tqdm(image_files):
    # i番目の入力画像と正解のbbox
    image_path = os.path.join(image_dir, image_file)

    # 予測
    confidence_threshold = 0.25
    out = ssd.predict(image_path)
    out = [pred for pred in out if pred["score"]>=confidence_threshold]
    out = sorted(out, key=lambda x:x["score"], reverse=True)
    pred = [p['bbox'] for p in out]
    preds.append(pred)

# 評価
score, cm = f1_scores(preds, ans)
print("f1_score:", score)
print("confusion matrix:", cm)
print("TP（検出）が伸びておらず、FN（未検出）が圧倒的に多くなっている")

##################

#2つ目「予測時に画像を水増しして予測」した時の精度を評価
preds = []
for image_file in tqdm(image_files):
    # i番目の入力画像と正解のbbox
    image_path = os.path.join(image_dir, image_file)

    # 予測
    confidence_threshold = 0.25
    out =  ssd.predict(image_path, [horizontal_flip_image, horizontal_flip_bbox])
    out = [pred for pred in out if pred["score"]>=confidence_threshold]
    out = sorted(out, key=lambda x:x["score"], reverse=True)
    pred = [p['bbox'] for p in out]
    preds.append(pred)

# 評価
score, cm = f1_scores(preds, ans)
print("f1_score:", score)
print("confusion matrix:", cm)
print("TP（検出）が伸びておらず、1つ目に比べFP（誤検出）が増加してしまっている")

##################

#3つ目「sliding windowによる予測」した時の精度を評価
preds = []
for image_file in tqdm(image_files):
    # i番目の入力画像と正解のbbox
    image_path = os.path.join(image_dir, image_file)

    # 予測
    confidence_threshold = 0.6
    window_size = (300, 300)
    stride = 300
    out = ssd.predict_sw(image_path, window_size, stride)
    out = [pred for pred in out if pred["score"]>=confidence_threshold]
    out = sorted(out, key=lambda x:x["score"], reverse=True)
    pred = [p['bbox'] for p in out]
    preds.append(pred)

# 評価
score, cm = f1_scores(preds, ans)
print("f1_score:", score)
print("confusion matrix:", cm)
print("TP（検出）が他に比べ良く伸びており、その結果FN（未検出）が減少。FP（誤検出）も減っている")

