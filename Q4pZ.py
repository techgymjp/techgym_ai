#AI-TECHGYM-1-13-Q-1
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
