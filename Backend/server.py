from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles
from typing import Literal

from main import GameFieldCondition

field_condition: GameFieldCondition | None = None


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
    is_hited_ship: bool
    dead_ships: int
    # Данные - корабль - количество подбитий
    ship_hits: int | None
    ship_name: str | None

    # Данные - общее количество выстрелов (для вывода финальной фразы со статистикой)
    total_count: int | None


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


@app.post("/shot_coordinate")
def shot_data(coordinates: ShotCoordinates):
    print("Координаты пришли", coordinates.shot)
    global field_condition

    value = field_condition.is_hited_ship(coordinates.shot)
    ship_name = field_condition.is_name_ship(coordinates.shot)
    ship_hits = field_condition.is_hits_at_ships(coordinates.shot)
    dead_ships = field_condition.count_dead_ships()

    return ShotResponse(is_hited_ship=value,
                        dead_ships=dead_ships,
                        ship_name=ship_name,
                        ship_hits=ship_hits)  # Добавить счётчик общего количества выстрелов
