from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://127.0.0.1:8000/",
    "http://localhost:8000/",
    "http://localhost/",
    "http://localhost:63343/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# post - Создание новых записей
# get - Чтение состояния записей
# put - Обновление записей
# delete - Удаление записи


