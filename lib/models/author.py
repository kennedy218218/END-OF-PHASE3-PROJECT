from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    books = relationship("Book", back_populates="author")

    def __repr__(self):
        return f"<Author(name='{self.name}')>"