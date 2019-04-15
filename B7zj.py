# word2vec データ読み込み
from gensim.models import KeyedVectors
import numpy as np

# ダウンロード先のパスを指定
MODEL_FILENAME = "embeddings/stanby-jobs-200d-word2vector.bin"
w2v = KeyedVectors.load_word2vec_format(MODEL_FILENAME, binary=True)

# githubのサンプルを参照
sim_vec = w2v.most_similar('Java', topn=5)
print(sim_vec)

# numpyを使って独自で計算
# コサイン類似度を使う
# cosine類似度
def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

word1 = "Java"
word2 = "PHP"
print(cos_sim(w2v[word1], w2v[word2]))
