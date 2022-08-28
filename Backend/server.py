from fastapi import FastAPI
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

from schemas import *
from GameLogic import GameFieldCondition

field_condition: GameFieldCondition | None = None


app = FastAPI()

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
                        ship_hits=ship_hits)
