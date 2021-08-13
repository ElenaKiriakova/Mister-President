import pygame

class Snaryad():
    def __init__(self, x, y, radius, color, facing):  # facing - показывает в какую сторону полетит снаряд
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing  # Скорость снаряда

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
