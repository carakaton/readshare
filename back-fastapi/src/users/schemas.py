from pydantic import BaseModel


class Token(BaseModel):

    access_token: str
    cookie_name: str
    expire_time: int


class LoginData(BaseModel):

    username: str
    password: str


class UserCreate(BaseModel):

    username: str
    password: str


class UserRead(BaseModel):

    username: str
