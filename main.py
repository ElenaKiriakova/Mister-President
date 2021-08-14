import pygame
from settings import Settings
from player import Player
from bullets import Snaryad
import game_functions as gf

def run_game():
    """Основная функция запуска игры"""
    pygame.init()
    # Вывод названия игры
    pygame.display.set_caption("Mister President")

    # Передаем необходимые классы в функцию
    set = Settings()
    pl = Player()

    # Игровое окно
    win = pygame.display.set_mode((set.win_width, set.win_height))

    clock = pygame.time.Clock()

    # прыгает игрок или нет



    while True:
        clock.tick(set.freim_count) #Указываем сколько фреймов в секунду будет в игре
        gf.check_events()
        gf.fire_bullets(set)
        # Создаем список в который положим все нажатые кнопки, чтобы их можно было отследить
        keys = pygame.key.get_pressed()
        gf.check_key_events(keys, pl, Snaryad, set)
        gf.pl_jump(keys, pl)
        gf.draw_window(set, win, pl)


run_game()