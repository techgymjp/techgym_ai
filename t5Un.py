#Tech-Gym-13-4-A
#OpenCV(画像処理)

import cv2
import matplotlib.pyplot as plt
import urllib.request as req

%matplotlib inline

url ="http://uta.pw/shodou/img/13/3609.png"
req.urlretrieve(url, "test.png")

image = "test.png"
img = cv2.imread(image)

plt.imshow(img)
plt.show()
