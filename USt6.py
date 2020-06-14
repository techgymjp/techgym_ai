#Techgym8-4-A

# ライブラリのインポート
from keras.models import Sequential
from keras.layers import Dense, Flatten, Activation
from keras.layers import Conv2D, MaxPooling2D

# モデルの定義
model = Sequential()
# 1. 畳み込み層(フィルタサイズ=6, カーネルサイズ=(3,3), 入力サイズ=(32,32,3))

# 2. 活性化関数(Sigmoid)

# 3. プーリング層(プーリングサイズ=(2,2))

# 4. 畳み込み層(フィルタサイズ=12, カーネルサイズ=(3,3))

# 5. 活性化関数(Sigmoid)

# 6. プーリング層(プーリングサイズ=(2,2))

# 7. 平坦化()

# 8. 全結合層(出力=120)

# 9. 活性化関数(Sigmoid)

# 10. 全結合層(出力=60)

# 11. 活性化関数(Sigmoid)

# 12. 全結合層(出力=10)

# 13. 活性化関数(Softmax)


# モデルの確認

