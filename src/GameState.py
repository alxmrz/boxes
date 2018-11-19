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
            'boxes': [],
            'walls': []
        }

        self.level1 = """
        WWWWWWWWWWWWWWWWWW
        WPW   W     W    W
        W W W W W W W  W W
        W   W W W W W  W W
        W W W W W W W  W W   
        W W W W W W W  W W   
        W W W   W        W   
        WWWWWWW     WWWWWW 
        WW       WWWWWWWWW 
        WWWWWWWW      WWWW 
        WWW      WWWWWWWWW 
        WWWWWWWWWWWWWWWWWW 
        """

        self.generate_level_objects(self.level1)

    def generate_level_objects(self, level):
        level = level.strip().split('\n')

        y = 0
        for line in level:
            line = line.strip()
            x = 0
            for ch in line:
                if ch == 'W':
                    self.game_objects['walls'].append(Wall((x, y)))
                elif ch == "P":
                    self.player = Player((x, y))
                    self.game_objects['player'] = self.player
                elif ch == "B":
                    self.game_objects['boxes'].append(Box((x, y)))
                x+= 50
            y+=50

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
                    if not self.move_collided_box('LEFT') or self.is_wall(self.player):
                        self.player.move(50)
                elif event.key == pygame.K_RIGHT:
                    self.player.move(50)
                    if not self.move_collided_box('RIGHT') or self.is_wall(self.player):
                        self.player.move(-50)
                elif event.key == pygame.K_UP:
                    self.player.move(0, -50)
                    if not self.move_collided_box('UP') or self.is_wall(self.player):
                        self.player.move(0, 50)
                elif event.key == pygame.K_DOWN:
                    self.player.move(0, 50)
                    if not self.move_collided_box('DOWN') or self.is_wall(self.player):
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