#techgym7-6-A-1

# 出力層
class OutputLayer:
    # 初期設定
    def __init__(self, n_upper, n):
        self.w =  # 重み（行列）
        self.b =  # バイアス（ベクトル）
    
    # 順伝播
    def forward(self, x):
        self.x = x
        u =
        self.y =   # 恒等関数
    
    # 逆伝播
    def backward(self, t):
        delta =
        
        self.grad_w =
        self.grad_b =
        
        self.grad_x =

    # 重みとバイアスの更新
    def update(self, eta):
        self.w -=
        self.b -= 

