#Techgym8-2-A-1

# ライブラリのインポート
from keras.models import Sequential
from keras.layers import Dense, Activation

# 活性化関数の追加
model = Sequential()
model.add(Dense(10, input_shape=(51,)))
model.add(Activation("tanh"))
model.add(Dense(10))
model.add(Activation("relu"))
model.add(Dense(1))
model.add(Activation("sigmoid"))
