from pydantic import BaseModel


class Token(BaseModel):

    access_token: str
    token_type: str


class LoginData(BaseModel):

    username: str
    password: str


class UserCreate(BaseModel):

    username: str
    password: str


class UserRead(BaseModel):

    username: str
