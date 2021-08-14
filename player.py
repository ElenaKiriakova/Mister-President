import pygame

class Player():
    def __init__(self):
        self.x = 50
        self.y = 425
        self.width = 60
        self.height = 71
        self.speed = 5
        self.walkRight = [pygame.image.load('images/right_1.png'), pygame.image.load('images/right_2.png'),
                 pygame.image.load('images/right_3.png'), pygame.image.load('images/right_4.png'),
                 pygame.image.load('images/right_5.png'), pygame.image.load('images/right_6.png')]

        self.walkLeft = [pygame.image.load('images/left_1.png'), pygame.image.load('images/left_2.png'),
                pygame.image.load('images/left_3.png'), pygame.image.load('images/left_4.png'),
                pygame.image.load('images/left_5.png'), pygame.image.load('images/left_6.png')]

        self.playerStand = pygame.image.load('images/idle.png')

        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right:
            self.x += self.speed
        if self.moving_left:
            self.x -= self.speed