from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine
from databases import Database

from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME


DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

Base = declarative_base()

database = Database(DATABASE_URL)


async def create_db_and_tables():
    async with create_async_engine(DATABASE_URL).begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
