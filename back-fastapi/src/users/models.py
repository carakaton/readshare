from sqlalchemy import Column, Integer, String, select

from database import Base, database


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    hashed_password = Column(String)

    @classmethod
    async def get_by_username(cls, username: str):
        query = select(cls).where(cls.username==username)
        return await database.fetch_one(query)
