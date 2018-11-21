import pygame
import sys
from src.Window import *


class Event():
    def __init__(self, game_state, game_objects):
        self.game_state = game_state
        self.game_objects = game_objects
        pass

    def handle(self):
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
                    if not self.game_state.move_collided_box('LEFT') or self.game_state.is_wall(self.game_objects.player):
                        self.game_objects.player.move(50)
                elif event.key == pygame.K_RIGHT:
                    self.game_objects.player.move(50)
                    if not self.game_state.move_collided_box('RIGHT') or self.game_state.is_wall(self.game_objects.player):
                        self.game_objects.player.move(-50)
                elif event.key == pygame.K_UP:
                    self.game_objects.player.move(0, -50)
                    if not self.game_state.move_collided_box('UP') or self.game_state.is_wall(self.game_objects.player):
                        self.game_objects.player.move(0, 50)
                elif event.key == pygame.K_DOWN:
                    self.game_objects.player.move(0, 50)
                    if not self.game_state.move_collided_box('DOWN') or self.game_state.is_wall(self.game_objects.player):
                        self.game_objects.player.move(0, -50)
        self._handle_buttons_events()

    def _handle_buttons_events(self):
        for button in self.game_objects.buttons:
            if button.is_hovered():
                button.color = Window.colors['red']
            elif button.is_clicked():
                if button.id == 'new':
                    self.game_state.scene.start_new_game()
                elif button.id == 'rules':
                    self.game_state.scene.show_rules_page()
                elif button.id == 'back':
                    self.game_state.scene.init_start_menu()
                elif button.id == 'exit':
                    sys.exit(0)
            else:
                button.color = Window.colors['green']
