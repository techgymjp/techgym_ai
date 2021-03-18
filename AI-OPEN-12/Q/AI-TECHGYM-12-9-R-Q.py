#techgym-12-9-R-Q

# インポート
from sklearn.datasets import load_breast_cancer
import requests

#データの読み込み
breast_cancer = load_breast_cancer()


#データの確認
print(x)
type(x)

#渡すデータの形式


#リクエスト
url = 'http://127.0.0.1:5000/'


# 200 であればデータの送受信が成功
print("res",res)

# 結果を JSON 形式で取得

print(result)

# 推論結果を表示
print("Result",result['y'])
