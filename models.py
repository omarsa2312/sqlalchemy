from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base


db_url = "sqlite:///database.db"
engine = create_engine(db_url) # engine is used to connect to db and execute sql queries

Base = declarative_base() # declarative base is used to create models


# Generally a class represents a table in database
# class name is singular, table name is plural
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    age = Column(Integer)


Base.metadata.create_all(engine) # creates the database
