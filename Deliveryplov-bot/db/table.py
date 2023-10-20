from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, MetaData, DateTime, ForeignKey, Enum
import datetime
import enum
Base = declarative_base()


class UsersTable(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    telegram_id = Column(Integer, unique=True)
    created_at = Column( DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now,
           onupdate=datetime.datetime.now)


class CategoriesTable(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    created_at = Column( DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now,
           onupdate=datetime.datetime.now)

class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    price = Column(Integer)
    category = Column(Integer, ForeignKey('categories.id'))
    photo = Column(String, nullable=True)
    created_at = Column( DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now,
           onupdate=datetime.datetime.now)
    





# class WordsTable(Base):
#     __tablename__ = 'words'

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     word = Column(String)
#     word_translation = Column(String)
#     photo = Column(String, nullable=True)
#     audio = Column(String, nullable=True)
#     created_at = Column(DateTime, default=datetime.datetime.now)
#     updated_at = Column(DateTime, default=datetime.datetime.now,
#                         onupdate=datetime.datetime.now)

