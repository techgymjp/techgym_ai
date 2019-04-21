# word2vec データ読み込み
from gensim.models import KeyedVectors
import numpy as np

# ダウンロード先のパスを指定
MODEL_FILENAME = "embeddings/stanby-jobs-200d-word2vector.bin"
w2v = KeyedVectors.load_word2vec_format(MODEL_FILENAME, binary=True)

# githubのサンプルを参照
# 計算した結果近い単語が出てくる
words = w2v.most_similar(positive=['テクノロジー', '金融'], negative=['IT'], topn=5)
for word in words:
  print(word)

