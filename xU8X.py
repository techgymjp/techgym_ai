#AI-TECHGYM-1-12-A-4
#自然言語処理

#インポート
from gensim.models import word2vec
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

#pandas
import pandas as pd

#PCA
from sklearn.decomposition import PCA

# k-means法を使うためのインポート
from sklearn.cluster import KMeans

#フォントの準備
#import urllib.request as req
#url = "https://github.com/hokuto-HIRANO/Word2Vec/raw/master/font/Osaka.ttc"
#req.urlretrieve(url, "./Osaka.ttc")

#フォントの指定
FONTPATH='./Osaka.ttc'
prop = font_manager.FontProperties(fname=FONTPATH)

#モデルの読み込み
model_path = './words.model'
model = word2vec.Word2Vec.load(model_path)

def draw_2d_2groups_k(vectors, target1, target2, topn=100):
    similars1 = [w[0] for w in vectors.wv.most_similar(target1, topn=topn)]
    similars1.insert(0, target1)
    similars2 = [w[0] for w in vectors.wv.most_similar(target2, topn=topn)]
    similars2.insert(0, target2)
    similars = similars1 + similars2
    colors = ['b']+['g']*(topn)+ ['r']+['orangered']*(topn)
    X = [vectors.wv[w] for w in similars]
    pca = PCA(n_components=2)
    Y = pca.fit_transform(X)
    
    # クラスター分析
    kmeans = KMeans(init='random', n_clusters=3)
    kmeans.fit(Y)
    z_pred = kmeans.predict(Y)
    
    # 順にx座標、y座標、cluster番号のデータを横に結合するためconcatでaxis=1を指定
    merge_data = pd.concat([pd.DataFrame(Y[:,0]), pd.DataFrame(Y[:,1]), pd.DataFrame(z_pred)], axis=1)
    merge_data.columns = ['X','Y','cluster']
    
    #グラフサイズ
    plt.figure(figsize=(20,20))
    
    #display(cluster_df)
    df0 = merge_data[merge_data.cluster == 0]
    df1 = merge_data[merge_data.cluster == 1]
    df2 = merge_data[merge_data.cluster == 2]

    #グラフのプロット
    plt.scatter(df0['X'],df0['Y'],color='blue',label='cluster0')
    plt.scatter(df1['X'],df1['Y'],color='red',label='cluster1')
    plt.scatter(df2['X'],df2['Y'],color='green',label='cluster2')
    
    for w, x, y in zip(similars[:], Y[:, 0], Y[:,1]):
        plt.annotate(w, xy=(x, y), xytext=(3,3), textcoords='offset points', fontproperties=prop, fontsize=15)
    plt.show()

#単語を指定
word1="海"
word2="老人"

#グラフ描画
draw_2d_2groups_k(model,word1,word2,topn=100)
