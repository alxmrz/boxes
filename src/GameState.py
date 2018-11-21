from src.GameObjects import GameObjects
from src.Scene import Scene
from src.Event import Event
from src.levels import levels


class GameState:
    def __init__(self, app):
        self.game_started = False
        self.game_over = False
        self.app = app
        self.current_level = 0
        self.game_objects = GameObjects()
        self.scene = Scene(self, self.game_objects, self.app.window.UI)
        self.event = Event(self, self.game_objects)

    def preupdate(self):
        self.scene.init_start_menu()

    def update(self):
        self.event.handle()

        if self.game_started and self.is_level_completed():
            self._finish_current_level()

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

    def is_wall(self, obj):
        for wall in self.game_objects.walls:
            if obj.colliderect(wall):
                return True
        return False

    def is_box(self, obj):
        for box in self.game_objects.boxes:
            if box is not obj and obj.colliderect(box):
                return True
        return False

    def _finish_current_level(self):
        self.current_level += 1
        if self.current_level >= len(levels):
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
