'''web是蓝图文件夹'''
from flask import Blueprint

web = Blueprint('web', __name__)

from app.web import book
from app.web import user