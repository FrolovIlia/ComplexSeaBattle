from pydantic import BaseModel
from typing import Literal


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
    ship_hits: int | None
    ship_name: str | None
    total_count: int | None
