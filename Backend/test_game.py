import pytest

from GameLogic import GameFieldCondition

data = {
    "shipTypes": {
        "carrier": {"size": 5, "count": 1},
        "battleship": {"size": 4, "count": 1},
        "cruiser": {"size": 3, "count": 1},
        "submarine": {"size": 3, "count": 1},
        "destroyer": {"size": 2, "count": 1}
    },
    "layout": [
        {"ship": "carrier", "positions": [[2, 9], [3, 9], [4, 9], [5, 9], [6, 9]]},
        {"ship": "battleship", "positions": [[5, 2], [5, 3], [5, 4], [5, 5]]},
        {"ship": "cruiser", "positions": [[8, 1], [8, 2], [8, 3]]},
        {"ship": "submarine", "positions": [[3, 0], [3, 1], [3, 2]]},
        {"ship": "destroyer", "positions": [[0, 0], [1, 0]]}
    ]
}

shot = [3, 4]


@pytest.mark.parametrize("coordinates,ship_name", [([9, 2], "carrier"),
                                                   ([5, 5], "battleship"),
                                                   ([1, 8], "cruiser"),
                                                   ([1, 3], "submarine"),
                                                   ([0, 1], "destroyer")])
def test_name_ship(coordinates, ship_name):
    gl = GameFieldCondition(data)
    assert gl.is_name_ship(coordinates) == ship_name


def test_is_hits_at_ships():
    hs = GameFieldCondition(data)
    assert hs.is_hits_at_ships(shot) is None

def test_count_dead_ships():
    dh = GameFieldCondition(data)
    assert dh.count_dead_ships() == 0