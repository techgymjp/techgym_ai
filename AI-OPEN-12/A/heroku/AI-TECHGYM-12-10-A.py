#techgym-12-10-A

from flask import Flask, request, jsonify
import joblib

fl_main = Flask(__name__)

# 訓練済みモデルの読み込み
clf = joblib.load('brest_cancer.pkl')

@fl_main.route('/', methods=['POST'])
def predict():
    x = request.json['x']
    y = clf.predict([x])[0]
    ret = {'y': int(y)}
    return jsonify(ret)

# メイン関数
if __name__ == '__main__':
    fl_main.run(debug=True)
