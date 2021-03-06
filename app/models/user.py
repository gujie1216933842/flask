from sqlalchemy import Column, Integer, String, Float, Boolean
from flask_sqlalchemy import SQLAlchemy
from app.models.base import Base
from werkzeug.security import generate_password_hash


class User(Base):
    # __tablename__ = 'user1'  # 指定表名

    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=False)
    _password = Column('password', String(128))
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    recieve_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)
