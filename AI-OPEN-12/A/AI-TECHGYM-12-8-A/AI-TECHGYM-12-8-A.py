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
    return render_template('index.html')

@fl_main.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    age = int(request.form['age'])
    new_user = User(name=name, age=age)
    session.add(new_user)
    session.commit()
    return redirect(url_for('database'))

@fl_main.route('/database', methods=['GET'])
def database():
    users = session.query(User).all()
    return render_template('database.html', users=users)

# メイン関数
if __name__ == '__main__':
    fl_main.run(debug=True)
