import sys
import pygame


animCount = 0

def check_events():

    for event in pygame.event.get():  # Метод get позволяет получить данные из массива event
        if event.type == pygame.QUIT:
             sys.exit()


def draw_window(set, win, left, right, pl, bullets):
    #animCount = 0 # Если не вызвать эту переменную, как глобальную, то функция создаст свою локальную переменную
    global animCount

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

    # Экран нужно постоянно обновлять
    pygame.display.update()
