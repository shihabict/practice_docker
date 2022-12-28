import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Server Works!'


@app.route('/hi')
def say_hello():
    return 'Hello from Server'

@app.route('/folders')
def show_number_of_folders():
    return f"{len(os.listdir('/projects'))} folder exist in projects dir"


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)  # default port is 5000
