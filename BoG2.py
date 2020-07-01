#techgym-10-3-Q

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
index =
image_path =
img =
gt =

# 衛星データを表示
plt.imshow()

# 今操作したいaxis（画像）を選択
current_axis = plt.gca()

# (x1, y1, x2, y2) = (xmin, ymin, xmax, ymax)
for label in gt["labels"]:
    # バウンディングボックスの座標から始点と幅、高さを算出し、四角形を生成
    xmin =
    ymin =
    width =
    height =
    rect =
    
    # 表示名はカテゴリ名とする為、カテゴリ名を取得
    category =

    # 四角形とカテゴリ名を画像中に表示
    current_axis.add_patch(rect)
    current_axis.text()
