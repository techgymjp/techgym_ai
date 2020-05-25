#techgym7-6-A-2

# 中間層
class MiddleLayer:
　　　　# 初期設定
    def __init__(self, n_upper, n):
        self.w = wb_width * np.random.randn(n_upper, n)  # 重み（行列）
        self.b = wb_width * np.random.randn(n)  # バイアス（ベクトル）

    # 順伝播
    def forward(self, x):
        self.x = x
        u = np.dot(x, self.w) + self.b
        self.y =
    
    # 逆伝播
    def backward(self, grad_y):
        delta = 
        
        self.grad_w = np.dot(self.x.T, delta)
        self.grad_b = np.sum(delta, axis=0)
        
        self.grad_x = np.dot(delta, self.w.T)
        
    def update(self, eta):  # 重みとバイアスの更新
        self.w -= eta * self.grad_w
        self.b -= eta * self.grad_b

