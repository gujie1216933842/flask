from sqlalchemy import Column, Integer, String, SmallInteger
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True  # 作用: sqlalchemy不会去创建base表

    status = Column(SmallInteger, default=1)
