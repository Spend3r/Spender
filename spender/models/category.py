# encoding: utf-8
from sqlalchemy import Column, Integer, String
from database import Base


class Category(Base):
    """ This is the category table """

    __tablename__ = "categories"

    id = Column(Integer, autoincrement=True, primary_key=True)
    category = Column(String(64))
