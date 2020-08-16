from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

# HELPFUL CHEAT-SHEET: https://www.pythonsheets.com/notes/python-sqlalchemy.html

# --------------------------------------------------------------------------------
# CONSTANTS
# --------------------------------------------------------------------------------

engine = create_engine('sqlite:///datastore/test.db')
Base = declarative_base()


# --------------------------------------------------------------------------------
# TABLES
# --------------------------------------------------------------------------------

class User(Base):
    __tablename__ = 'user'
    id   = Column(Integer, primary_key=True)
    name  = Column(String, nullable=False)


# --------------------------------------------------------------------------------
# SETUP
# --------------------------------------------------------------------------------

Base.metadata.create_all(bind=engine)
Session = sessionmaker()
Session.configure(bind=engine)
