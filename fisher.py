'''运行一个最简单的web程序'''
from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'hello flask'


if __name__ == '__main__':
    app.run()
