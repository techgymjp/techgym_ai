#techgym7-4-A-1

%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

# x、y座標(-1から1まで0.1刻み)
ar_min = -1.0
ar_max = 1.0
notch = 0.1

X = np.arange(ar_min, ar_max, notch)
Y = np.arange(ar_min, ar_max, notch)

#グリッド数
grid_num = int((abs(ar_min) + abs(ar_max)) / notch)

#出力を格納するグリッド
Z = np.zeros((grid_num,grid_num))

#シグモイド関数
def sigmoid_function(x):
    return 1 / ( 1 + np.exp(-x))

#ソフトマックス関数
def softmax_function(x):
    return np.exp(x)/np.sum(np.exp(x))

############################################################

# 重み
w_im = np.array([[1.0,2.0],
                               [2.0,1.0]])  # 中間層 2x2の行列
w_mo = np.array([[-1.0,1.0],
                                [1.0,-1.0]]) # 出力層 2x2の行列

# バイアス
b_im = np.array([0.3,-0.3]) # 中間層
b_mo = np.array([0.3,0.1])  # 出力層

# 中間層
def middle_layer(x, w, b):
    u = np.dot(x, w) + b
    return sigmoid_function(u) # シグモイド関数

# 出力層
def output_layer(x, w, b):
    u = np.dot(x, w) + b
    return softmax_function(u) # ソフトマックス関数

# 分類結果を格納するリスト
x_1 = []
y_1 = []
x_2 = []
y_2 = []

# グリッドの各マスでニューラルネットワークの演算
for i in range(grid_num):
    for j in range(grid_num):
        
        # 順伝播
        inp = np.array([X[i], Y[j]])
        mid = middle_layer(inp, w_im, b_im)
        out = output_layer(mid, w_mo, b_mo)
        
        # 確率の大小を比較し、分類する
        if out[0] > out[1]:
            x_1.append(X[i])
            y_1.append(Y[j])
        else:
            x_2.append(X[i])
            y_2.append(Y[j])

# 散布図の表示
plt.scatter(x_1, y_1, marker="+")
plt.scatter(x_2, y_2, marker="o")
plt.show()

############################################################

