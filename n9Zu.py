# word2vec データ読み込み
from gensim.models import KeyedVectors
import numpy as np
import pandas as pd
import json

# ダウンロード先のパスを指定
MODEL_FILENAME = "embeddings/stanby-jobs-200d-word2vector.bin"
w2v = KeyedVectors.load_word2vec_format(MODEL_FILENAME, binary=True)

# データの読み込み
df = pd.read_csv("words.csv") 

# 読み込んだデータのサンプルを取得
sample = df.sample(n=100)
co_sample = sample

# 閾値を決める
THRESHOLD = 0.4

# 結果をdictで保存
result = {}

# 類似度を計算
for i in sample["words"].values:
    tmp_list = []
    for j in co_sample["words"].values:
        tmp_dict = {}
        # word2vecにない単語はスルーする
        try:
            similarity = w2v.similarity(i, j)
            # 類似度が0.99以上は同じ単語とする
            # 類似度がTHRESHOLD以上のものを抽出
            if similarity < 0.99 and similarity > THRESHOLD:
                tmp_dict = {"類似度" : str(similarity), "単語" : j} 
        except:
            pass
        
        if tmp_dict != {}:
            tmp_list.append(tmp_dict)

    if tmp_list != []:
        result[i] = tmp_list

print(result)
f = open("result.json", "w")
json.dump(result, f, skipkeys=True, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
