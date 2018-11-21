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


class GameState:
    def __init__(self, app):
        self.game_started = False
        self.game_over = False
        self.score = 0
        self.app = app
        self.current_level = 0
        self.game_objects = GameObjects()

    def preupdate(self):
        self._init_start_menu()

    def _init_start_menu(self):
        """
        Init primary game state
        :return: None
        """
        self.game_objects.reset()
        self.game_objects.buttons.extend(
            [
                Button(self.app.window.UI, "New game", "new", (400, 100)),
                Button(self.app.window.UI, "Rules", "rules", (400, 250)),
                Button(self.app.window.UI, "Exit", "exit", (400, 400))
            ]
        )

    def _start_new_game(self):
        self.current_level = 0
        self.game_started = True
        self._init_new_level()

    def _show_rules_page(self):
        self.game_objects.reset()
        self.game_objects.texts.append(
            Text(self.app.window.UI, """
            You play as a red box!
            Your goal is to push green boxes to circles.
            When they will be on circles the game is finished.""", (450, 200))
        )
        self.game_objects.buttons.append(
            Button(self.app.window.UI, "Back", "back", (600, 300))
        )

    def _init_new_level(self):
        self.game_objects.reset()
        self.player = Player((400, 300))
        self.game_objects.player = self.player

        self.generate_level_objects(levels.levels[self.current_level])

    def generate_level_objects(self, level):
        level = level.strip().split('\n')
        y = 0
        for line in level:
            line = line.strip()
            x = 0
            for ch in line:
                if ch == 'W':
                    self.game_objects.walls.append(Wall((x, y)))
                elif ch == "P":
                    self.player = Player((x, y))
                    self.game_objects.player = self.player
                elif ch == "B":
                    self.game_objects.boxes.append(Box((x, y)))
                elif ch == "T":
                    self.game_objects.targets.append(Target((x+25, y+25)))
                x+= 50
            y+=50

    def update(self):
        self._handle_events()
        for button in self.game_objects.buttons:
            if button.is_hovered():
                button.color = Window.colors['red']
            elif button.is_clicked():
                if button.id == 'new':
                    self._start_new_game()
                elif button.id == 'rules':
                    self._show_rules_page()
                elif button.id == 'back':
                    self._init_start_menu()
                elif button.id == 'exit':
                    sys.exit(0)
            else:
                button.color = Window.colors['green']
        if self.game_started and self.is_level_completed():
            self.current_level += 1
            if self.current_level >= len(levels.levels):
                self._init_game_finished()
            else:
                self._init_new_level()

    def _init_game_finished(self):
        self.game_objects.reset()
        self.game_objects.texts.append(
            Text(self.app.window.UI, "You win!\nCongratulations!", (450, 200))
        )
        self.game_objects.buttons.append(
            Button(self.app.window.UI, "New game", "new", (450, 300))
        )

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
        for box in self.game_objects.boxes:
            if box.colliderect(self.player):
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

    def is_level_completed(self):
        for target in self.game_objects.targets:
            for box in self.game_objects.boxes:
                if box.colliderect(target.get_rect()):
                    target.status = True
        for target in self.game_objects.targets:
            if target.status == False:
                return False
        return True
