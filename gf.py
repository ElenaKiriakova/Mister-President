import pygame

def events(set, bullets):
    for event in pygame.event.get():  # Метод get позволяет получить данные из массива event
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < set.win_width and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

