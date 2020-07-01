#techgym-10-3-A

import os
import cv2
import json
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
%matplotlib inline

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

#サイズ指定
plt.figure(figsize=(11,11))

# 画像を選択
index = 15
image_path = os.path.join(image_dir, image_files[index])
img = cv2.imread(image_path)
gt = annotation[index]

# 衛星データを表示
plt.imshow(img[:,:,::-1])

# 今操作したいaxis（画像）を選択
current_axis = plt.gca()

# (x1, y1, x2, y2) = (xmin, ymin, xmax, ymax)
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
