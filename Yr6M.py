#Tech-Gym-13-26-Q
#リアルタイム画像認識
#

import torch
from IPython.display import Image, clear_output  # to display images

clear_output()
print('Setup complete. Using torch %s %s' % (torch.__version__, torch.cuda.get_device_properties(0) if torch.cuda.is_available() else 'CPU'))

#!python detect.py --weights yolov5s.pt --img 640 --conf 0.25 --source data/images/

#Image(filename='runs/detect/exp/zidane.jpg', width=600)
