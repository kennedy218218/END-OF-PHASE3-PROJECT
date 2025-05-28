from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('sqlite:///books.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

from .author import Author
from .book import Book

Base.metadata.create_all(engine)