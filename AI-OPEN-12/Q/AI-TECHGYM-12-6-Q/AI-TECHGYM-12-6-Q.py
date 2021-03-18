#techgym-12-6-Q

# インポート
from flask import Flask, render_template


fl_main = Flask(__name__)

# DBとの接続


@fl_main.route('/')
def hello():


# Main
if __name__ == '__main__':
    fl_main.run(debug=True)
