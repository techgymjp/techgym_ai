#techgym-12-5-A

from flask import Flask, render_template

fl_main  = Flask(__name__)

@fl_main .route('/')
def index():
    name = 'Tech Gym'
    return render_template('index.html', name=name)

# main function
if __name__ == '__main__':
    fl_main .run(debug=True)
