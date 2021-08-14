import pygame
from settings import Settings
from player import Player
from bullets import Snaryad
import game_functions as gf




def run_game():

    pygame.init()

    set = Settings()
    pl = Player()
    # Игровое окно
    win = pygame.display.set_mode((set.win_width, set.win_height))

    # Вывод названия игры
    pygame.display.set_caption("Mister President")

    clock = pygame.time.Clock()

    isJump = False #прыгает игрок или нет
    jumpCount = 10

    lastMove = "right"

    left = False #игрок перемещается влево
    right = False # игрок перемещается вправо


    bullets =[] #Список обьектов класса Snaryad

    while True:
        clock.tick(set.freim_count) #Указываем сколько фреймов в секунду будет в игре

        gf.check_events()

        for bullet in bullets:
            if bullet.x < set.win_width and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))


        # Создаем список в который положим все нажатые кнопки, чтобы их можно было отследить
        keys = pygame.key.get_pressed()


        if keys[pygame.K_f]:
            if lastMove == "right":
                facing = 1
            else:
                facing = -1

            if len(bullets) < 5:

                bullets.append(Snaryad(round(pl.x + pl.width//2), round(pl.y + pl.height//2), set.radius, set.color, facing))

        if keys[pygame.K_LEFT] and pl.x > 5: # x > 5 отвечает, чтобы игрок не вышел за край экрана
            pl.x -= pl.speed
            left = True
            right = False
            lastMove = "left"

        elif keys[pygame.K_RIGHT] and pl.x < set.win_width - pl.width - 5:
            pl.x += pl.speed
            left = False
            right = True
            lastMove = "right"
        else:
            left = False
            right = False
            animCount = 0

        if not isJump:
            if keys[pygame.K_SPACE]:
                isJump = True
        else:
            if jumpCount >= -10:
                if jumpCount < 0:
                    pl.y += (jumpCount ** 2) / 2
                else:
                    pl.y -= (jumpCount ** 2) / 2  # Делим на 2, чтобы игрок не слишком высоко прыгнул
                jumpCount -= 1

            else:
                isJump = False
                jumpCount = 10

        gf.draw_window(set, win, left, right, pl, bullets)


run_game()