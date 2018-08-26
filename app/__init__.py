'''
作用:可以让python文件变成一个包
     初始化代码

'''
from flask import Flask
from app.models.book import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_buleprint(app)

    db.init_app(app)
    db.create_all()
    return app


'''蓝图要注册在app中'''


def register_buleprint():
    pass
