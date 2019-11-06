#AI-TECHGYM-1-12-A-2
#自然言語処理

#インポート
from gensim.models import word2vec
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

#PCA
from sklearn.decomposition import PCA

#フォントの準備
import urllib.request as req
url = "https://github.com/hokuto-HIRANO/Word2Vec/raw/master/font/Osaka.ttc"
req.urlretrieve(url, "./Osaka.ttc")

#フォントの指定
FONTPATH='./Osaka.ttc'
prop = font_manager.FontProperties(fname=FONTPATH)

#モデルの読み込み
model_path = './words.model'
model = word2vec.Word2Vec.load(model_path)

#対象の単語
words = []
words.append("老人")
words.append("海")
words.append("ヘミングウェイ")
words.append("魚")
words.append("彼")

vectors = []

for w in words:
    vectors.append(model.wv[w])

#単語のベクトル表現を2次元に圧縮する
pca = PCA(n_components=2)
pca.fit(vectors)
vectors_pca = pca.transform(vectors)

for w in vectors_pca:
    #配列形式に整形
    print(np.array2string(w, separator=', ', formatter={'float_kind': lambda x: '{: .4f}'.format(x)}))

#ブロットする
k = 0
while k < len(vectors_pca):
    #点プロット
    plt.plot(vectors_pca[k][0], vectors_pca[k][1], ms=5.0, zorder=2, marker="o")
 
    #文字プロット
    plt.annotate(words[k], (vectors_pca[k][0], vectors_pca[k][1]), fontproperties=prop, fontsize=15)

    k += 1

#グラフ表示
plt.show()
