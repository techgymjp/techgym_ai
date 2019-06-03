#AI-TECHGYM-N-B
import numpy as np

#2から3までに9個の要素を持つ列
array = np.linspace(2,3,9)
display(array)

#0から8までの整数を発生します
np.arange(9)

# データの準備 3x3の行列にする
array1 = np.arange(9).reshape(3,3)
display(array1)

#「[行範囲:列範囲]」
#開始インデックスや終了インデックスを省略したときは、それぞれ「最初から」「末尾まで」という意味

#1行目
display(array1[0,:])

#1列目
display(array1[:,0])

array2 = np.arange(9,18).reshape(3,3)
display(array2)

#行列の各要素の掛け算
display(array1*array2)

#行列の掛け算
display(np.dot(array1, array2))
