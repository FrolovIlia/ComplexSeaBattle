from typing import Union, Optional

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import FileResponse


class Item(BaseModel):
    game_num: Optional[int]


class GameObject(BaseModel):
    shipType: str
    item: Item

class JustKidding(BaseModel):
    go: GameObject
    status: str

app = FastAPI()
game10 = 0

@app.get("/")
def get_root():
    return FileResponse("index.html")


@app.post("/")
def post_root(item: Item = Item(name="Magic")):
    return {"message": f'Hello, {item.name}'}

@app.get("/start_game/{value}")
def start_game(value: Optional[int]):
    global game10
    game10 = 0
    if value:
        game10 = value

    print("Играм началась!")
    return {"status": "Ok", "game_num": game10}

@app.post("/start_game")
def start_game(item: Item):
    global game10
    game10 = 0
    print(f"item: {item}")
    if hasattr(item, "game_num"):
        print("hasattr")
        game10 = item.game_num

    print("Играм началась!")
    return {"status": "Ok", "game_num": game10}


@app.get("/increase")
def increase_num():
    global game10
    game10 = game10 + 1
    print("Увеличиваем на 1")
    return {"status": "Ok", "game_num": game10}




@app.get("/decrease")
def decrease_num():
    global game10
    game10 = game10 - 1
    print("Уменьшаем на 1")
    return {"status": "Ok", "game_num": game10}

