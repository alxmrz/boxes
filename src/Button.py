import pygame
from src.Window import Window


class Button(pygame.Rect):
    def __init__(self, ui, text, id, coords):
        self.x = coords[0]
        self.y = coords[1]
        self.width = 120
        self.height = 50
        self.id = id
        self.ui = ui
        self.color = Window.colors['green']
        self.text = text
        super().__init__((self.x, self.y), (self.width, self.height))

    def move(self, x=0, y=0):
        self.x += x
        self.y += y

    def is_hovered(self):
        """
        Check, is button hovered with mouse
        :return: bool
        """
        return self.collidepoint(pygame.mouse.get_pos()) and not self.is_clicked()

    def is_clicked(self):
        """
        Check, is button clicked with left mouse key
        :return:
        """
        return pygame.mouse.get_pressed()[0] and self.collidepoint(pygame.mouse.get_pos())

    def draw(self, screen):
        """
        Draw button
        :param screen: pygame.surface.Surface
        :return: None
        """
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height], 2)
        self.ui.show_text(self.text, (self.x + self.width // 2, self.y + self.height // 2), 30)

