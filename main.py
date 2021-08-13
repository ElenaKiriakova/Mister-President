import pygame
from settings import Settings
from player import Player
import gf as gf
from bullets import Snaryad

animCount = 0 # на каком фрейме сейчас находится анимация
def run_game():


    pygame.init()


    pl = Player()
    set = Settings()
    #bull = Snaryad(pl.x, pl.y, radius, color, facing)

    # Игровое окно
    win = pygame.display.set_mode((set.screen_width, set.screen_height))
    # Вывод названия игры
    pygame.display.set_caption("Mister President")

    clock = pygame.time.Clock()

     #прыгает игрок или нет
    isJump = False
    jumpCount = 10

    lastMove = "right"

    left = False #игрок перемещается влево
    right = False # игрок перемещается вправо

    walkRight = [pygame.image.load('images/right_1.png'), pygame.image.load('images/right_2.png'),
                 pygame.image.load('images/right_3.png'), pygame.image.load('images/right_4.png'),
                 pygame.image.load('images/right_5.png'), pygame.image.load('images/right_6.png')]

    walkLeft = [pygame.image.load('images/left_1.png'), pygame.image.load('images/left_2.png'),
                pygame.image.load('images/left_3.png'), pygame.image.load('images/left_4.png'),
                pygame.image.load('images/left_5.png'), pygame.image.load('images/left_6.png')]

    bg = pygame.image.load('images/bg.jpg')

    playerStand = pygame.image.load('images/idle.png') #Изображение когда игрок стоит

    bullets =[] #Список обьектов класса Snaryad

    run = True

    while run:
        clock.tick(30) #Указываем сколько фреймов в секунду будет в игре
        for event in pygame.event.get(): # Метод get позволяет получить данные из массива event
            if event.type == pygame.QUIT:
                run = False

        for bullet in bullets:
            if bullet.x < set.screen_width and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))


        gf.key_events(lastMove, bullets, pl, set, isJump, jumpCount)

        gf.draw_window(win, left, right, walkLeft, walkRight, playerStand, bullets, pl, bg)

    pygame.quit() #Если цикл будет равен False то игра автоматически выйдет


run_game()