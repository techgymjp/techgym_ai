#techgym-12-5-Q

from flask import Flask, render_template

fl_main  = Flask(__name__)

@fl_main .route('/')
def index():
    name = 'Tech Gym'


# main function
if __name__ == '__main__':

