#Tech-Gym-13-18-A
#ディープラーニング画像分類器:CNN
#手書き文字データ:モデル保存

from sklearn import datasets, svm
from sklearn.externals import joblib
from sklearn.metrics import accuracy_score

# アヤメのサンプルデータを読み込む
iris = datasets.load_iris()

# データを学習
model = svm.SVC()
model.fit(iris.data, iris.target)

# 学習済みデータを保存
joblib.dump(model, 'iris.pkl', compress=True)

# 保存した学習済みデータと分類器を読み込む
clf = joblib.load('iris.pkl')

# アヤメのサンプルデータを読み込み
iris = datasets.load_iris()

# 予測する
pre = clf.predict(iris.data)

# 正解率を調べる
print(accuracy_score(iris.target, pre))


