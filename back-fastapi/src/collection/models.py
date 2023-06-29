from sqlalchemy import Column, Integer, ForeignKey

from database import Base
from users.models import User
from books.models import Book


class BookUser(Base):
    __tablename__ = "book_user"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    book_id = Column(Integer, ForeignKey(Book.id))
