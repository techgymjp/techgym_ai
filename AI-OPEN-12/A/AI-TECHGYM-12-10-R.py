#techgym-12-10-R

#インポート
import requests
from sklearn.datasets import load_breast_cancer

# 送信するデータの準備
breast_cancer = load_breast_cancer()
x = breast_cancer['data'][0]
data = {'x': x.tolist()}

#リクエスト:各自のURLに変更する
url = 'https://techgym-test-proj.herokuapp.com/'
res = requests.post(url, json=data)

# 200 であればデータの送受信が成功
print("res",res)

# 結果を JSON 形式で取得
result = res.json()
print(result)

# 推論結果を表示
print("Result",result['y'])
