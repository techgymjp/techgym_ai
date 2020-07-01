#techgym9-2-Q

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
        

    def forward(self, x):

    
    def backward(self, grad_y):


#インスタンス
mid =
print("w",mid.w)

#順伝搬
in_x =
mid.
print("u",mid.u)
print("y",mid.y)

#逆伝播
mid.
print("grad w",mid.grad_w)
print("grad b",mid.grad_b)
print("grad x",mid.grad_x)
