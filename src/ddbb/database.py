"""
MySQL Database file configuration
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.configuration import configuration


__all__ = ['create_db_tables', 'SessionLocal', 'Base', 'engine']


def create_db_tables(base, engine) -> None:
    base.metadata.create_all(bind=engine)


SQLALCHEMY_DATABASE_DATABASE = 'chat_app'
SQLALCHEMY_DATABASE_USER = configuration.get_database()['user']
SQLALCHEMY_DATABASE_PASSWORD = configuration.get_database()['password']
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://{user}:{password}@{url}/{database}'.format(
                                user=SQLALCHEMY_DATABASE_USER, 
                                password=SQLALCHEMY_DATABASE_PASSWORD, 
                                url=configuration.get_database()["url"], 
                                database=SQLALCHEMY_DATABASE_DATABASE
                            )
engine = create_engine(url=SQLALCHEMY_DATABASE_URL)
# class for database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# class for inherit models
Base = declarative_base()
