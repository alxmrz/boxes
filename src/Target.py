import pygame
from src.Window import Window

class Target:
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]
        self.width = 40
        self.height = 40
        self.radius = 20
        self.rect = pygame.Rect((self.x - self.radius, self.y - self.radius), (self.width, self.height))
        self.status = False

    def get_rect(self):
        return self.rect

    def draw(self, screen):
        pygame.draw.circle(screen, Window.colors['red'], (self.x, self.y), self.radius)
