#techgym-10-4-A

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

#各画像にどんなカテゴリが付いているのかを表すデータフレームを生成します
pieces = []
for i, annot in enumerate(annotation):
    image_name = image_files[i]
    for label in annot["labels"]:
        category = label["category"]
        pieces.append((image_name, category))
tmp = pd.DataFrame(pieces, columns=["name","category"])
display(tmp)

#各カテゴリのバウンディングボックスの数を数えます
print(tmp["category"].value_counts())

#1枚あたりのバウンディングボックスの数を求める為に、ファイル名でデータを集約します
tmp2 = tmp.groupby("name").count()
print(tmp2)

#集約結果の基本統計量を確認します
print(tmp2.describe())

#最も多くバウンディングボックスが付いている画像名を特定し、そのindexを取得します
file_name = tmp2["category"].idxmax()
print("file name(MAX) : ",file_name)
print("index(MAX) : ",image_files.index(file_name))
