'''
作用:可以让python文件变成一个包
     肩负着包里面初始化代码的工作

'''

from flask import Flask
from app.models.book import db


def register_web_blueprint(app):
    from app.web import web
    app.register_blueprint(web)


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_web_blueprint(app)

    # db.init_app(app)
    # db.create_all()
    return app


'''蓝图要注册在app中'''


