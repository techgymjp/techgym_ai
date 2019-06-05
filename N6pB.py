#AI-TECHGYM-N-D
import numpy as np

#表示のためのライブラリの読み込み
import matplotlib.pyplot as plt
%matplotlib inline

#乱数
import numpy.random as random

#設定値
init_seed = 0
x_num = 100
y_num = 100
x_fig = 10
y_fig = 10

#シード値の設定
random.seed(init_seed)

# x軸、y軸のデータ
x = np.random.randn(x_num)
y = np.sin(x) + np.random.randn(y_num)

# グラフの大きさ指定
plt.figure(figsize=(x_fig, y_fig))

# グラフの描写 plt.scatter(x, y)でもよい
plt.plot(x, y, 'o')

#sin関数
x = np.linspace(-5, 5,100)
plt.plot(x, np.sin(x)) 

# グラフの中にある縦線と横線の表示
plt.grid(True)

# タイトル
plt.title('Title')

# X、Yの座標名
plt.xlabel('X')
plt.ylabel('Y')
