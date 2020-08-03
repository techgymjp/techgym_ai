#Tech-Gym-13-28-A
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

        # 動画ストリームからフレームを取得
        ret, frame = cap.read()
        frame = cv2.resize(frame,(1000,600))
        result = tfnet.return_predict(frame)

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
                cv2.rectangle(frame, (tlx, tly), (brx, bry), class_colors[class_num], 2)

                #ラベルの作成
                text = label + " " + ('%.2f' % conf)  
                cv2.rectangle(frame, (tlx, tly - 15), (tlx + 100, tly + 5), class_colors[class_num], -1)
                cv2.putText(frame, text, (tlx, tly), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1)

        # 表示
        cv2.imshow("Show FLAME Image", frame) 

        # escを押したら終了。
        k = cv2.waitKey(10);
        if k == ord('q'):  break;

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()