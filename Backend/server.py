from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles


class Item(BaseModel):
    game_num: Optional[int]


class GameObject(BaseModel):
    shipType: str
    item: Item


class JustKidding(BaseModel):
    go: GameObject
    status: str


# -----------------------------------------

class ShipRange(BaseModel):
    size: int
    count: int


class ShipTypes(BaseModel):
    ship_name: str
    ship_data: ShipRange


class Layouts(BaseModel):
    ship: str
    positions: list[int]


class ShipsData(BaseModel):
    shipTypes: ShipTypes
    layout: Layouts

class ShotCoordinates(BaseModel):
    shot: list[int]


app = FastAPI()
game10 = 0

app.mount("/static", StaticFiles(directory="Frontend", html=True), name="static")


@app.get("/")
def get_root():
    return FileResponse("Frontend/index.html")

#
# @app.post("/")
# def post_root(item: Item = Item(name="Magic")):
#     return {"message": f'Hello, {item.name}'}


@app.get("/start_game/{value}")
def start_game(value: Optional[int]):
    global game10
    game10 = 0
    if value:
        game10 = value

    print("Играм началась!")
    return {"status": "Ok", "game_num": game10}


@app.post("/start_game")
def start_game(data: ShipsData):
    print(f"Приняли JSON: {data}")
    if hasattr(data, "game_num"):
        print("hasattr")

    print("Играм началась!")
    return {"status": "Ok"}


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


@app.get("/test")
def test_frase():
    return {"code frase": "hello world"}