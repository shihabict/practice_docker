from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Server Works!'


@app.route('/hi')
def say_hello():
    return 'Hello from Server'


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)  # default port is 5000
