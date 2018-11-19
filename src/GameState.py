import sys
import pygame
from src.Player import *
from src.Box import *
from src.Wall import *


class GameState:

    def __init__(self, app):
        self.game_started = False
        self.game_over = False
        self.score = 0
        self.app = app
        self.game_objects = {
            'ball': None,
            'platform': None,
            'plates': []
        }

    def preupdate(self):
        self._init_game_objects()

    def _init_game_objects(self):
        """
        Init primary game state
        :return: None
        """
        self.box = Box((300, 300))
        self.player = Player((400, 300))
        self.walls = Wall((300, 500))
        self.score = 0

        self.game_objects = {
            'player': self.player,
            'boxes': (self.box,),
            'walls': (self.walls,)
        }

    def _create_plates_table(self):
        """
        Creates plates table for destroying. 9 row and 16 columns.
        :return:
        """
        result = []
        y_row = 5
        for row in range(9):
            x_row = 5
            for column in range(16):
                result.append(Plate((x_row, y_row)))
                x_row += 55
            y_row += 25

        return result

    def update(self):
        self._handle_events()



        self.app.window.display()

    def _handle_events(self):
        """
        Handling events
        :return: None
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not self.game_started:
                        self.game_started = True
                    elif self.game_over:
                        self.game_over = False
                        self._init_game_objects()
                    else:
                        self.game_started = False
                elif event.key == pygame.K_LEFT:
                    self.player.move(-50)
                    if not self.move_collided_box('LEFT'):
                        self.player.move(50)
                elif event.key == pygame.K_RIGHT:
                    self.player.move(50)
                    if not self.move_collided_box('RIGHT'):
                        self.player.move(-50)
                elif event.key == pygame.K_UP:
                    self.player.move(0, -50)
                    if not self.move_collided_box('UP'):
                        self.player.move(0, 50)
                elif event.key == pygame.K_DOWN:
                    self.player.move(0, 50)
                    if not self.move_collided_box('DOWN'):
                        self.player.move(0, -50)

    def move_collided_box(self, direction):
        for box in self.game_objects['boxes']:
            if box.colliderect(self.player):
                if direction == 'UP':
                    box.move(0, -50)
                    if self.is_wall(box):
                        box.move(0, 50)
                        return False
                elif direction == 'DOWN':
                    box.move(0, 50)
                    if self.is_wall(box):
                        box.move(0, -50)
                        return False
                elif direction == 'LEFT':
                    box.move(-50)
                    if self.is_wall(box):
                        box.move(50)
                        return False
                elif direction == 'RIGHT':
                    box.move(50)
                    if self.is_wall(box):
                        box.move(-50)
                        return False
        return True

    def is_wall(self, object):
        for wall in self.game_objects['walls']:
            if object.colliderect(wall):
                return True
        return False