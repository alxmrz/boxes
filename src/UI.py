import pygame


class UI:

    def __init__(self, app):
        self.app = app
        self.font = 'freesansbold.ttf'

    def show_text(self, text, coords, size=50, color=(255, 255, 255)):
        """
        Show text on the screen
        :param text: string
        :param coords: List
        :return: None
        """
        font = pygame.font.SysFont(self.font, size)
        text_surface = font.render(text, True, color)
        text_surface_rect = text_surface.get_rect()
        text_surface_rect.center = coords

        self.app.window.screen.blit(text_surface, text_surface_rect)
