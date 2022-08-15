import json

dead_ships = 0
shot_at_ship = False

with open('data_file.json') as f:
    ships_dict = json.load(f)


def stop_game():
    if dead_ships == len(ships_dict["layout"]):
        print('Игра закончена! Поздравляю!')
        return True
    else:
        return False


def shooting(hit):
    global dead_ships
    global shot_at_ship
    shot_at_ship = False
    for ship in ships_dict["layout"]:
        if hit in ship['positions']:
            print(ship['positions'])
            print("Попадание")
            print(f"Удаляем из списка {hit}")
            ship['positions'].remove(hit)
            shot_at_ship = True
            if len(ship['positions']) == 0:
                print("Корабль полностью подбит")
                dead_ships += 1
                print(f'Подбито кораблей: {dead_ships}')

        else:
            print(ship['positions'])
            print("Нет попадания")

        print()
    return print(f"Привет, медвед, подбито {dead_ships}, Корабль подбит? {shot_at_ship}")
