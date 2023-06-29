from datetime import datetime, timedelta

from fastapi import Request, HTTPException, status
from jose import JWTError, jwt
from passlib.context import CryptContext

from config import SECRET
from .schemas import Token
from .models import User


_TOKEN_ENCODE_ALGORITHM = 'HS256'

_TOKEN_EXPIRE_MINUTES = 30

_PWD_CONTEXT = CryptContext(schemes=['bcrypt'], deprecated='auto')

_TOKEN_NAME = 'token'


def create_access_token(data: any) -> Token:
    """ Создает новый токен """

    to_encode = {'sub': data}
    expire = datetime.utcnow() + timedelta(minutes=_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET, algorithm=_TOKEN_ENCODE_ALGORITHM)

    return Token(access_token=encoded_jwt, cookie_name=_TOKEN_NAME, expire_time=expire)

    

async def get_user_if_valid(username: str, password: str) -> User:
    """ Подтверждение пользователя """
    
    user = await User.get_by_username(username)
    if user and _PWD_CONTEXT.verify(password, user.hashed_password):
        return user
    

def encode_password(password: str) -> str:
    """ Кодирует пароль """

    return _PWD_CONTEXT.hash(password)


async def get_current_user(request: Request):
    """ Получение текущего пользователя """

    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                            detail='Could not validate credentials', 
                                            headers={'WWW-Authenticate': 'Bearer'})
    
    token = request.cookies.get(_TOKEN_NAME)
    try:
        payload = jwt.decode(token, SECRET, algorithms=[_TOKEN_ENCODE_ALGORITHM])
        data = payload.get('sub')
    except JWTError:
        raise credential_exception
    
    if data is None:
        raise credential_exception
    
    user = await User.get_by_username(data['username'])
    if user is None:
        raise credential_exception
    
    return user
