'''运行一个最简单的web程序'''
from flask import Flask

app = Flask(__name__)

'''如果路由配置成  /hello/会重定向/hello'''


@app.route('/hello')
def hello():
    return 'hello flask'


def hello1():
    return 'hello flask1'


if __name__ == '__main__':
    '''另一种路由注册的方式'''
    app.add_url_rule('/hello1', view_func=hello1)
    '''加入debug模式'''
    app.run(debug=True)
