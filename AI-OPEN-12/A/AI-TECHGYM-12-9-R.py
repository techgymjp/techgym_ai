#techgym-12-9-R

# インポート
from sklearn.datasets import load_breast_cancer
import requests

#データの読み込み
breast_cancer = load_breast_cancer()
x = breast_cancer['data'][0]

#データの確認
print(x)
type(x)

#渡すデータの形式
data = {'x': x.tolist()}

#リクエスト
url = 'http://127.0.0.1:5000/'
res = requests.post(url, json=data)

# 200 であればデータの送受信が成功
print("res",res)

# 結果を JSON 形式で取得
result = res.json()
print(result)

# 推論結果を表示
print("Result",result['y'])
