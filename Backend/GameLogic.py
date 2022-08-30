from Ships import Ship


class GameFieldCondition:
    def __init__(self, local_ships_dict):
        self.base_field = None
        self.field_with_ships = None
        self.start_field()
        self.all_ships = []
        self.add_ships(local_ships_dict)

    def start_field(self):
        field_size = 10
        self.base_field = [['~'] * field_size for _ in range(field_size)]

    def add_ships(self, json_ship_dict):
        self.field_with_ships = [line.copy() for line in self.base_field]

        for ship in json_ship_dict["layout"]:
            ship_instance = Ship(ship['positions'], ship['ship'])
            self.all_ships.append(ship_instance)

            for y, x in ship_instance.positions:
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

    def is_hited_ship(self, shot_pos):
        self.note_shoot(shot_pos)
        return isinstance(self.field_with_ships[shot_pos[0]][shot_pos[1]], Ship)

    def count_dead_ships(self):
        counter = 0
        for ship in self.all_ships:
            if ship.ship_dead():
                counter += 1
        return counter

    def is_name_ship(self, shot_pos):
        current_pos = self.field_with_ships[shot_pos[0]][shot_pos[1]]
        if isinstance(current_pos, Ship):
            name = current_pos.ship_name
            return name

    def is_hits_at_ships(self, shot_pos):
        current_pos = self.field_with_ships[shot_pos[0]][shot_pos[1]]
        if isinstance(current_pos, Ship):
            hits = len(current_pos.padded_pos)
            return hits
