#Tech-Gym-13-27-Q
#リアルタイム画像認識
#

from darkflow.net.build import TFNet
import cv2
import numpy as np

options = {"model": "cfg/yolo.cfg", "load": "bin/yolo.weights", "threshold": 0.1}

tfnet = TFNet(options)

class_names = ['aeroplane', 'bicycle', 'bird', 'boat', 'bottle',
              'bus', 'car', 'cat', 'chair', 'cow', 'diningtable',
              'dog', 'horse', 'motorbike', 'person', 'pottedplant',
              'sheep', 'sofa', 'train', 'tvmonitor']

imgcv = cv2.imread("./sample_img/sample_dog.jpg")
result = tfnet.return_predict(imgcv)
print(result)

num_classes = len(class_names)
class_colors = []
for i in range(0, num_classes):
    hue = 255*i/num_classes
    col = np.zeros((1,1,3)).astype("uint8")
    col[0][0][0] = hue
    col[0][0][1] = 128
    col[0][0][2] = 255
    cvcol = cv2.cvtColor(col, cv2.COLOR_HSV2BGR)
    col = (int(cvcol[0][0][0]), int(cvcol[0][0][1]), int(cvcol[0][0][2]))
    class_colors.append(col)

for item in result:
    tlx = item['topleft']['x']
    tly = item['topleft']['y']
    brx = item['bottomright']['x']
    bry = item['bottomright']['y']
    label = item['label']
    conf = item['confidence']

    if conf > 0.6:

        for i in class_names:
            if label == i:
                class_num = class_names.index(i)
                break

        #枠の作成
        cv2.rectangle(imgcv, (tlx, tly), (brx, bry), class_colors[class_num], 2)

        #ラベルの作成
        text = label + " " + ('%.2f' % conf)
        cv2.rectangle(imgcv, (tlx, tly - 15), (tlx + 100, tly + 5), class_colors[class_num], -1)
        cv2.putText(imgcv, text, (tlx, tly), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1)

# 書き出し
cv2.imwrite("./sample_img/sample_dog2.jpg", imgcv)

