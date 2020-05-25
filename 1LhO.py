#techgym7-6-A-3

%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

#入力と正解の用意
input_data = np.arange(0, np.pi*2, 0.1)  # 入力
input_data = (input_data-np.pi)/np.pi     # 入力を-1.0-1.0の範囲に収める

correct_data = np.sin(input_data)  # 正解
n_data = len(correct_data)             # データ数

# 各設定値
n_in = 1  # 入力層のニューロン数
n_mid = 3  # 中間層のニューロン数
n_out = 1  # 出力層のニューロン数

wb_width = 0.01  # 重みとバイアスの広がり具合
eta = 0.1               # 学習係数
epoch = 2001      # エポック
interval = 200      # 経過の表示間隔
