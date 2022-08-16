from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles
from typing import Literal

from main import GameFieldCondition
from GameLogic import shooting

field_condition = None


class ShipRange(BaseModel):
    size: int
    count: int


class ShipTypes(BaseModel):
    carrier: ShipRange
    battleship: ShipRange
    cruiser: ShipRange
    submarine: ShipRange
    destroyer: ShipRange


class ShipLayout(BaseModel):
    ship: str
    positions: list[list[int]]


class ShipsData(BaseModel):
    shipTypes: ShipTypes
    layout: list[ShipLayout]


class ShotCoordinates(BaseModel):
    shot: list[int]


class SuccessfulStart(BaseModel):
    message: Literal["Ok"]


class ShotResponse(BaseModel):
    shot_value: bool


app = FastAPI()
game10 = 0

app.mount("/static", StaticFiles(directory="Frontend", html=True), name="static")


@app.get("/")
def get_root():
    return FileResponse("Frontend/index.html")


@app.post("/start_game", response_model=SuccessfulStart)
def start_game(data: ShipsData):
    global field_condition
    print("Стартовая информация успешно принята")
    start_data = data.dict()
    field_condition = GameFieldCondition(start_data)
    return SuccessfulStart(message="Ok")


web_field_condition = GameFieldCondition()


@app.post("/shot_coordinate")
def shot_data(coordinates: ShotCoordinates):
    print("Координаты пришли", coordinates.shot)

    web_field_condition.note_shoot(coordinates.shot)

    return ShotResponse(shot_value=True)  # Здесь должно передаваться булево значение попал/не попал

#
# @app.post("/")
# def post_root(item: Item = Item(name="Magic")):
#     return {"message": f'Hello, {item.name}'}


# @app.get("/start_game/{value}")
# def start_game(value: Optional[int]):
#     global game10
#     game10 = 0
#     if value:
#         game10 = value
#
#     print("Играм началась!")
#     return {"status": "Ok", "game_num": game10}

#

# @app.get("/increase")
# def increase_num():
#     global game10
#     game10 = game10 + 1
#     print("Увеличиваем на 1")
#     return {"status": "Ok", "game_num": game10}
#
#
# @app.get("/decrease")
# def decrease_num():
#     global game10
#     game10 = game10 - 1
#     print("Уменьшаем на 1")
#     return {"status": "Ok", "game_num": game10}
