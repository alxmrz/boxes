from src.UI import *
import pygame


class Window():

    def __init__(self, app, width, height, title):
        self.title = title
        self.width = width
        self.height = height
        self.UI = UI(app)
        self.app = app
        self.screen = None
        self.colors = {
            'black': (0, 0, 0)
        }

    def init(self):
        """
        Init window and screen painter
        :return: None
        """
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        level = pygame.surface.Surface((self.width, self.height), pygame.SRCALPHA, 32)
        pygame.display.set_caption(self.title)

    def display(self):
        """
        Display scnene, objects and ui
        :return: None
        """
        self.screen.fill(self.colors['black'])

        self._draw_scene_objects()
        self.UI.show()

        pygame.display.flip()

    def _draw_scene_objects(self):
        """
        Draw game objects for interaction
        :return: None
        """
        for name, object in self.app.game_state.game_objects.items():
            if name == 'player':
                object.draw(self.screen)
            else:
                for o in object:
                    o.draw(self.screen)

