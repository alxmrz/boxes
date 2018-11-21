import pygame
from src.Window import Window


class Player(pygame.Rect):
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]
        self.width = 50
        self.height = 50
        super().__init__((self.x, self.y), (self.width, self.height))

    def move(self, x=0, y=0):
        self.x += x
        self.y += y

    def change_coords(self, coords):
        self.x = coords[0]
        self.y = coords[1]

    def draw(self, screen):
        pygame.draw.rect(screen, Window.colors['red'], [self.x, self.y, self.width, self.height])
