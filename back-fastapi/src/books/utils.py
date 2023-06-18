from bs4 import BeautifulSoup
from .schemas import FoundBook, FoundBooks, FullBook
from config import BOOK_FIND_URL, BOOK_INFO_URL
import requests


def get_books_basic_info(query: str, offset: int = 0) -> FoundBooks:
    """ Ищет книги на сайте из файла конфигурации """

    page = '' if not offset else f'~{offset + 1}'
    response = requests.get(f'{BOOK_FIND_URL}/{query}/{page}')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, features='html.parser')

    found_books = FoundBooks(count=0, books=[])
    books = soup.find_all('div', class_='object-info')
    for book in books or []:

        raw_title = book.find('a', class_='title')
        raw_author = book.find('a', class_='description')

        found_books.books.append(FoundBook(
                livelib_id=raw_title['href'].split('/')[-1].split('-')[0],
                title=raw_title.text, 
                author=raw_author.text if raw_author else None))

    found_books.count = len(found_books.books)
    return found_books


def get_full_book(livelib_id: int) -> FullBook:
    
    response = requests.get(f'{BOOK_INFO_URL}/{livelib_id}')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, features='html.parser')

    raw_author = soup.find('a', class_='bc-author__link')

    return FullBook(
        id=livelib_id,
        title=soup.find('h1', class_='bc__book-title').text,
        author=raw_author.text if raw_author else None,
        cover_url=soup.find('img', class_='bc-header__bg').get('src', None)
    )
