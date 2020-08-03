#Tech-Gym-13-8-A
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
plt.imshow(X)
plt.title("The original image", fontsize=18)
plt.show()

# 畳み込み層
class Conv:
    # Wは3x3で固定している、stridesやpaddingは考慮していない
    def __init__(self, W):
        self.W = W
    def f_prop(self, X):
        #出力用の行列を初期化
        out = np.zeros((X.shape[0]-2, X.shape[1]-2))
        for i in range(out.shape[0]):
            for j in range(out.shape[1]):
                x = X[i:i+3, j:j+3]
                # 要素ごとの積の合計をとっています
                out[i,j] = np.dot(self.W.flatten(), x.flatten())
        return out

# カーネル(フィルタ)
W = np.array([[0,1,0],
              [0,1,0],
              [0,1,0]])

#カーネルの画像を表示
plt.imshow(W)
plt.suptitle("kernel", fontsize=18)
plt.show()

# 畳み込み
conv1 = Conv(W); C = conv1.f_prop(X)

#畳み込み処理をした画像ｗの表示
plt.imshow(C)
plt.suptitle("Convolution result", fontsize=18)
plt.show()
