#AI-TECHGYM-1-6-A-1
#教師なし学習 PCA

#データ加工・処理・分析ライブラリ
import pandas as pd

#可視化ライブラリ
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
%matplotlib inline

#インポート
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

#乳がんデータを読み込むためのインポート
from sklearn.datasets import load_breast_cancer

#乳がんデータの取得
cancer = load_breast_cancer()

#三次元のグラフ
fig = plt.figure()
ax_3d = Axes3D(fig)
ax_3d.set_xlabel(cancer.feature_names[0])
ax_3d.set_ylabel(cancer.feature_names[1])
ax_3d.set_zlabel(cancer.feature_names[2])
ax_3d.view_init(elev=10., azim=-15)
ax_3d.plot(cancer.data[:,0],cancer.data[:,1],cancer.data[:,2],marker="o",linestyle='None',color='black')
plt.show()

#標準化
sc = StandardScaler()
sc.fit(cancer.data)
X_std = sc.transform(cancer.data)

#主成分分析
pca = PCA(n_components=2)
pca.fit(X_std)
X_pca = pca.transform(X_std)

#属性表示
print('X_pca shape:{}'.format(X_pca.shape))
print('Explained variance ratio:{}'.format(pca.explained_variance_ratio_))

#列にラベルをつける、1つ目が第1主成分、2つ目が第2主成分
X_pca = pd.DataFrame(X_pca, columns=['pc1','pc2'])

#上のデータに、目的変数（cancer.target）を紐づける、横に結合
X_pca = pd.concat([X_pca, pd.DataFrame(cancer.target, columns=['target'])], axis=1)

#悪性、良性を分ける
pca_malignant = X_pca[X_pca['target']==0]
pca_benign = X_pca[X_pca['target']==1]

#悪性、良性をプロット
ax = pca_malignant.plot.scatter(x='pc1', y='pc2', color='red', label='malignant');
pca_benign.plot.scatter(x='pc1', y='pc2', color='blue', label='benign', ax=ax);