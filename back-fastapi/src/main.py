from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from books.router import router as books_router
from users.router import router as users_router
from collection.router import router as collection_router
from database import database, create_db_and_tables


app = FastAPI(title='ReadShare')

app.include_router(books_router)
app.include_router(users_router)
app.include_router(collection_router)

origins = [
    'http://localhost:8080',
    'http://localhost:5173'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'OPTIONS', 'DELETE', 'PATCH', 'PUT'],
    allow_headers=['Authorization', 'Access-Contol-Allow-Headers', 'Access-Control-Allow-Origin', 'Access-Control-Allow-Methods']
)


@app.on_event("startup")
async def startup():
    await create_db_and_tables()
    await database.connect()
    

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)
