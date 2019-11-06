#AI-TECHGYM-1-9-A-2
#自然言語処理

#インポート
from gensim.models import Word2Vec

#モデル
sentences = [["猫", "鳴く", "にゃー"], ["犬", "鳴く", "わんわん"]]
model = Word2Vec(sentences, min_count=1)

#類似している単語を出力する
cat = model.wv.most_similar(positive=['猫']) 
#cat = model.wv.similar_by_vector('猫') 
#cat = model.wv.similar_by_word('猫') 
for item in cat:
    print(item[0], item[1])