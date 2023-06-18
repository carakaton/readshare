from asyncio import to_thread
from fastapi import APIRouter

from .schemas import FoundBooks
from .utils import get_books_basic_info, get_full_book


router = APIRouter(
    prefix='/book',
    tags=['Books']
)


@router.get('/find/{search_query}')
async def find(search_query: str, offset: int = 0) -> FoundBooks:
    """ Поиск книг """

    found_books = await to_thread(get_books_basic_info, search_query, offset)
    return found_books
