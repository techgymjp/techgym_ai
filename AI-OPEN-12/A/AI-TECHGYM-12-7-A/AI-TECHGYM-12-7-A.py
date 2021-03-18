#techgym-12-7-A

# インポート
from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User

fl_main = Flask(__name__)

# DBとの接続
engine = create_engine('sqlite:///test.db')
session = sessionmaker(bind=engine)()

@fl_main.route('/')
def index():
    users = session.query(User).all()
    return render_template('index.html', users=users)

# Main
if __name__ == '__main__':
    fl_main.run(debug=True)
