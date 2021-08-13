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

    def Jumping(self, isJump, keys, jumpCount):
        if not isJump:
            if keys[pygame.K_SPACE]:
                isJump = True
        else:
            if jumpCount >= -10:
                if jumpCount < 0:
                    self.y += (jumpCount ** 2) / 2
                else:
                    self.y -= (jumpCount ** 2) / 2  # Делим на 2, чтобы игрок не слишком высоко прыгнул
                jumpCount -= 1

            else:
                isJump = False
                jumpCount = 10