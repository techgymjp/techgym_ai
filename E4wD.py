#Tech-Gym-13-11-A
#ディープラーニング画像分類器:CNN
#手書き文字データ
#60,000枚の28x28，10個の数字の白黒画像と10,000枚のテスト用画像データセット

#必要なライブラリ
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
%matplotlib inline
%config InlineBackend.figure_format = 'retina'

#MNISTデータ
from keras.datasets import mnist

(X_train, y_train), (X_test, y_test) = mnist.load_data()

#行列の大きさを確認
print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)     

#はじめの100個を表示
plt.figure(figsize=(15, 15))
gs = gridspec.GridSpec(10,10)

for i in range(10):
    for j in range(10):
        plt.axis("off")
        plt.subplot(gs[i,j])
        plt.imshow(X_test[i+j], "gray")
        plt.text(0, 5, y_test[i+j], fontsize=16, color='red')
plt.show()


