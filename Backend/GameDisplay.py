import sys

import pygame
from pygame.locals import *

from main import *

display_size_x = 840
display_size_y = 600
space = 4
LINES = 10
shot_counter = 0

small_xy_hit_size = display_size_y / 30
ship_size = (display_size_x / 14, display_size_y / 3)

pygame.init()
game_display = pygame.display.set_mode((display_size_x, display_size_y))
pygame.display.set_caption('BattleShip')
# pygame.display.set_icon(pygame.image.load("pictures/ship_icon.png"))
game_display.fill('white')

counter_style = pygame.font.Font(None, 50)
player_style = pygame.font.Font(None, 25)


def update_surf_count_1():
    counter_1_surf.fill("#facb03")
    player_text_style = pygame.font.Font(None, 25)

    player_name = player_text_style.render('Player 1', True, (0, 0, 0))
    counter_1_surf.blit(player_name, (30, 90))

    pygame.draw.line(counter_1_surf, 'black', [10, 75], [110, 75], 2)


def update_counter_1(value=0):
    sign_counter_1 = counter_style.render(f'{value:02}', True, (0, 0, 0))
    counter_1_surf.blit(sign_counter_1, (40, 25))
    game_display.blit(counter_1_surf, (display_size_x / 14, display_size_y / 10))


def update_surf_count_2():
    counter_2_surf.fill("#62a79e")

    player_name = player_style.render('Player 2', True, (0, 0, 0))
    counter_2_surf.blit(player_name, (30, 90))

    pygame.draw.line(counter_2_surf, 'black', [10, 75], [110, 75], 2)

    sign_counter_2 = counter_style.render(f'00', True, (0, 0, 0))
    counter_2_surf.blit(sign_counter_2, (40, 25))

    game_display.blit(counter_2_surf, (display_size_x / 4.5, display_size_y / 10))


def update_counter_2():
    pass


def draw_base_indicators():
    for value in dict_indicator_pos.values():
        for pos in value:
            empty_cell = pygame.transform.scale(pygame.image.load('pictures/m_Miss small.png'),
                                                (small_xy_hit_size, small_xy_hit_size))
            game_display.blit(empty_cell, pos)


draw_base_indicators()


def update_indicators(condition_field):
    current_pos = condition_field.field_with_ships[shot[0]][shot[1]]
    if isinstance(current_pos, Ship):
        padded_cell = pygame.transform.scale(pygame.image.load('pictures/m_Hit small.png'),
                                             (small_xy_hit_size, small_xy_hit_size))
        game_display.blit(padded_cell, current_pos.indicator_pos[current_pos.counter_hits() - 1])


def draw_lines():
    for line in range(1, LINES):
        pygame.draw.line(field_surf, (0, 0, 0), ((field_surf.get_width() / LINES) * line, 0),
                         ((field_surf.get_width() / LINES) * line, field_surf.get_width()), 2)

        pygame.draw.line(field_surf, (0, 0, 0), (0, (field_surf.get_height() / LINES) * line),
                         (field_surf.get_height(), (field_surf.get_height() / LINES) * line), 2)


def click_on_field():
    if (display_size_x / 2.3) < pygame.mouse.get_pos()[0] < ((display_size_x / 2.3) + (display_size_x / 2)) and (
            display_size_y / 10) < pygame.mouse.get_pos()[1] < ((display_size_y / 10) + display_size_x / 2):
        return True


