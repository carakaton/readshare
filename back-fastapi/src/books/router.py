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

BOOKS = {
  "count": 18,
  "books": [
    {
      "livelib_id": 1001257165,
      "title": "Дракон",
      "author": "Евгений Шварц"
    },
    {
      "livelib_id": 1000383103,
      "title": "Дракон. Повести. Пьесы. Сценарии (сборник)",
      "author": "Евгений Шварц"
    },
    {
      "livelib_id": 1000493344,
      "title": "Тень. Дракон. Обыкновенное чудо (сборник)",
      "author": "Евгений Шварц"
    },
    {
      "livelib_id": 1000455964,
      "title": "Обыкновенное чудо. Голый король. Тень. Дракон. Снежная королева. Два клена. Золушка (сборник)",
      "author": "Евгений Шварц"
    },
    {
      "livelib_id": 1000529123,
      "title": "Дракон. Пьесы (сборник)",
      "author": "Евгений Шварц"
    },
    {
      "livelib_id": 1000234105,
      "title": "Голый король. Снежная королева. Тень. Дракон. Два клена. Обыкновенное чудо. Золушка. Дон-Кихот (сборник)",
      "author": "Евгений Шварц"
    },
    {
      "livelib_id": 1001456315,
      "title": "Лекция «Eвгений Шварц и тайна дракона»",
      "author": "Дмитрий Быков"
    },
    {
      "livelib_id": 1001833566,
      "title": "Лекция «Евгений Шварц и тайна дракона. Часть 3-я»",
      "author": "Дмитрий Быков"
    },
    {
      "livelib_id": 1000580634,
      "title": "Обыкновенное чудо. Голый король. Тень. Дракон",
      "author": "Евгений Шварц"
    },
    {
      "livelib_id": 1000451207,
      "title": "Пьесы: Клад. Красная шапочка. Снежная королева. Тень. Дракон. Два клена. Обыкновенное чудо. Повесть о молодых супругах. Золушка. Дон Кихот (сборник)",
      "author": "Евгений Шварц"
    },
    {
      "livelib_id": 1002105656,
      "title": "Обыкновенное чудо. Дракон (сборник)",
      "author": "Шварц Евгений Львович"
    },
    {
      "livelib_id": 1000222533,
      "title": "Голый король. Снежная королева. Тень. Дракон. Пьесы 1934 - 1943 (сборник)",
      "author": "Евгений Шварц"
    },
    {
      "livelib_id": 1001438270,
      "title": "Лекция «Евгений Шварц и тайна дракона». лекция 2.",
      "author": "Дмитрий Быков"
    },
    {
      "livelib_id": 1007394436,
      "title": "Дракон",
      "author": "Евгений Шварц"
    },
    {
      "livelib_id": 1002889767,
      "title": "Дракон (сборник)",
      "author": "Евгений Шварц"
    },
    {
      "livelib_id": 1001831976,
      "title": "Лекция «Евгений Шварц и тайна дракона. Часть 2-я»",
      "author": "Дмитрий Быков"
    },
    {
      "livelib_id": 1003035665,
      "title": "Дракон над Москвой. Сборник рассказов",
      "author": "Евгений Шварц"
    },
    {
      "livelib_id": 1005712495,
      "title": "Снежная королева. Дракон. Пьесы-сказки.",
      "author": "Евгений Шварц"
    }
  ]
}


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
    return BOOKS


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

    # book = await to_thread(get_full_book, livelib_id)

    book, = filter(lambda book: book if book['livelib_id'] == livelib_id else None, BOOKS['books'])
    book = FullBook(
        id=book['livelib_id'],
        title = book['title'],
        author = book['author'],
        cover_url = None
    )

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