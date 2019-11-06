#AI-TECHGYM-1-15-Q-1
#自然言語処理

#インポート
from gensim.models import KeyedVectors

# ダウンロード先のパスを指定
MODEL_FILENAME = "./stanby-jobs-200d-word2vector.bin"
w2v = KeyedVectors.load_word2vec_format(MODEL_FILENAME, binary=True)

print("単語を入力してください。\n")
word = input()
