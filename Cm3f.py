#Tech-Gym-7-19
#モデル比較（異なるデータ：手書き文字)

#可視化ライブラリ
import matplotlib.pyplot as plt
%matplotlib inline

# 分析対象データ
from sklearn.datasets import load_digits

digits = load_digits()

# 画像の表示
plt.figure(figsize=(20,5))
for label, img in zip(digits.target[:10], digits.images[:10]):
    plt.subplot(1,10,label+1)
    plt.axis('off')
    plt.imshow(img,cmap=plt.cm.gray_r,interpolation='nearest')
    plt.title('Number:{0}'.format(label))
