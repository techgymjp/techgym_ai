#AI-TECHGYM-1-13-A-1
#自然言語処理

# word2vec データ読み込み
from gensim.models import KeyedVectors

#ファイルの準備
import os
import urllib.request

title = "stanby-jobs-200d-word2vector.bin"
if not os.path.exists(title):
    print(title + " DOWNLOAD.")
    url = "https://github.com/bizreach/ai/releases/download/2018-03-13/stanby-jobs-200d-word2vector.bin"
    urllib.request.urlretrieve(url,"{0}".format(title))
else :
    print(title + " EXIST.")

# stanby-jobs-200d-word2vector.bin が見つからない時はこちらをダウンロードして利用してください
# https://drive.google.com/file/d/1uJe1vhwzoGVUqz3gYUmoeMUDOabl6ojx/view?usp=sharing

# ダウンロード先のパスを指定
MODEL_FILENAME = "./stanby-jobs-200d-word2vector.bin"
w2v = KeyedVectors.load_word2vec_format(MODEL_FILENAME, binary=True)

#計算した結果近い単語が出てくる
print("「テクノロジー」")
words = w2v.most_similar('テクノロジー', topn=5)
for word in words:print(word)
print('\n')

print("「テクノロジー」＋「金融」")
words = w2v.most_similar(positive=['テクノロジー', '金融'], topn=5)
for word in words:print(word)
print('\n')

print("「テクノロジー」＋「金融」ー「IT」")
words = w2v.most_similar(positive=['テクノロジー', '金融'], negative=['IT'], topn=5)
for word in words:print(word)
print('\n')

print("「テクノロジー」(ベクトル)")
word1 = w2v['テクノロジー']
words = w2v.similar_by_vector(word1, topn=5)
for word in words:print(word)
print('\n')

print("「テクノロジー」＋「金融」(ベクトル)")
word1 = w2v['テクノロジー']
word2 = w2v['金融']
word_base = word1 + word2
words = w2v.similar_by_vector(word_base, topn=5)
for word in words:print(word)
print('\n')

print("「テクノロジー」＋「金融」?「IT」(ベクトル)")
word1 = w2v['テクノロジー']
word2 = w2v['金融']
word3 = w2v['IT']
word_base = word1 + word2 - word3
words = w2v.similar_by_vector(word_base, topn=5)
for word in words:print(word)
print('\n')
