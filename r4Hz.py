#Tech-Gym-13-5-A
#OpenCV(画像処理)

import cv2
import matplotlib.pyplot as plt
import urllib.request as req

%matplotlib inline

url = "http://www.ess.ic.kanagawa-it.ac.jp/std_img/colorimage/Lenna.jpg"
req.urlretrieve(url, "Lenna.jpg")

#画像の指定
image = "Lenna.jpg"
img_r = cv2.imread(image)

#画像を表示
plt.imshow(img_r)
plt.show()

#色空間を変換する
#BGR -> RGB
img = cv2.cvtColor(img_r, cv2.COLOR_BGR2RGB)

#変換後を表示
plt.imshow(img)
plt.show()

#軸の表示をなしにして表示
plt.axis("off")
plt.imshow(img)
plt.show()
