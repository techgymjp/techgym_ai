#Tech-Gym-13-12-Q
#ディープラーニング画像分類器:CNN
#手書き文字データ

#必要なライブラリ
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
%matplotlib inline

#keras
from keras.models import Sequential
from keras.utils.np_utils import to_categorical
from keras.layers import Dense, Activation

#性能評価
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

#MNISTデータ
from keras.datasets import mnist

(X_train, y_train), (X_test, y_test) = mnist.load_data()

#行列の大きさを確認
print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)  

#はじめの6000個を1次元行列の形に変更

#行列の大きさを確認

#モデルのインスタンスを作成

# 入力ユニット数は784、1つ目の全結合層の出力ユニット数は256

# 2つ目の全結合層の出力ユニット数は128

# 3つ目の全結合層（出力層）の出力ユニット数は10

#モデルの生成

#学習

#acc、val_accのプロット

#モデル構造

#モデル評価

#混合行列


#性能評価



