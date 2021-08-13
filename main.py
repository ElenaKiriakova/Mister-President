import pygame
from settings import Settings
from player import Player
from bullets import Snaryad
import gf as gf


animCount = 0 # на каком фрейме сейчас находится анимация
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

    bg = pygame.image.load('images/bg.jpg')





    def draw_window():
        global animCount # Если не вызвать эту переменную, как глобальную, то функция создаст свою локальную переменную


        win.blit(set.bg_image, (0, 0)) #Сначала указывает картинку, потом координаты. Сначала надо прорисовать задний фон, потом уже картинку

        if animCount >= set.freim_count: #У нас 30 кадров в секунду каждый спрайт будет идти по 5 кадров(у нас всего 6 спрайтов)
            animCount = 0

        if left:
            win.blit(pl.walkLeft[animCount//5], (pl.x, pl.y))
            animCount += 1
        elif right:
            win.blit(pl.walkRight[animCount // 5], (pl.x, pl.y))
            animCount += 1
        else:
            win.blit(pl.playerStand, (pl.x, pl.y))

        for bullet in bullets:
            bullet.draw(win)
        # функции в качестве параметров передается пверхность,
        # поскольку выбран draw (квадрат), цвет в формате rgb и параментры
        # расположение х и у ширина и высота
        #pygame.draw.rect(win, (0, 0, 255), (x, y, width, height))  # функции в качестве параметров передается пверхность

        # Экран нужно постоянно обновлять
        pygame.display.update()

    bullets =[] #Список обьектов класса Snaryad

    run = True

    while run:
        clock.tick(set.freim_count) #Указываем сколько фреймов в секунду будет в игре

        for event in pygame.event.get():  # Метод get позволяет получить данные из массива event
            if event.type == pygame.QUIT:
                run = False

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

        draw_window()

    pygame.quit() #Если цикл будет равен False то игра автоматически выйдет


run_game()