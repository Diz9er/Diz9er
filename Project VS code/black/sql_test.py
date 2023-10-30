from sqlalchemy import Column, Integer, String, func
from DataBase import engine, Base

class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key = True)
    Login = Column(String(30), nullable=False)
    Password = Column(String(30), nullable=False)

Base.metadata.create_all(engine)
