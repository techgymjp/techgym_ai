#AI-TECHGYM-1-9-A-3
#自然言語処理

#インポート
from gensim.models import Word2Vec
import numpy as np

#モデル
sentences = [["猫", "鳴く", "にゃー"], ["犬", "鳴く", "わんわん"]]
model = Word2Vec(sentences, min_count=1)

#コサイン類似度
ret_s = model.wv.n_similarity(['犬'],['猫']) 
print(ret_s)

#numpyを使って計算
#コサイン類似度を使う
def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

word1 = "犬"
word2 = "猫"
print(cos_sim(model.wv[word1], model.wv[word2]))