#techgym7-3-A-1

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

############################################################

# 重み
w_im = np.array([[4.0,4.0],
                 [4.0,4.0]])  #中間層 2x2の行列
w_mo = np.array([[1.0],
                 [-1.0]])     #出力層 2x1の行列

# バイアス
b_im = np.array([3.0,-3.0])   #中間層
b_mo = np.array([0.1])        #出力層

#中間層(シグモイド関数)
def middle_layer_s(x, w, b):
    u = np.dot(x, w) + b
    return sigmoid_function(u)

#出力層(恒等関数)
def output_layer(x, w, b):
    u = np.dot(x, w) + b
    return u

# グリッドの各マスでニューラルネットワークの演算
for i in range(grid_num):
    for j in range(grid_num):

        #順伝播
        inp = np.array([X[i], Y[j]])           #入力層
        mid = middle_layer_s(inp, w_im, b_im)  #中間層
        out = output_layer(mid, w_mo, b_mo)    #出力層
        
        #グリッドに出力を格納
        Z[j][i] = out[0]

#表示
plt.imshow(Z, "gray", vmin = 0.0, vmax = 1.0)
plt.colorbar()
plt.show()

############################################################

#ReLU
def relu_function(x):
    return np.where(x <= 0, 0, x)

#中間層(ReLU関数)
def middle_layer_r(x, w, b):
    u = np.dot(x, w) + b
    return relu_function(u)


# グリッドの各マスでニューラルネットワークの演算
for i in range(grid_num):
    for j in range(grid_num):

        #順伝播
        inp = np.array([X[i], Y[j]])           #入力層
        mid = middle_layer_r(inp, w_im, b_im)  #中間層
        out = output_layer(mid, w_mo, b_mo)    #出力層
        
        #グリッドに出力を格納
        Z[j][i] = out[0]

#表示
plt.imshow(Z, "gray", vmin = 0.0, vmax = 1.0)
plt.colorbar()
plt.show()

