# word2vec データ読み込み
from gensim.models import KeyedVectors

# ダウンロード先のパスを指定
MODEL_FILENAME = "embeddings/stanby-jobs-200d-word2vector.bin"
w2v = KeyedVectors.load_word2vec_format(MODEL_FILENAME, binary=True)

# githubのサンプルを参照

# numpyを使って独自で計算
