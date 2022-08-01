dict_indicator_pos = {"carrier": ((190, 220), (220, 220), (250, 220), (280, 220), (310, 220)),
                      "battleship": ((190, 270), (220, 270), (250, 270), (280, 270)),
                      "cruiser": ((190, 320), (220, 320), (250, 320)),
                      "submarine": ((190, 370), (220, 370), (250, 370)),
                      "destroyer": ((190, 420), (220, 420))}


class Ship:

    def __init__(self, positions: list, name: str, indicator_pos, padded_pos=None):
        ship_length = len(positions)
        if padded_pos is None:
            padded_pos = []
            self.indicator_pos = indicator_pos
            self.ship_length = ship_length
            self.padded_pos = padded_pos
            self.name = name
            self.positions = positions


    # подбитие корабля
    def hit_at_ship(self, shot):
        if shot not in self.padded_pos:
            self.padded_pos.append(shot)
            return True
        else:
            return False

    # количество подбитий у корабля
    def counter_hits(self):
        return len(self.padded_pos)

    # уничтожение корабля
    def ship_dead(self):
        if self.ship_length == len(self.padded_pos):
            return True
        else:
            return False

    def __repr__(self):
        return "s"
