from dotenv import load_dotenv
import os


load_dotenv()

DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')

BOOK_FIND_URL = 'https://www.livelib.ru/find/books'
BOOK_INFO_URL = 'https://www.livelib.ru/book'
