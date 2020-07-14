#techgym9-2-A

#インポート
import numpy as np

#基底クラス
class BaseLayer:
    def update(self, eta):
        self.w -= eta * self.grad_w
        self.b -= eta * self.grad_b

    def test_set_value(self,s1,s2,s3,s4):
        self.w = s1
        self.b = s2
        self.grad_w = s3
        self.grad_b = s4

##################################################

#中間層
class MiddleLayer(BaseLayer):
    def __init__(self, n_upper, n):
        #初期値
        self.w = np.random.randn(n_upper, n) * np.sqrt(2/n_upper)
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

#インスタンス
mid = MiddleLayer(5,1)
print("w",mid.w)

#順伝搬
in_x = np.array([[0,1,2,3,4]])
mid.forward(in_x)
print("u",mid.u)
print("y",mid.y)

#逆伝播
mid.backward(10)
print("grad w",mid.grad_w)
print("grad b",mid.grad_b)
print("grad x",mid.grad_x)
