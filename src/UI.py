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
        if self.app.game_state.game_over:
            self._show_text('Game over!', (500, 300))
            self._show_text('Your score: ' + str(self.app.game_state.score), (500, 400))
            self._show_text('Press [space] to start new game', (500, 450))
        elif not self.app.game_state.game_started:
            self._show_text('Press [space] to start new game', (500, 300))
        elif not self.app.game_state.game_objects['plates']:
            self.app.game_over = True
            self._show_text('You win!', (500, 300))
            self._show_text('Your score: ' + str(self.app.game_state.score), (500, 400))
            self._show_text('Press [space] to start new game', (500, 450))
        else:
            self._show_text('Score: ' + str(self.app.game_state.score), (100, 550))

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