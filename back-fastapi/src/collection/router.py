from fastapi import APIRouter, Depends, status, Response
from sqlalchemy import insert, select, delete

from database import database
from users.models import User
from users.core import get_current_user
from books.models import Book
from books.schemas import FullBooks, FullBook
from .models import BookUser


router = APIRouter(
    prefix='/collection',
    tags=['Collection']
)


@router.get('/')
async def get_books(user: User = Depends(get_current_user)) -> FullBooks:
    """ Книги текущего пользователя """
    
    query = select(BookUser).join(Book).where(BookUser.user_id==user.id)
    books= await database.fetch_all(query)
    
    full_books = [FullBook(
        id = book.id,
        title = book.title,
        author = book.author,
        cover_url = book.cover_url
    ) for book in books or []] 

    return FullBooks(
        count = len(full_books),
        books = full_books
    )


@router.post('/')
async def add_book(book_id: int, user: User = Depends(get_current_user)):
    """ Добавить книгу текущему пользователю """

    query = insert(BookUser).values(book_id=book_id, user_id=user.id)
    await database.execute(query)
    
    return Response(status_code=status.HTTP_201_CREATED)



@router.delete('/')
async def remove_book(book_id: int, user: User = Depends(get_current_user)):
    """ Все книги текущего пользователя """
    
    query = delete(BookUser).where(book_id=book_id, user_id=user.id)
    await database.execute(query)
    
    return Response(status_code=status.HTTP_200_OK)
from fastapi import APIRouter, Depends, status, Response
from sqlalchemy import insert, select, delete

from database import database
from users.models import User
from users.core import get_current_user
from books.models import Book
from books.schemas import FullBooks, FullBook
from .models import BookUser


router = APIRouter(
    prefix='/collection',
    tags=['Collection']
)


@router.get('/')
async def get_books(user: User = Depends(get_current_user)) -> FullBooks:
    """ Книги текущего пользователя """
    
    query = select(BookUser).join(Book).where(BookUser.user_id==user.id)
    books= await database.fetch_all(query)
    
    full_books = [FullBook(
        id = book.id,
        title = book.title,
        author = book.author,
        cover_url = book.cover_url
    ) for book in books or []] 

    return FullBooks(
        count = len(full_books),
        books = full_books
    )


@router.post('/')
async def add_book(book_id: int, user: User = Depends(get_current_user)):
    """ Добавить книгу текущему пользователю """

    query = insert(BookUser).values(book_id=book_id, user_id=user.id)
    await database.execute(query)
    
    return Response(status_code=status.HTTP_201_CREATED)



@router.delete('/')
async def remove_book(book_id: int, user: User = Depends(get_current_user)):
    """ Все книги текущего пользователя """
    
    query = delete(BookUser).where(book_id=book_id, user_id=user.id)
    await database.execute(query)
    
    return Response(status_code=status.HTTP_200_OK)
