#techgym-12-8-A

# インポート
from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User

fl_main  = Flask(__name__)

# DBとの接続
engine = create_engine('sqlite:///myDB.db')
session = sessionmaker(bind=engine)()

@fl_main.route('/', methods=['GET'])
def index():




@fl_main.route('/register', methods=['POST'])
def register():




@fl_main.route('/database', methods=['GET'])
def database():




# メイン関数
if __name__ == '__main__':
    fl_main.run(debug=True)
