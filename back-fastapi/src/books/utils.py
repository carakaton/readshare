from bs4 import BeautifulSoup
from .schemas import FoundBook, FoundBooks, Book
from config import BOOK_FIND_URL
import requests


def get_books_basic_info(query: str, offset: int = 0) -> FoundBooks:
    """ Ищет книги на сайте из файла конфигурации """

    books_info = []

    page = '' if not offset else f'~{offset + 1}'
    response = requests.get(f'{BOOK_FIND_URL}/{query}/{page}')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, features='html.parser')

    books = soup.find_all('div', class_='object-info')
    for book in books or []:

        raw_title = book.find('a', class_='title')
        raw_author = book.find('a', class_='description')

        books_info.append(
            FoundBook(
                livelib_id=raw_title['href'].split('/')[-1].split('-')[0],
                title=raw_title.text, 
                author=raw_author.text if raw_author else None
            )
         )

    return FoundBooks(
        count=len(books_info),
        books=books_info or None
    )


def get_full_book(livelib_id: int) -> Book:
    ...
