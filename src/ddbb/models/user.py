"""
User database model
"""
from typing import Type
from sqlalchemy import Column, Integer, String
from src.ddbb.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(20), unique=True, index=True)
    email = Column(String(30), unique=True, index=True)
    password = Column(String(64))
