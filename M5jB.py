#Techgym8-1-A-2

# ライブラリのインポート
from keras.models import Sequential
from keras.layers import Dense

# モデルの定義
model = Sequential()
model.add(Dense(10 , input_shape = (51, )))
model.add(Dense(10))
model.add(Dense(1))

