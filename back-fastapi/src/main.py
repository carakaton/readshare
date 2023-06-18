from fastapi import FastAPI
import uvicorn

from books.router import router as books_router
from database import database


app = FastAPI(title='ReadShare')
app.include_router(books_router)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
