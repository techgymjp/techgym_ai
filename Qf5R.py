#AI-TECHGYM-1-7-A-4
#教師なし学習 アソシエーション分析

import pandas as pd
import urllib.request as req

import cv2
import matplotlib.pyplot as plt

%matplotlib inline

#githubからファイルをDownloadできない場合は以下を実行
#url = "http://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx"
#req.urlretrieve(url, "Online_Retail.xlsx")
#trans = pd.read_excel('Online_Retail.xlsx', sheet_name='Online Retail')
#trans.to_csv("./Online_Retail.csv")

#購買データの読み込み
trans = pd.read_csv('Online_Retail.csv')

#####前処理#####
#キャンセルデータと不明なデータを除くための処理をする

# InoivceNoの先頭1文字をcancel_flgとして追加
trans['cancel_flg'] = trans.InvoiceNo.map(lambda x:str(x)[0])

# cancel_flgでグルーピングして集計
trans.groupby('cancel_flg').size()

#有効なデータに上書きする
trans = trans[(trans.cancel_flg == '5') & (trans.CustomerID.notnull())]
################

#対象の商品名を調べる
display(trans[trans['StockCode'] == '85123A'].head(1))
display(trans[trans['StockCode'] == '47566'].head(1))

#画像を持ってくる
url = "https://giftsatpinkparrot.com/wp-content/uploads/2013/02/AX182.jpg"
req.urlretrieve(url, "HEART.jpg")

#画像の指定
image = "HEART.jpg"
img_r = cv2.imread(image)

#画像を表示
plt.axis("off")
plt.imshow(img_r)
plt.title("85123A : WHITE HANGING HEART T-LIGHT HOLDER  ")
plt.show()

#画像を持ってくる
url = "https://previews.123rf.com/images/tribalium123/tribalium1231210/tribalium123121000184/15870997-party-flags-party-pennant-bunting-bunting-flags.jpg"
req.urlretrieve(url, "FLAG.jpg")

#画像の指定
image = "FLAG.jpg"
img_f = cv2.imread(image)

#画像を表示
plt.axis("off")
plt.imshow(img_f)
plt.title("47566 : PARTY BUNTING ")
plt.show()

#考察
print("イギリスのバレンタインデーではキャンドルを灯しながら祝うことが多いので")
print("パーティーグッツとして併売されることが多いと思われる")
