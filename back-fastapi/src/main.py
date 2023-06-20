from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from books.router import router as books_router
from database import database


app = FastAPI(title='ReadShare')

app.include_router(books_router)

origins = [
    'http://localhost:8080',
    'http://localhost:8000',
    'http://localhost:5173',
    'http://localhost'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'OPTIONS', 'DELETE', 'PATCH', 'PUT'],
    allow_headers=['Content-Type', 'Set-Cookie', 'Authorization', 
                   'Access-Contol-Allow-Headers', 'Access-Control-Allow-Origin', 'Access-Control-Allow-Methods']
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)
