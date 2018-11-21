import pygame
from src.Application import *


class UI:

    def __init__(self, application):
        self.app = application

    def show_text(self, text, coords, size=50, color=(255, 255, 255)):
        """
        Show text on the screen
        :param text: string
        :param coords: list
        :return: None
        """
        font = pygame.font.SysFont('freesansbold.ttf', size)
        textsurface = font.render(text, True, color)
        textsurfaceRectObj = textsurface.get_rect()
        textsurfaceRectObj.center = coords
        self.app.window.screen.blit(textsurface, textsurfaceRectObj)
