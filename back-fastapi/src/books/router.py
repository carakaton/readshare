from asyncio import to_thread
from fastapi import APIRouter
from typing import Optional
from sqlalchemy import insert, select, delete
from asyncpg.exceptions import UniqueViolationError

from database import database
from .models import Book
from .schemas import FullBook, FullBooks, FoundBooks
from .utils import get_books_basic_info, get_full_book


router = APIRouter(
    prefix='/book',
    tags=['Books']
)


@router.get('/all')
async def get_all_books():
    """ Получает все книги """
    
    query = select(Book)
    books: list[Book] = await database.fetch_all(query)
    
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


@router.get('/find/{search_query}')
async def find_books(search_query: str, offset: int = 0) -> FoundBooks:
    """ Поиск книг """

    found_books = await to_thread(get_books_basic_info, search_query, offset)
    return found_books


@router.get('/{id}')
async def get_book(id: int) -> Optional[FullBook]:
    """ Получение книги """

    query = select(Book).where(Book.id == id)
    book: Book = await database.fetch_one(query)
    return FullBook(
        id = book.id,
        title = book.title,
        author = book.author,
        cover_url = book.cover_url
    ) if book else None


@router.post('/')
async def add_book(livelib_id: int) -> dict:
    """ Добавление книги """

    book = await to_thread(get_full_book, livelib_id)
    query = insert(Book).values(**book.dict())
    try:
        await database.execute(query)
        status = 'Book added'
    except UniqueViolationError:
        status = 'Book already exists'
    return {'status': status}


@router.delete('/{id}')
async def delete_book(id: int) -> dict:
    """ Удаление книги """

    query = delete(Book).where(Book.id == id)
    result = await database.execute(query)
    return {'status': 'Book deleted (probably, lol)'}