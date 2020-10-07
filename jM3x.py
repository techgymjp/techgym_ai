#Tech-Gym-13-8-Q
#ディープラーニング画像分類器:CNN

import numpy as np
import matplotlib.pyplot as plt
import urllib.request
%matplotlib inline

#urlからDownloadできないときはgithubに登録されているcircle.npyを使用する
url = "https://aidemystorageprd.blob.core.windows.net/data/5100_cnn_data/circle.npy"
local_filename, headers = urllib.request.urlretrieve(url)
X = np.load(local_filename)

#円の画像を表示する

# 畳み込み層

# カーネル(フィルタ)
W = np.array([[0,1,0],
              [0,1,0],
              [0,1,0]])

#カーネルの画像を表示

# 畳み込み

#畳み込み処理をした画像ｗの表示