def convert_to_cell(field_pos):  # Принимает координаты внутри игрового поля.
    cell_size = (field_surf.get_width() / 10, field_surf.get_height() / 10)
    field_cell = (int(field_pos[0] // cell_size[0]), int(field_pos[1] // cell_size[1]))
    return field_cell


def draw_hits_on_field(condition_field):
    for x, line in enumerate(condition_field.base_field):
        for y, place in enumerate(line):
            if place == "*":
                red_x = pygame.transform.scale(pygame.image.load('pictures/red x.png'),
                                               (big_xy_hit_size, big_xy_hit_size))
                field_surf.blit(red_x, ((field_surf.get_width() / 10) * x, (field_surf.get_height() / 10) * y))
            if place == "x":
                black_x = pygame.transform.scale(pygame.image.load('pictures/black x.png'),
                                                 (big_xy_hit_size, big_xy_hit_size))
                field_surf.blit(black_x, ((field_surf.get_width() / 10) * x, (field_surf.get_height() / 10) * y))


def show_victory_message():
    victory_message = player_style.render(f"All ships hit, you win!"
                                          f" Number of shots fired: {shot_counter}", True, (0, 0, 0))
    game_display.blit(victory_message, (200, 500))


# Cчётчик 1
counter_1_surf = pygame.Surface((display_size_x / 7, display_size_x / 7))

update_surf_count_1()
update_counter_1(GameLogic.dead_ships)

# Cчётчик 2
counter_2_surf = pygame.Surface((display_size_x / 7, display_size_x / 7))

update_surf_count_2()

# Параметры кораблей
carrier_shape = pygame.transform.scale(pygame.image.load('pictures/Carrier_shape.png'), (120, 40))
game_display.blit(carrier_shape, (display_size_x / 14, 200))

battleship_shape = pygame.transform.scale(pygame.image.load('pictures/Battleship_Shape.png'), (120, 40))
game_display.blit(battleship_shape, (display_size_x / 14, 250))

cruiser_shape = pygame.transform.scale(pygame.image.load('pictures/Cruiser_Shape.png'), (120, 40))
game_display.blit(cruiser_shape, (display_size_x / 14, 300))

submarine_shape = pygame.transform.scale(pygame.image.load('pictures/Submarine_Shape.png'), (120, 40))
game_display.blit(submarine_shape, (display_size_x / 14, 350))

destroyer_shape = pygame.transform.scale(pygame.image.load('pictures/Destroyer_Shape.png'), (120, 40))
game_display.blit(destroyer_shape, (display_size_x / 14, 400))

# Параметры поля
field_surf = pygame.Surface((display_size_x / 2, display_size_x / 2))  # Создаём новый дисплей, для игрового поля.
field_surf.fill("gray")

big_xy_hit_size = field_surf.get_width() / 10

draw_lines()  # Разбиваем поле линиями

field_frame = pygame.draw.rect(field_surf, (250, 203, 3),
                               (0, 0, display_size_x / 2, display_size_x / 2), 3)  # Добавляем оранжевую рамку

# Указываем выстрелы на поле

field_condition = GameFieldCondition()

game_display.blit(field_surf, (display_size_x / 2.3, display_size_y / 10))  # Отрисовываем игровое поле

# События поля
LEFT = 1
RIGHT = 3
running = 1

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    elif event.type == pygame.MOUSEBUTTONDOWN and (event.button == LEFT or event.button == RIGHT) and click_on_field():
        # print("Нажата кнопка мыши")
        field_pos_correction = (int(pygame.mouse.get_pos()[0] - display_size_x / 2.3),
                                int(pygame.mouse.get_pos()[1] - display_size_y / 10))

        shot = convert_to_cell(field_pos_correction)
        shot_counter += 1
        print(f"Всего сделано выстрелов: {shot_counter}")
        # print(f"По координатам: {pygame.mouse.get_pos()}")
        # print(f"Координаты внутри поля: {field_pos_correction}")
        print(f"Координаты ячейки: {shot}")

        GameLogic.shooting(list(shot))
        update_counter_1(GameLogic.dead_ships)
        field_condition.note_shoot(list(shot))

        draw_hits_on_field(field_condition)
        game_display.blit(field_surf, (display_size_x / 2.3, display_size_y / 10))

        update_indicators(field_condition)  # Индикаторы подбития

        update_counter_1(GameLogic.dead_ships)
        # update_counter_2()

        if GameLogic.dead_ships == len(ships_dict["layout"]):
            show_victory_message()
            running = 0

    update_surf_count_1()
    # update_surf_count_2()

    pygame.display.flip()


# Условия выхода и основной цикл
def event_handler():
    for game_event in pygame.event.get():
        if game_event.type == QUIT:
            pygame.quit()
            sys.exit()


while True:
    event_handler()
    pygame.display.update()
