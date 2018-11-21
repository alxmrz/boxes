from src.UI import UI
from src.Player import Player
import pygame


class Window:
    colors = {
        'black': (0, 0, 0),
        'white': (255, 255, 255),
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255)
    }

    def __init__(self, app, width, height, title):
        self.title = title
        self.width = width
        self.height = height
        self.UI = UI(app)
        self.fps = 60
        self.app = app
        self.screen = None
        self.clock = pygame.time.Clock()

    def init(self):
        """
        Init window and screen painter
        :return: None
        """
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

    def display(self):
        """
        Display scnene, objects and ui
        :return: None
        """
        dt = self.clock.tick(self.fps) / 1000
        self.screen.fill(self.colors['black'])

        self._draw_scene_objects(dt)

        pygame.display.flip()

    def _draw_scene_objects(self, dt):
        """
        Draw game objects for interaction
        :return: None
        """
        for obj in self.app.game_state.game_objects.all():
            if obj is not None:
                if isinstance(obj, Player):
                    obj.draw(self.screen, dt)
                else:
                    obj.draw(self.screen)
