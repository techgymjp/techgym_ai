#techgym9-1-A

#インポート

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

#インスタンス
base = BaseLayer()

base.test_set_value(0,0,3,4)
base.update(0.2)
base.update(0.2)
base.update(0.2)

print("w : ",base.w)
print("b : ",base.b)
print("grad_w : ",base.grad_w)
print("grad_b : ",base.grad_b)
