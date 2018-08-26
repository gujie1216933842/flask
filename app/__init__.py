'''
作用:可以让python文件变成一个包
     初始化代码

'''
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    return app

'''蓝图要注册在app中'''
def register_buleprint():
