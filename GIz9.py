#techgym-10-9-A

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

#変換
ans = []
for a1 in annotation:
    tmp = []
    for a2 in a1["labels"]:
        tmp.append((a2["box2d"]["x1"], a2["box2d"]["y1"], a2["box2d"]["x2"], a2["box2d"]["y2"]))
    ans.append(tmp)

##################################################################

#インポート
from evaluation import f1_score

# 画像を1枚選択
index = 4
image_path = os.path.join(image_dir, image_files[index])
img = cv2.imread(image_path)
data = annotation[index]

# 選択した画像に対してbboxの予測を行う
output = ssd.predict(image_path)

# 確信度の閾値
confidence_threshold = 0.25

# スコアが閾値以上のものだけに絞る
output_thresh = [prediction for prediction in output if prediction["score"]>= confidence_threshold]

# スコア順にソート
output_thresh = sorted(output_thresh, key=lambda x:x["score"], reverse=True)

# 正解データのbbox
print("正解データ", type(data["labels"][0]["box2d"]), data["labels"][0]["box2d"])

# 予測結果のbbox
print("予測結果", type(output_thresh[0]["bbox"]), output_thresh[0]["bbox"])

##################

# 画像を選択
index = 4
image_path = os.path.join(image_dir, image_files[index])
img = cv2.imread(image_path)
gt = annotation[index]
answer = ans[index]

# 予測
confidence_threshold = 0.25
out = ssd.predict(image_path)
out = [pred for pred in out if pred["score"]>=confidence_threshold]
out = sorted(out, key=lambda x:x["score"], reverse=True)

# 評価
pred = [p['bbox'] for p in out]
evaluation = f1_score(pred, answer)
print('f1score:', evaluation)

#表示
plot_bbox(img, gt, out)
print("１つ目：正解と予測の重複度を表すIoUが規定値(0.5)に達していないことから, 誤検出(FP)となっており、正解bboxも検出できていない為、未検出（FN）")

##################

# 画像を選択
index = 4
image_path = os.path.join(image_dir, image_files[index])
img = cv2.imread(image_path)
gt = annotation[index]
answer = ans[index]

# 予測
confidence_threshold = 0.25
out = ssd.predict(image_path, [horizontal_flip_image, horizontal_flip_bbox])
out = [pred for pred in out if pred["score"]>=confidence_threshold]
out = sorted(out, key=lambda x:x["score"], reverse=True)

# 評価
pred = [p['bbox'] for p in out]
evaluation = f1_score(pred, answer)
print('f1score:', evaluation)

#表示
plot_bbox(img, gt, out)
print("２つ目:正解と予測の重複度を表すIoUが規定値(0.5)に達していないことから, 誤検出(FP)となっており、正解bboxも検出できていない為、未検出（FN）")

##################

# 画像を選択
index = 4
image_path = os.path.join(image_dir, image_files[index])
img = cv2.imread(image_path)
gt = annotation[index]
answer = ans[index]

# 予測
confidence_threshold = 0.6
window_size = (300, 300)
stride = 300
out = ssd.predict_sw(image_path, window_size, stride)
out = [pred for pred in out if pred["score"]>=confidence_threshold]
out = sorted(out, key=lambda x:x["score"], reverse=True)

# 評価
pred = [p['bbox'] for p in out]
evaluation = f1_score(pred, answer)
print('f1score:', evaluation)

#表示
plot_bbox(img, gt, out)
print("3つ目：正解と予測の重複度を表すIoUが規定値(0.5)に達している為,検出（TP）されているが、誤検出（FP）もある")

##################

#AveragePrecision
from evaluation import ap

pred = [p['bbox'] for p in out]
evaluation = ap(pred, answer)
print(evaluation)
