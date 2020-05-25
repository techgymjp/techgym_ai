#Techgym7-2-A-2

%matplotlib inline

import numpy as np
import matplotlib.pyplot as plt

# x、y座標
#-1から1まで0.1刻み
ar_min = -1.0
ar_max = 1.0
notch = 0.1

X =
Y =

#グリッド数
grid_num =

# 出力を格納するグリッド
Z =

#シグモイド関数
def sigmoid_function(x):
    
    
#単一ニューロン
def simple_neuron(w_x,w_y,bias):
    # グリッドの各マスでニューロンの演算
    for i in range(grid_num):
        for j in range(grid_num):
        

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
