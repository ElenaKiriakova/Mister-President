import pygame

def run_game():
    pygame.init()

    # Игровое окно
    win = pygame.display.set_mode((500, 500))

    # Вывод названия игры
    pygame.display.set_caption("Mister President")

    # Данные игрока
    x = 50
    width = 40
    y = 425 # высота экрана - ширина игрока - "земля"
    height = 60
    speed = 5

    isJump = False #прыгает игрок или нет
    jumpCount = 10

    run = True
    while run:
        pygame.time.delay(50) # Данный цикл будет выполняться каждую 0.1 сек
        for event in pygame.event.get(): # Метод get позволяет получить данные из массива event
            if event.type == pygame.QUIT:
                run = False



        # Создаем список в который положим все нажатые кнопки, чтобы их можно было отследить
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > 5: # x > 5 отвечает, чтобы игрок не вышел за край экрана
            x -= speed
        if keys[pygame.K_RIGHT] and x < 500 - width - 5:
            x += speed
        if not isJump:
            if keys[pygame.K_UP] and y > 5:
                y -= speed
            if keys[pygame.K_DOWN] and y < 500 - height - 15:
                y += speed
            if keys[pygame.K_SPACE]:
                isJump = True
        else:
            


        # Чтобы за игроком не оставались старые спрайты, вводим функцию заполнения экрана фоновым цветом
        win.fill((0,0,0))
        # Создаем игрока
        # функции в качестве параметров передается пверхность,
        # поскольку выбран draw (квадрат), цвет в формате rgb и параментры
        # расположение х и у ширина и высота
        pygame.draw.rect(win, (0, 0, 255), (x, y, width, height))  # функции в качестве параметров передается пверхность

        # Экран нужно постоянно обновлять
        pygame.display.update()


    pygame.quit() #Если цикл будет равен False то игра автоматически выйдет


run_game()