#Tech-Gym-13-10-Q
#ディープラーニング画像分類器:CNN
#プーリング層
#畳み込み層の出力を縮約してデータの量を削減する層

import numpy as np
import matplotlib.pyplot as plt
import urllib.request
%matplotlib inline

#urlからDownloadできないときはgithubに登録されているcircle.npyを使用する
url = "https://aidemystorageprd.blob.core.windows.net/data/5100_cnn_data/circle.npy"
local_filename, headers = urllib.request.urlretrieve(url)
X = np.load(local_filename)

plt.imshow(X)
plt.title("The original image", fontsize=12)
plt.show()

#畳み込み層を定義
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

#プーリング層


def show_image(G1,G2,G3,G4):
    plt.subplot(1,4,1); plt.imshow(G1)
    plt.subplot(1,4,2); plt.imshow(G2)
    plt.subplot(1,4,3); plt.imshow(G3)
    plt.subplot(1,4,4); plt.imshow(G4)

# カーネル(フィルタ)
W1 = np.array([[0,1,0],
               [0,1,0],
               [0,1,0]])

W2 = np.array([[0,0,0],
               [1,1,1],
               [0,0,0]])

W3 = np.array([[1,0,0],
               [0,1,0],
               [0,0,1]])

W4 = np.array([[0,0,1],
               [0,1,0],
               [1,0,0]])

show_image(W1,W2,W3,W4)
plt.suptitle("kernel", fontsize=12)
plt.show()

# 畳み込み
conv1 = Conv(W1); C1 = conv1.f_prop(X)
conv2 = Conv(W2); C2 = conv2.f_prop(X)
conv3 = Conv(W3); C3 = conv3.f_prop(X)
conv4 = Conv(W4); C4 = conv4.f_prop(X)

show_image(C1,C2,C3,C4)
plt.suptitle("Convolution result", fontsize=12)
plt.show()

# プーリング


