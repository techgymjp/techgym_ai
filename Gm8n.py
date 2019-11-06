#AI-TECHGYM-1-12-A-3
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

def draw_2d_2groups(vectors, target1, target2, topn=100):
    similars1 = [w[0] for w in vectors.wv.most_similar(target1, topn=topn)]
    similars1.insert(0, target1)
    similars2 = [w[0] for w in vectors.wv.most_similar(target2, topn=topn)]
    similars2.insert(0, target2)
    similars = similars1 + similars2
    colors = ['b']+['g']*(topn)+ ['r']+['orangered']*(topn)
    X = [vectors.wv[w] for w in similars]
    pca = PCA(n_components=2)
    Y = pca.fit_transform(X)
    plt.figure(figsize=(20,20))
    plt.scatter(Y[:,0], Y[:,1], color=colors)
    for w, x, y, c in zip(similars[:], Y[:,0], Y[:,1], colors):
        plt.annotate(w, xy=(x, y), xytext=(3,3), textcoords='offset points', fontproperties=prop, fontsize=15, color=c)
    plt.show()

#単語を指定
word1="海"
word2="老人"

#グラフ描画
draw_2d_2groups(model,word1,word2,topn=100)