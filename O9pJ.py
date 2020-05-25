#techgym7-5-A

%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt


#二乗和誤差を定義する
def square_sum(y, t):
    return 1.0/2.0 * np.sum(np.square(y - t))

#入力値
y_array = np.array([1,2,3])
t_array = np.array([2,3,4])

#誤差を計算する
err = square_sum(y_array, t_array)
print("ERR:",err)

###################################

#x,yの値
x = np.linspace(1.0e-03, 1)
y = - np.log(x)

#グラフをプロット
plt.plot(x, y)
plt.show()

#交差エントロピーの定義
def cross_entropy(y, t):
    return - np.sum(t * np.log(y + 1e-7))

#入力値
y_array = np.array([0.9,0.1,0.1])
t_array = np.array([1,0,0])

#誤差を計算する
err = cross_entropy(y_array,t_array)
print("ERR:",err)

###################################

