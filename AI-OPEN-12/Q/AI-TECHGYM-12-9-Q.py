#techgym-12-9-Q

from flask import Flask, request, jsonify
import joblib

fl_main = Flask(__name__)

# 訓練済みモデルの読み込み


@fl_main.route('/', methods=['POST'])


# メイン関数
if __name__ == '__main__':
    fl_main.run(debug=True)
