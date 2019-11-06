#AI-TECHGYM-1-7-A-3
#教師なし学習 アソシエーション分析

import pandas as pd
import urllib.request as req

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

#すべてのInvoiceNoをtrans_allとして抽出
trans_ALL = set(trans.InvoiceNo) 

#商品85123Aを購入
trans_X = set(trans[trans['StockCode']=='85123A'].InvoiceNo)

#商品47566を購入したデータ
trans_Y = set(trans[trans['StockCode']=='47566'].InvoiceNo)

#商品85123Aかつ商品47566を購入したデータをtrans_XYとする
trans_XY = trans_X & trans_Y

#信頼度
C = len(trans_XY)/len(trans_X)
print('信頼度:{:.3f}'.format(C))

#支持度
S_XY = len(trans_XY)/len(trans_ALL)
print('支持度:{:.3f}'.format(S_XY))

#全体のバスケットに占める商品Yの割合を計算
S_Y = len(trans_Y) / len(trans_ALL)

# リフト値を計算
LIFT = C / S_Y
print('lift値:{:.3f}'.format(LIFT))
