'''运行一个最简单的web程序'''
from flask import Flask ,make_response

app = Flask(__name__)
app.config.from_object('config')


@app.route('/hello')
def hello():
    return 'hello flask'


def hello1():
    return 'hello flask1'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=5000)
