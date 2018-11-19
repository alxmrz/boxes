import pygame
from src.Application import *


class UI:

    def __init__(self, application):
        self.app = application

    def show(self) -> None:
        """
        Show ui
        :return: None
        """
        pass

    def _show_text(self, text, coords):
        """
        Show text on the screen
        :param text: string
        :param coords: list
        :return: None
        """
        font = pygame.font.SysFont('freesansbold.ttf', 50)
        textsurface = font.render(text, True, (255, 255, 255))
        textsurfaceRectObj = textsurface.get_rect()
        textsurfaceRectObj.center = coords
        self.app.window.screen.blit(textsurface, textsurfaceRectObj)