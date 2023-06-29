from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy import insert

from database import database
from .models import User
from .core import get_current_user, create_access_token, encode_password, get_user_if_valid
from .schemas import Token, UserRead, UserCreate, LoginData


router = APIRouter(
    prefix='/user',
    tags=['User']
)

@router.post('/register')
async def register(user: UserCreate):
    """ Регистрация нового пользователя """

    user_exists = await User.get_by_username(user.username)
    if user_exists:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User already exists')
    
    query = insert(User).values(
        username=user.username,
        hashed_password=encode_password(user.password)
    )
    await database.execute(query)
    
    return Response(status_code=status.HTTP_201_CREATED)


@router.post('/login')
async def login(data: LoginData) -> Token:
    """ Вход с получением токена """

    user = await get_user_if_valid(data.username, data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Incorect username or password',
                            headers={'WWW-Authenticate': 'Bearer'})
    
    return create_access_token(data=user.username) 
    

@router.get('/me')
async def read_users_me(user: User = Depends(get_current_user)) -> UserRead:
    """ Информация о текущем пользователе """

    return UserRead(username=user.username)
