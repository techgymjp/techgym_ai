from flask import Flask
from fluent import sender

app    = Flask(__name__)
logger = sender.FluentSender('test_app')

@app.route('/')
def hello():
  # ここにfluentdとの連携を記述
  return 'Hello, World!'
