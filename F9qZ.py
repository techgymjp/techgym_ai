#Tech-Gym-13-28-Q
#リアルタイム画像認識
#

from darkflow.net.build import TFNet
import cv2
import numpy as np

options = {"model": "cfg/yolo.cfg", "load": "bin/yolo.weights", "threshold": 0.1}
tfnet = TFNet(options)

# カメラの起動
cap = cv2.VideoCapture(0)

class_names = ['aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 
              'bus', 'car', 'cat', 'chair', 'cow', 'diningtable', 
              'dog', 'horse', 'motorbike', 'person', 'pottedplant',
              'sheep', 'sofa', 'train', 'tvmonitor']

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

def main():

    while(True):

        # escを押したら終了。
        k = cv2.waitKey(10);
        if k == ord('q'):  break;

if __name__ == '__main__':
    main()
