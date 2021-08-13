import pygame
from player import Player

class Settings(Player):
    def __init__(self):
        super(Settings, self).__init__()
        #Параметры экрана
        self.win_width = 500
        self.win_height = 500
        self.freim_count = 30

        # Параметры пули
        self.radius = 5
        self.color = (255, 0, 0)

        self.bg_image = pygame.image.load('images/bg.jpg')
