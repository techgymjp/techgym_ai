#Tech-Gym-13-6-A
#OpenCV(画像処理)

import numpy as np
import cv2

import matplotlib.pyplot as plt
%matplotlib inline

#画像のサイズ
size = 512
img_size = (size,size)

#要素が[0,0,255]の行列をつくる
my_img = np.array([[[ 0, 0, 255] for _ in range(img_size[1])]
                   for _ in range(img_size[0])], dtype="uint8")

#数値として表示
print(my_img)

#画像として表示
plt.imshow(my_img)
plt.show()
