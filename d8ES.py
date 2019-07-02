from flask import Flask
from fluent import sender


app    = Flask(__name__)
logger = sender.FluentSender('test_app')

@app.route('/')
def hello():
  logger.emit('access', {'user': 'userA', 'to': 'top page'})
  return 'Hello, World!'
