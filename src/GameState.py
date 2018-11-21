import sys
import pygame
from src.Player import *
from src.Box import *
from src.Wall import *
from src.Target import *
import src.levels as levels
from src.Button import *
from src.Window import *
from src.Text import *
from src.GameObjects import *
from src.Scene import *

class GameState:
    def __init__(self, app):
        self.game_started = False
        self.game_over = False
        self.app = app
        self.current_level = 0
        self.game_objects = GameObjects()
        self.scene = Scene(self, self.game_objects, self.app.window.UI)

    def preupdate(self):
        self.scene.init_start_menu()

    def update(self):
        self._handle_events()

        if self.game_started and self.is_level_completed():
            self._finish_current_level()

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
                if event.key == pygame.K_LEFT:
                    self.game_objects.player.move(-50)
                    if not self.move_collided_box('LEFT') or self.is_wall(self.game_objects.player):
                        self.game_objects.player.move(50)
                elif event.key == pygame.K_RIGHT:
                    self.game_objects.player.move(50)
                    if not self.move_collided_box('RIGHT') or self.is_wall(self.game_objects.player):
                        self.game_objects.player.move(-50)
                elif event.key == pygame.K_UP:
                    self.game_objects.player.move(0, -50)
                    if not self.move_collided_box('UP') or self.is_wall(self.game_objects.player):
                        self.game_objects.player.move(0, 50)
                elif event.key == pygame.K_DOWN:
                    self.game_objects.player.move(0, 50)
                    if not self.move_collided_box('DOWN') or self.is_wall(self.game_objects.player):
                        self.game_objects.player.move(0, -50)
        self._handle_buttons_events()

    def move_collided_box(self, direction):
        for box in self.game_objects.boxes:
            if box.colliderect(self.game_objects.player):
                if direction == 'UP':
                    box.move(0, -50)
                    if self.is_wall(box) or self.is_box(box):
                        box.move(0, 50)
                        return False
                elif direction == 'DOWN':
                    box.move(0, 50)
                    if self.is_wall(box) or self.is_box(box):
                        box.move(0, -50)
                        return False
                elif direction == 'LEFT':
                    box.move(-50)
                    if self.is_wall(box) or self.is_box(box):
                        box.move(50)
                        return False
                elif direction == 'RIGHT':
                    box.move(50)
                    if self.is_wall(box) or self.is_box(box):
                        box.move(-50)
                        return False
        return True

    def is_wall(self, object):
        for wall in self.game_objects.walls:
            if object.colliderect(wall):
                return True
        return False

    def is_box(self, object):
        for box in self.game_objects.boxes:
            if box is not object and object.colliderect(box):
                return True
        return False

    def _handle_buttons_events(self):
        for button in self.game_objects.buttons:
            if button.is_hovered():
                button.color = Window.colors['red']
            elif button.is_clicked():
                if button.id == 'new':
                    self.scene.start_new_game()
                elif button.id == 'rules':
                    self.scene.show_rules_page()
                elif button.id == 'back':
                    self.scene.init_start_menu()
                elif button.id == 'exit':
                    sys.exit(0)
            else:
                button.color = Window.colors['green']

    def _finish_current_level(self):
        self.current_level += 1
        if self.current_level >= len(levels.levels):
            self.scene.init_game_finished()
        else:
            self.scene.init_new_level()

    def is_level_completed(self):
        for target in self.game_objects.targets:
            for box in self.game_objects.boxes:
                if box.colliderect(target.get_rect()):
                    target.status = True
        for target in self.game_objects.targets:
            if target.status == False:
                return False
        return True
