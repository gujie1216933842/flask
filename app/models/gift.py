from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, SmallInteger
from sqlalchemy.orm import relationships
from app.models.base import Base


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationships('User')
    uid = Column(Integer, ForeignKey('user.id'))
    launched = Column(Boolean, nullable=False)
    isbn = Column(String(15), nullable=False)
    # book = relationships('Book')
    # bid = Column(Integer, ForeignKey('book.id'))
    status = Column(SmallInteger, default=0)
