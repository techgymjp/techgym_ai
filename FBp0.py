#techgym9-4-A

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

mid = MiddleLayer(5,5)
gen = GenOutLayer(5,1)
disc = DiscOutLayer(5,1)

test_gen_layers = [mid,mid,gen]

x = 10
y = forward_propagation(x,test_gen_layers)
print("forward_propagation : y",y)

t = 10
backpropagation(t,test_gen_layers)

# 学習係数
eta = 0.001
update_params(test_gen_layers)

print("誤差計算",get_error(y[0],t))
print("正解率",get_accuracy(y[0],t))

test_disc_layers = [mid,mid,disc]

x = 10
y = forward_propagation(x,test_disc_layers)
print("forward_propagation : y",y)

t = 10
backpropagation(t,test_gen_layers)

# 学習係数
eta = 0.001
update_params(test_gen_layers)

print("誤差計算",get_error(y[0],t))
print("正解率",get_accuracy(y[0],t))

