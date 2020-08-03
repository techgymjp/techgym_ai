#Tech-Gym-13-7-A
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
my_img_r = cv2.resize(img_r,(img_r.shape[1]*2 , img_r.shape[0]*2))

#画像を表示
plt.imshow(my_img_r)
plt.show()

#反転：引数に0を指定するとx軸中心
my_img_r = cv2.flip(img_r,0)

#画像を表示
plt.imshow(my_img_r)
plt.show()

#各画素のビットを操作して、ポジネガ反転する
my_img_r = cv2.bitwise_not(img_r)

#画像を表示
plt.imshow(my_img_r)
plt.show()

#閾値処理 THRESH_BINARY:しきい値を超えるピクセルはmaxValueにそれ以外は0にする
thr = 120
thr_max = 255
retval,my_img_r = cv2.threshold(img_r, thr , thr_max , cv2.THRESH_BINARY)

#画像を表示
plt.imshow(my_img_r)
plt.show()

#ぼかしをするNxN個のピクセルとの平均をとる
g_size = (9,9)
my_img_r = cv2.GaussianBlur(img_r,g_size,0)

#画像を表示
plt.imshow(my_img_r)
plt.show()

# 微分フィルタ
kernel = np.array([[0, 0, 0],
                   [0, -1, 1],
                   [0, 0, 0]])

# フィルタリングを行う
my_img_r = cv2.filter2D(img_r, -1, kernel)

#画像を表示
plt.imshow(my_img_r)
plt.show()


