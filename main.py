import pygame
animCount = 0 # на каком фрейме сейчас находится анимация
def run_game():
    pygame.init()

    # Игровое окно
    win = pygame.display.set_mode((500, 500))

    # Вывод названия игры
    pygame.display.set_caption("Mister President")

    clock = pygame.time.Clock()

    # Данные игрока
    x = 50
    width = 60
    height = 71
    y = 425 # высота экрана - ширина игрока - "земля"

    speed = 5

    isJump = False #прыгает игрок или нет
    jumpCount = 10


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

    def draw_window():
        global animCount # Если не вызвать эту переменную, как глобальную, то функция создаст свою локальную переменную


        win.blit(bg, (0, 0)) #Сначала указывает картинку, потом координаты. Сначала надо прорисовать задний фон, потом уже картинку

        if animCount >= 30: #У нас 30 кадров в секунду каждый спрайт будет идти по 5 кадров(у нас всего 6 спрайтов)
            animCount = 0

        if left:
            win.blit(walkLeft[animCount//5], (x, y))
            animCount += 1
        elif right:
            win.blit(walkRight[animCount // 5], (x, y))
            animCount += 1
        else:
            win.blit(playerStand, (x, y))


        # функции в качестве параметров передается пверхность,
        # поскольку выбран draw (квадрат), цвет в формате rgb и параментры
        # расположение х и у ширина и высота
        #pygame.draw.rect(win, (0, 0, 255), (x, y, width, height))  # функции в качестве параметров передается пверхность

        # Экран нужно постоянно обновлять
        pygame.display.update()


    run = True

    while run:
        clock.tick(30) #Указываем сколько фреймов в секунду будет в игре
        for event in pygame.event.get(): # Метод get позволяет получить данные из массива event
            if event.type == pygame.QUIT:
                run = False



        # Создаем список в который положим все нажатые кнопки, чтобы их можно было отследить
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > 5: # x > 5 отвечает, чтобы игрок не вышел за край экрана
            x -= speed
            left = True
            right = False

        elif keys[pygame.K_RIGHT] and x < 500 - width - 5:
            x += speed
            left = False
            right = True
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
                    y += (jumpCount ** 2) / 2
                else:
                    y -= (jumpCount**2)/2 #Делим на 2, чтобы игрок не слишком высоко прыгнул
                jumpCount -= 1

            else:
                isJump = False
                jumpCount = 10

        draw_window()

    pygame.quit() #Если цикл будет равен False то игра автоматически выйдет


run_game()