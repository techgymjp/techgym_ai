#techgym-10-1-A

import os
import cv2
import json
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
%matplotlib inline

#画像データの読み込みと可視化

image_dir = os.path.join("competition_data", "val_images")
print("directory path:", image_dir)
print()

# フォルダ内のファイル名のリストを取得
image_files = sorted(os.listdir(image_dir))

# 画像のファイル名を出力
print(image_files)
print()

# 画像の枚数を出力
print("total images:",len(image_files))

image_path = os.path.join(image_dir, image_files[1])
print("image path:", image_path)

# cv2を使い、画像を1枚読み込む
img = cv2.imread(image_path)
print(type(img))

print(img.shape)
print(img.dtype)

# BGRのまま可視化した場合とRGBに変換して可視化した場合の比較
plt.figure(figsize=(11,11))
plt.subplot(1,2,1)
plt.title("BGR")
plt.imshow(img)
plt.subplot(1,2,2)
plt.title("RGB")
# 「::-1」は反転の意味（BGRの反転がRGB）
plt.imshow(img[:,:,::-1])
plt.show()


image_path = os.path.join(image_dir, image_files[15])
img = cv2.imread(image_path)

# BGRのまま可視化した場合とRGBに変換して可視化した場合の比較
plt.figure(figsize=(11,11))
plt.subplot(1,2,1)
plt.title("BGR")
plt.imshow(img)
plt.subplot(1,2,2)
plt.title("RGB")
# 「::-1」は反転の意味（BGRの反転がRGB）
plt.imshow(img[:,:,::-1])
plt.show()

