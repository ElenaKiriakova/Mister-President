import pygame
from bullets import Snaryad

def draw_window(win, left, right, walkLeft, walkRight, playerStand, bullets, pl, bg):
    global animCount  # Если не вызвать эту переменную, как глобальную, то функция создаст свою локальную переменную

    win.blit(bg, (0, 0))  # Сначала указывает картинку, потом координаты. Сначала надо прорисовать задний фон, потом уже картинку

    if animCount >= 30:  # У нас 30 кадров в секунду каждый спрайт будет идти по 5 кадров(у нас всего 6 спрайтов)
        animCount = 0

    if left:
        win.blit(walkLeft[animCount // 5], (pl.x, pl.y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount // 5], (pl.x, pl.y))
        animCount += 1
    else:
        win.blit(playerStand, (pl.x, pl.y))

    for bullet in bullets:
        bullet.draw(win)
    # функции в качестве параметров передается пверхность,
    # поскольку выбран draw (квадрат), цвет в формате rgb и параментры
    # расположение х и у ширина и высота
    # pygame.draw.rect(win, (0, 0, 255), (x, y, width, height))  # функции в качестве параметров передается пверхность

    # Экран нужно постоянно обновлять
    pygame.display.update()

def key_events(lastMove, bullets, pl, set, isJump, jumpCount):
       # Создаем список в который положим все нажатые кнопки, чтобы их можно было отследить
        for keys in pygame.key.get_pressed():
            if keys[pygame.K_f]:
                if lastMove == "right":
                    facing = 1
                else:
                    facing = -1

                if len(bullets) < 5:
                    bullets.append(Snaryad(round(pl.x + pl.width//2), round(pl.y + pl.height//2), 5, (255, 0, 0), facing))

            if keys[pygame.K_LEFT] and pl.x > 5: # x > 5 отвечает, чтобы игрок не вышел за край экрана
                pl.x -= set.speed
                left = True
                right = False
                lastMove = "left"

            elif keys[pygame.K_RIGHT] and pl.x < set.screen_width - pl.width - 5:
                pl.x += set.speed
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





