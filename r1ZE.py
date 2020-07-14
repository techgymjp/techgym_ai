#techgym-10-2-A

import os
import cv2
import json
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
%matplotlib inline

#ディレクトリの設定
image_dir = os.path.join("competition_data", "val_images")

# フォルダ内のファイル名のリストを取得
image_files = sorted(os.listdir(image_dir))

##################################################################

#画像データの読み込みと可視化
annotations_dir = os.path.join('competition_data', 'val_annotations')
annotations_files = sorted(os.listdir(annotations_dir))

# メタデータのファイル名を出力
print(annotations_files)
print()

# メタデータのデータ数を出力
print('total number of annotation files:', len(annotations_files))

annotation = []
for file in annotations_files:
    with open(os.path.join(annotations_dir,file)) as f:
        data = json.load(f)
        annotation.append(data)

#アノテーション表示
print(annotation[4])

##################################################################

#取り出す
index = 15
data = annotation[index]
print(type(data))
print("place", data["attributes"]["place"])

# 1つ目のアノテーションデータ
print("labels", data["labels"][0]["category"])
print("box2d_x1", data["labels"][0]["box2d"]["x1"])

# アノテーション数
print("number of annotations:", len(data["labels"]))

##################################################################

#サイズ指定
plt.figure(figsize=(5,5))

# 操作したいaxis（画像）を選択
current_axis = plt.gca()

# 四角形を生成（始点座標を(0.5,0.5)とし、そこから幅0.2、高さ0.4の四角形を描画、色は赤で、塗りつぶしはなし）
rect = plt.Rectangle((0.5,0.5), 0.2, 0.4, color="r", fill=False)

# 今選択したaxisに四角形を追加
current_axis.add_patch(rect)

plt.show()

##################################################################

#サイズ指定
plt.figure(figsize=(5,5))

# 操作したいaxis（画像）を選択
current_axis = plt.gca()

# 始点（0.5,0.5）から"test"という文字を文字サイズ大きめで表示
plt.text(0.5, 0.5, "test", size="x-large")

# 始点（0.2,0.2）から"test"という文字を文字サイズ大きめで表示、かつ文字を四角で囲み、色を赤とする
plt.text(0.2, 0.2, "text", size="x-large", color="w", bbox={"facecolor":"r"})

plt.show()

