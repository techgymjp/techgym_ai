#Tech-Gym-13-4-Q
#OpenCV

import matplotlib.pyplot as plt
import urllib.request as req

%matplotlib inline

#ここにURLを入れる
req.urlretrieve(url, "test.png")

image = "test.png"
img = cv2.imread(image)

plt.imshow(img)
plt.show()

