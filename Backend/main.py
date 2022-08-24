import GameLogic
from GameLogic import *
from Ships import dict_indicator_pos, Ship


def start_field():
    field_size = 10
    clean_field = [['~'] * field_size for _ in range(field_size)]
    return clean_field


def get_field_condition():
    global field_condition
    return field_condition


class GameFieldCondition:
    def __init__(self, local_ships_dict=ships_dict):
        self.base_field = None
        self.field_with_ships = None
        self.start_field()
        self.all_ships = []
        self.add_ships(local_ships_dict, dict_indicator_pos)

    def start_field(self):
        field_size = 10
        self.base_field = [['~'] * field_size for _ in range(field_size)]

    def add_ships(self, json_ship_dict, indicator_pos_dict):
        self.field_with_ships = [line.copy() for line in self.base_field]

        for ship in json_ship_dict["layout"]:
            indicator_pos = indicator_pos_dict[ship['ship']]
            ship_instance = Ship(ship['positions'], ship['ship'], indicator_pos)
            self.all_ships.append(ship_instance)

            for x, y in ship_instance.positions:
                self.field_with_ships[x][y] = ship_instance

    def note_shoot(self, shoot: list):
        x, y = shoot
        if isinstance(self.field_with_ships[x][y], Ship):
            self.base_field[x][y] = '*'
            self.field_with_ships[x][y].hit_at_ship(shoot)
        else:
            self.base_field[x][y] = 'x'

    def show_field(self, with_ships=False):
        if with_ships:
            field = self.field_with_ships
        else:
            field = self.base_field
        for y in range(len(field)):
            for x in range(len(field[y])):
                print(field[y][x], end=' ')
            print()

    def is_hited_ship(self, shot):
        self.note_shoot(shot)
        return isinstance(self.field_with_ships[shot[0]][shot[1]], Ship)

    def count_dead_ships(self):
        counter = 0
        for ship in self.all_ships:
            if ship.ship_dead():
                counter += 1
        return counter


    def is_name_ship(self, shot):
        name = "submarine"  # Хардкод для теста. Нужно брать текущее имя корабля.
        return name

    def is_hits_at_ships(self, shot):
        hits = 3  # Хардкод для теста. Нужно брать текущие данные корабля.
        return hits



if __name__ == '__main__':

    field_condition = GameFieldCondition()

    while stop_game() is False:
        shot = input('Введите координаты в формате XY: ')

        GameLogic.shooting(shot)

        field_condition.note_shoot(shot)
        field_condition.show_field()

    else:
        print("Game Over")
