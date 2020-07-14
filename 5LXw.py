#techgym9-5-Q

#インポート
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

#学習係数
eta = 0.001

#使用する関数
def sigmoid(x):
    return 1/(1+np.exp(-x))

def init_w(n_upper,n):
    return np.random.randn(n_upper, n) * np.sqrt(2/n_upper)

#基底クラス
class BaseLayer:
    def update(self, eta):
        self.w -= eta * self.grad_w
        self.b -= eta * self.grad_b

#中間層
class MiddleLayer(BaseLayer):
    def __init__(self, n_upper, n):
        #初期値
        self.w = init_w(n_upper,n)
        self.b = np.zeros(n)

    def forward(self, x):
        self.x = x
        self.u = np.dot(x, self.w) + self.b
        # ReLU
        self.y = np.where(self.u <= 0, 0, self.u)
    
    def backward(self, grad_y):
        delta = grad_y * np.where(self.u <= 0, 0, 1)
        self.grad_w = np.dot(self.x.T, delta)
        self.grad_b = np.sum(delta, axis=0)
        self.grad_x = np.dot(delta, self.w.T)

# Generatorの出力層
class GenOutLayer(BaseLayer):
    def __init__(self, n_upper, n):
        #初期値
        self.w = init_w(n_upper,n)
        self.b = np.zeros(n)

    def forward(self, x):
        self.x = x
        u = np.dot(x, self.w) + self.b
        # tanh関数
        self.y = np.tanh(u)

    def backward(self, grad_y):
        delta = grad_y * (1 - self.y**2)
        
        self.grad_w = np.dot(self.x.T, delta)
        self.grad_b = np.sum(delta, axis=0)
        self.grad_x = np.dot(delta, self.w.T)

# Discriminatorの出力層
class DiscOutLayer(BaseLayer):
    def __init__(self, n_upper, n):
        #初期値
        self.w = init_w(n_upper,n)
        self.b = np.zeros(n)

    def forward(self, x):
        self.x = x
        u = np.dot(x, self.w) + self.b
        # シグモイド関数
        self.y = sigmoid(u)

    def backward(self, t):
        delta = self.y-t
        
        self.grad_w = np.dot(self.x.T, delta)
        self.grad_b = np.sum(delta, axis=0)
        self.grad_x = np.dot(delta, self.w.T)

# 全ての層での順伝播
def forward_propagation(x, layers):
    for layer in layers:
        layer.forward(x)
        x = layer.y
    return x

# 全ての層での逆伝播
def backpropagation(t, layers):
    grad_y = t
    for layer in reversed(layers):
        layer.backward(grad_y)
        grad_y = layer.grad_x
    return grad_y

# パラメータの更新
def update_params(layers):
    for layer in layers:
        layer.update(eta)

# 誤差計算
def get_error(y, t):
    # 二値の交差エントロピー誤差
    eps = 1e-7
    return -np.sum(t*np.log(y+eps) + (1-t)*np.log(1-y+eps)) / len(y)

# 正解率計算
def get_accuracy(y, t):
    correct = np.sum(np.where(y<0.5, 0, 1) == t)
    return correct / len(y)

##################################################

#ノイズの数
n_noise = 8

# 行数と列数
n_rows = 8
n_cols = 8
    
#層のサイズ
n_layer1 = 1
n_layer32 = 32
n_layer64 = 64

#画像の高さと幅
img_size = 8

# モデルの訓練
def train_model(x, t, prop_layers, update_layers):
    y =
    
    update_params()
    return ()


#各層を初期化
gen_layers = []

disc_layers = []

#画像生成して表示
def generate_images(i,rows,cols):
    # 画像の生成
    n_rows =
    n_cols =
    noise =
    g_imgs = forward_propagation(noise, gen_layers)
    g_imgs =  # 0-1の範囲にする

    img_size_spaced = img_size + 2
    matrix_image = np.zeros()  # 全体の画像

    # 生成された画像を並べて一枚の画像にする
    for r in range(n_rows):
        for c in range(n_cols):
            g_img = g_imgs[r*n_cols + c].reshape(img_size, img_size)
            top = r*img_size_spaced
            left = c*img_size_spaced
            matrix_image[top : top+img_size, left : left+img_size] = g_img

    plt.figure(figsize=(5, 5))
    plt.
    #軸目盛りのラベルと線を消す
    plt.tick_params(labelbottom=False, labelleft=False, bottom=False, left=False)
    plt.show()

#画像を表示
generate_images()
