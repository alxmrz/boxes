import pygame
from src.Window import *

class Button(pygame.Rect):
    def __init__(self, ui, text, id, coords):
        self.x = coords[0]
        self.y = coords[1]
        self.width = 120
        self.heidht = 50
        self.id = id
        self.ui = ui
        self.color = Window.colors['green']
        self.text = text
        super().__init__((self.x, self.y), (self.width, self.heidht))

    def move(self, x=0, y=0):
        self.x += x
        self.y += y

    def is_hovered(self):
        return self.collidepoint(pygame.mouse.get_pos()) and not self.is_clicked()

    def is_clicked(self):
        return pygame.mouse.get_pressed()[0] and self.collidepoint(pygame.mouse.get_pos())

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.heidht], 2)
        self.ui.show_text(self.text, (self.x + self.width // 2, self.y + self.height // 2), 30)

