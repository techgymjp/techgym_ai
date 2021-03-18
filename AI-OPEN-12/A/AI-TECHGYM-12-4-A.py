#techgym-12-4-A

from flask import Flask

fl_main = Flask(__name__)

@fl_main.route('/')
def index():
    return 'Hello World'

# メイン関数
if __name__ == '__main__':
    fl_main.run()
