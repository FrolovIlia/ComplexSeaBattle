import GameLogic
from GameLogic import *
from Ships import *


def start_field():
    field_size = 10
    clean_field = [['~'] * field_size for _ in range(field_size)]
    return clean_field


def check_shoot(shoot: str) -> list[int]:
    if len(shoot) == 2 and shoot.isnumeric():
        print('Данные верны')
        return [int(shoot[0]), int(shoot[1])]
    else:
        trying = input('Пожалуйста, введите корректные координаты в формате XY: ')
        return check_shoot(trying)


def get_field_condition():
    global field_condition
    return field_condition


class GameFieldCondition:
    sample = None

    def __init__(self):
        self.base_field = None
        self.field_with_ships = None
        if GameFieldCondition.sample:
            self = GameFieldCondition.sample
        else:
            self.start_field()
            self.add_ships(ships_dict, dict_indicator_pos)
            GameFieldCondition.sample = self

    def start_field(self):
        field_size = 10
        self.base_field = [['~'] * field_size for _ in range(field_size)]

    def add_ships(self, json_ship_dict, indicator_pos_dict):
        self.field_with_ships = [line.copy() for line in self.base_field]

        for ship in json_ship_dict["layout"]:
            indicator_pos = indicator_pos_dict[ship['ship']]
            ship_instance = Ship(ship['positions'], ship['ship'], indicator_pos)

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


if __name__ == '__main__':

    field_condition = GameFieldCondition()

    print('Добро пожаловать в игру "Морской Бой!"')
    print('Выберите координаты от 0 до 9 по X и Y')
    print()

    while stop_game() is False:
        shot = input('Введите координаты в формате XY: ')
        shot = check_shoot(shot)

        GameLogic.shooting(shot)

        field_condition.note_shoot(shot)
        # field_condition.show_field(with_ships=True)
        field_condition.show_field()

    else:
        print("Game Over")
