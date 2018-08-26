'''
作用:可以让python文件变成一个包
     初始化代码

'''
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_buleprint(app)
    return app


'''蓝图要注册在app中'''


def register_buleprint():
    pass
