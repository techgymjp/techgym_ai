#Tech-Gym-13-25-A
#リアルタイム画像認識

import numpy as np
import cv2

# 動画ファイルを開く
video = cv2.VideoCapture('./Dogs10820.mp4')

# PCに接続されたカメラの映像を表示する場合
#video = cv2.VideoCapture(0)

if not video.isOpened():
    raise RuntimeError

cv2.namedWindow('frame', cv2.WINDOW_AUTOSIZE)

while True:

    ok, frame = video.read()

    if not ok:
        break

    cv2.imshow('frame', frame)

    key_wait = int(1000 / 30)
    key = cv2.waitKey(key_wait)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
