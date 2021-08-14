import sys
import pygame


animCount = 0
isJump = False
jumpCount = 10
bullets =[] #Список обьектов класса Snaryad
lastMove = "right"
left = False #игрок перемещается влево
right = False # игрок перемещается вправо

#keys = pygame.key.get_pressed()

def check_events():

    for event in pygame.event.get():  # Метод get позволяет получить данные из массива event
        if event.type == pygame.QUIT:
             sys.exit()


def check_key_events(keys, pl, Snaryad, set):
    global lastMove
    global bullets
    global left
    global right

    if keys[pygame.K_f]:
        if lastMove == "right":
            facing = 1
        else:
            facing = -1

        if len(bullets) < 5:
            bullets.append(
                Snaryad(round(pl.x + pl.width // 2), round(pl.y + pl.height // 2), set.radius, set.color, facing))

    if keys[pygame.K_LEFT] and pl.x > 5:  # x > 5 отвечает, чтобы игрок не вышел за край экрана
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




def draw_window(set, win, pl):
    global bullets
    global left
    global right
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


def pl_jump(keys, pl):
    global isJump
    global jumpCount

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

def fire_bullets(set):
    global bullets
    for bullet in bullets:
        if bullet.x < set.win_width and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))