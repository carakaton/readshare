from sqlalchemy import Column, Integer, String

from database import Base


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String, nullable=True)
    cover_url = Column(String, nullable=True)
