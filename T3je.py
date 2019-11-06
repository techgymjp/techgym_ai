#AI-TECHGYM-1-6-A-2
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

#アヤメのデータを読み込むためのインポート
from sklearn.datasets import load_iris

#サンプルデータ
iris = load_iris()

#三次元のグラフ
fig = plt.figure()
ax_3d = Axes3D(fig)
ax_3d.set_xlabel(iris.feature_names[1])
ax_3d.set_ylabel(iris.feature_names[2])
ax_3d.set_zlabel(iris.feature_names[3])
ax_3d.view_init(elev=10., azim=-15)
ax_3d.plot(iris.data[:,1],iris.data[:,2],iris.data[:,3],marker="o",linestyle='None',color='black')
plt.show()

#標準化
sc = StandardScaler()
sc.fit(iris.data)
X_std = sc.transform(iris.data)

#主成分分析
pca = PCA(n_components=2)
pca.fit(X_std)
X_pca = pca.transform(X_std)

print('主成分分析前のデータ次元：{}'.format(iris.data.shape))
print('主成分分析後のデータ次元：{}'.format(X_pca.shape))

#グラフ化
merge_data = pd.concat([pd.DataFrame(X_pca[:,0]), pd.DataFrame(X_pca[:,1]), pd.DataFrame(iris.target)], axis=1)
merge_data.columns = ['pc1','pc2', 'target']

#データを分ける
iris_0 = merge_data[iris.target==0]
iris_1 = merge_data[iris.target==1]
iris_2 = merge_data[iris.target==2]

#プロット
ax = iris_0.plot.scatter(x='pc1', y='pc2',color='blue', label='target-0')
iris_1.plot.scatter(x='pc1', y='pc2',color='red', label='target-1', ax=ax)
iris_2.plot.scatter(x='pc1', y='pc2',color='green', label='target-2', ax=ax)
