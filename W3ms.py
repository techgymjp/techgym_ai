#AI-TECHGYM-1-15-A-2
#自然言語処理

#インポート
from gensim.models import KeyedVectors

# ダウンロード先のパスを指定
MODEL_FILENAME = "./stanby-jobs-200d-word2vector.bin"
w2v = KeyedVectors.load_word2vec_format(MODEL_FILENAME, binary=True)

print("連想ゲームのはじめの単語を入力してください(終了:Q)")

while True:
    #インプット
    word = input()
    if word == 'Q':
        break

    try:
        job = w2v.most_similar(word,topn=1)
    except :
        print("モデルにない単語なのでもう一度入力してください。\n")
        continue

    #連想した単語
    word_sim = job[0][0]

    #マジカルバナナ
    print("'" + word + "'と言ったら'" + word_sim + "'です。\n")
    print("'" + word_sim + "'と言ったら？'\n")
