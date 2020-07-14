#techgym9-3-Q

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

##################################################

# Generatorの出力層
class GenOutLayer(BaseLayer):
    def __init__(self, n_upper, n):
        #初期値


    def forward(self, x):

    def backward(self, grad_y):

# Discriminatorの出力層
class DiscOutLayer(BaseLayer):
    def __init__(self, n_upper, n):
        #初期値


    def forward(self, x):


    def backward(self, t):


#インスタンス
gen =
print("w",gen.w)

#順伝搬
in_x =
gen.
print("x",gen.x)
print("y",gen.y)

#逆伝播
gen.
print("grad w",gen.grad_w)
print("grad b",gen.grad_b)
print("grad x",gen.grad_x)

#インスタンス
disc =
print("w",disc.w)

#順伝搬
in_x =
disc.forward(in_x)
print("x",disc.x)
print("y",disc.y)

#逆伝播
disc.
print("grad w",disc.grad_w)
print("grad b",disc.grad_b)
print("grad x",disc.grad_x)

