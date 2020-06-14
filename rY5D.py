#Techgym8-2-A-2

# ライブラリのインポート
from keras.models import Sequential
from keras.layers import Dense, Activation

# 活性化関数の追加
model = Sequential()
# 中間層1
model.add(Dense(150, input_shape=(101,)))
model.add(Activation("sigmoid"))
# 中間層2
model.add(Dense(200))
model.add(Activation("tanh"))
# 中間層3
model.add(Dense(100))
model.add(Activation("relu"))
# 出力層4
model.add(Dense(10))
model.add(Activation("softmax"))

# モデルの確認
model.summary()
