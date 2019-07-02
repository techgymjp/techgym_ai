# word2vec データ読み込み
from gensim.models import KeyedVectors
import pandas as pd

# ダウンロード先のパスを指定
MODEL_FILENAME = "embeddings/stanby-jobs-200d-word2vector.bin"
w2v = KeyedVectors.load_word2vec_format(MODEL_FILENAME, binary=True)

# データの読み込み
df = pd.read_csv("words.csv") 

# numpyを使って独自で計算
# lesson2で使ったコサイン類似度の関数を使って各単語同士の類似度を計算
