#techgym9-8-A

#インポート
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

#学習係数
eta = 0.001

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

# モデルの訓練
def train_model(x, t, prop_layers, update_layers):
    y = forward_propagation(x, prop_layers)
    backpropagation(t, prop_layers)
    update_params(update_layers)
    return (get_error(y, t), get_accuracy(y, t))


#各層を初期化
gen_layers = [MiddleLayer(n_noise, n_layer32),
                         MiddleLayer(n_layer32, n_layer64),
                         GenOutLayer(n_layer64, img_size*img_size)]

disc_layers = [MiddleLayer(img_size*img_size, n_layer64),
                         MiddleLayer(n_layer64, n_layer32),
                         DiscOutLayer(n_layer32, n_layer1)]

#画像生成して表示
def generate_images(i,rows,cols):
    # 画像の生成
    n_rows = rows
    n_cols = cols
    noise = np.random.normal(0, 1, (n_rows*n_cols, n_noise))
    g_imgs = forward_propagation(noise, gen_layers)
    g_imgs = g_imgs/2 + 0.5  # 0-1の範囲にする

    img_size_spaced = img_size + 2
    matrix_image = np.zeros((img_size_spaced*n_rows, img_size_spaced*n_cols))  # 全体の画像

    # 生成された画像を並べて一枚の画像にする
    for r in range(n_rows):
        for c in range(n_cols):
            g_img = g_imgs[r*n_cols + c].reshape(img_size, img_size)
            top = r*img_size_spaced
            left = c*img_size_spaced
            matrix_image[top : top+img_size, left : left+img_size] = g_img

    plt.figure(figsize=(5, 5))
    plt.imshow(matrix_image.tolist(), cmap="Greys_r")
    #軸目盛りのラベルと線を消す
    plt.tick_params(labelbottom=False, labelleft=False, bottom=False, left=False)
    plt.show()


n_learn = 10001  # 学習回数
interval = 5000  # 経過の表示間隔
batch_size = 32 #バッチサイズ

# 手書き文字訓練データ
digits_data = datasets.load_digits()
x_train = np.asarray(digits_data.data)
x_train = x_train / 15*2-1  # -1~1の範囲に調整
t_train = digits_data.target

# 学習
batch_half = batch_size // 2
error_record = np.zeros((n_learn, 2))
acc_record = np.zeros((n_learn, 2))

for i in range(n_learn):

    # ノイズから画像を生成しDiscriminatorを訓練
    noise = np.random.normal(0, 1, (batch_half, n_noise))
    imgs_fake = forward_propagation(noise, gen_layers)  # 画像の生成
    t = np.zeros((batch_half, 1))  # 正解は0
    error, accuracy = train_model(imgs_fake, t, disc_layers, disc_layers)
    error_record[i][0] = error
    acc_record[i][0] = accuracy
    
    # 本物の画像を使ってDiscriminatorを訓練
    rand_ids = np.random.randint(len(x_train), size=batch_half)
    imgs_real = x_train[rand_ids, :]
    t = np.ones((batch_half, 1))  # 正解は1
    error, accuracy = train_model(imgs_real, t, disc_layers, disc_layers)
    error_record[i][1] = error
    acc_record[i][1] = accuracy


    # 結合したモデルによりGeneratorを訓練する
    noise = np.random.normal(0, 1, (batch_size, n_noise))
    t = np.ones((batch_size, 1))  # 正解は1
    train_model(noise, t, gen_layers+disc_layers, gen_layers)  # Generatorのみ訓練


##################################################

#step刻みで抜き出す
step = 20

# 誤差の推移
axis_x = range(1, n_learn+1, step)
axis_y = error_record[::step, :]
plt.figure(figsize=(16,9))
plt.plot(axis_x, axis_y[:, 0].tolist(), label="Error_fake")
plt.plot(axis_x, axis_y[:, 1].tolist(), label="Error_real")
plt.legend(fontsize=20)
plt.xlabel("n_learn",fontsize=20)
plt.ylabel("Error",fontsize=20)
plt.show()

#正解率の推移
axis_x = range(1, n_learn+1, step)
axis_y = acc_record[::step, :]
plt.figure(figsize=(16,9))
plt.plot(axis_x, axis_y[:, 0].tolist(), label="Acc_fake")
plt.plot(axis_x, axis_y[:, 1].tolist(), label="Acc_real")
plt.legend(fontsize=20)
plt.xlabel("n_learn",fontsize=20)
plt.ylabel("Accuracy",fontsize=20)
plt.show()
