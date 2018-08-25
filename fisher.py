'''运行一个最简单的web程序'''
from flask import Flask

app = Flask(__name__)

'''如果路由配置成  /hello/会重定向/hello'''


@app.route('/hello')
def hello():
    return 'hello flask'


if __name__ == '__main__':
    '''加入debug模式'''
    app.run(debug=True)
