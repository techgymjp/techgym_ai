#Techgym7-2-A-2

%matplotlib inline

import numpy as np
import matplotlib.pyplot as plt

# x、y座標
#-1から1まで0.1刻み
ar_min = -1.0
ar_max = 1.0
notch = 0.1

X = np.arange(ar_min, ar_max, notch)
Y = np.arange(ar_min, ar_max, notch)

#グリッド数
grid_num = int((abs(ar_min) + abs(ar_max)) / notch)

# 出力を格納するグリッド
Z = np.zeros((grid_num,grid_num))

#シグモイド関数
def sigmoid_function(x):
    return 1 / ( 1 + np.exp(-x))

#単一ニューロン
def simple_neuron(w_x,w_y,bias):
    # グリッドの各マスでニューロンの演算
    for i in range(grid_num):
        for j in range(grid_num):
        
            # 入力と重みの積の総和 + バイアス
            u = X[i]*w_x + Y[j]*w_y + bias
        
            # グリッドに出力を格納
            y = sigmoid_function(u)
            Z[j][i] = y

    print("w_x  w_y  bias : ",w_x,w_y,bias)
    # グリッドの表示
    plt.imshow(Z, "gray", vmin = 0.0, vmax = 1.0)
    plt.colorbar()
    plt.show()

#パラメーターを変更して実行
simple_neuron(0,0,0.1)
simple_neuron(-2.5,-3.0,0.1)
simple_neuron(0,3.0,0.1)
simple_neuron(4.0,3.0,0.1)

simple_neuron(-2.5,-3.0,10)
simple_neuron(-2.5,-3.0,-10)
simple_neuron(-2.5,-3.0,3)
simple_neuron(-2.5,-3.0,-1)
