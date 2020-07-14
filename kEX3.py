#techgym9-4-Q

#インポート
import numpy as np

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

##################################################

# 全ての層での順伝播
def forward_propagation(x, layers):


# 全ての層での逆伝播
def backpropagation(t, layers):


# パラメータの更新
def update_params(layers):


# 誤差計算
def get_error(y, t):
    # 二値の交差エントロピー誤差
    eps = 1e-7
    return

# 正解率計算
def get_accuracy(y, t):

    return correct / len(y)

mid =
gen =
disc =

test_gen_layers = []

x =
y =
print("forward_propagation : y",y)

t =
backpropagation()

# 学習係数
eta = 0.001
update_params()

print("誤差計算")
print("正解率")

test_disc_layers = []

x =
y =
print("forward_propagation : y",y)

t =
backpropagation()

# 学習係数
eta = 0.001
update_params()

print("誤差計算")
print("正解率")

