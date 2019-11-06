#AI-TECHGYM-1-10-A-3
#自然言語処理

#インポート
from gensim.models import Word2Vec
from janome.tokenizer import Tokenizer

#形態素解析のオブジェクト
text = Tokenizer()

#txtファイルからデータの読み込み
text_file = open("techgym-AI.txt")
txt = text_file.read()
 
#読み込んだデータを形態素解析
results = []
lines = txt.split("\r\n")
for i in lines:
    text_c = text.tokenize(i,wakati=True)
    results.append(text_c)

#モデル
model = Word2Vec(results, min_count=1)
vector = model.wv['プログラミング']

#ベクトル表現
print(vector)

pro = model.wv.most_similar(positive=['プログラミング'], topn=5)
#pro = model.wv.similar_by_vector('プログラミング') 
#pro = model.wv.similar_by_word('プログラミング') 
for item in pro:
    print(item[0], item[1])