# word2vec データ読み込み
from gensim.models import KeyedVectors
import numpy as np
import pandas as pd

# ダウンロード先のパスを指定
MODEL_FILENAME = "embeddings/stanby-jobs-200d-word2vector.bin"
w2v = KeyedVectors.load_word2vec_format(MODEL_FILENAME, binary=True)

# データの読み込み
df = pd.read_csv("words.csv") 

vectors = []
tmp_vec = ""
for i in range(0, 200):
    tmp_vec = tmp_vec + " " + str(i * 0)
tmp_vec = "[" + tmp_vec + "]" 

for row in df["words"].values:
    try:
        vectors.append(w2v[row])
    except Exception as e:
        vectors.append(tmp_vec)

df["vectors"] = vectors
df.to_csv("words2vector.csv",index=False)
