from sqlalchemy import Column, Integer, String, Float, Boolean
from app.models.base import db


class Gift(db.Model):
    id = Column(Integer, primary_key=True)
    nickname = Column(Boolean, nullable=False)
