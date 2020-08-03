#Tech-Gym-12-7-Q
#OpenCV(画像処理)

import numpy as np
import cv2
import matplotlib.pyplot as plt
import urllib.request as req

%matplotlib inline

url = "http://www.ess.ic.kanagawa-it.ac.jp/std_img/colorimage/Lenna.jpg"
req.urlretrieve(url, "Lenna.jpg")

#画像の指定
img_r = cv2.imread("Lenna.jpg")

#サイズを2倍にする

#画像を表示

#反転：引数に0を指定するとx軸中心

#画像を表示

#各画素のビットを操作して、ポジネガ反転する

#画像を表示

#閾値処理 THRESH_BINARY:しきい値を超えるピクセルはmaxValueにそれ以外は0にする
thr = 120
thr_max = 255

#画像を表示

#ぼかしをするNxN個のピクセルとの平均をとる
g_size = (9,9)

#画像を表示

# 微分フィルタ
kernel = np.array([[0, 0, 0],
                   [0, -1, 1],
                   [0, 0, 0]])

# フィルタリングを行う

#画像を表示
