from src.Player import *
from src.Box import *
from src.Wall import *
from src.Target import *
import src.levels as levels
from src.Button import *
from src.Window import *
from src.Text import *
from src.GameObjects import *


class Scene:
    def __init__(self, game_state, game_objects, ui):
        self.game_state = game_state
        self.game_objects = game_objects
        self.ui = ui

    def init_start_menu(self):
        """
        Init primary game state
        :return: None
        """
        self.game_objects.reset()
        self.game_objects.buttons.extend(
            [
                Button(self.ui, "New game", "new", (400, 100)),
                Button(self.ui, "Rules", "rules", (400, 250)),
                Button(self.ui, "Exit", "exit", (400, 400))
            ]
        )

    def show_rules_page(self):
        self.game_objects.reset()
        self.game_objects.texts.append(
            Text(self.ui, """
            You play as a red box!
            Your goal is to push green boxes to circles.
            When they will be on circles the game is finished.""", (450, 200))
        )
        self.game_objects.buttons.append(
            Button(self.ui, "Back", "back", (600, 300))
        )

    def init_game_finished(self):
        self.game_objects.reset()
        self.game_objects.texts.append(
            Text(self.ui, "You win!\nCongratulations!", (450, 200))
        )
        self.game_objects.buttons.append(
            Button(self.ui, "New game", "new", (450, 300))
        )

    def start_new_game(self):
        self.game_state.current_level = 0
        self.game_state.game_started = True
        self.init_new_level()

    def init_new_level(self):
        self.game_objects.reset()
        self.game_state.player = Player((400, 300))
        self.game_objects.player = self.game_state.player

        self._generate_level_objects(levels.levels[self.game_state.current_level])

    def _generate_level_objects(self, level):
        level = level.strip().split('\n')
        y = 0
        for line in level:
            line = line.strip()
            x = 0
            for ch in line:
                if ch == 'W':
                    self.game_objects.walls.append(Wall((x, y)))
                elif ch == "P":
                    self.game_state.player = Player((x, y))
                    self.game_objects.player = self.game_state.player
                elif ch == "B":
                    self.game_objects.boxes.append(Box((x, y)))
                elif ch == "T":
                    self.game_objects.targets.append(Target((x+25, y+25)))
                x += 50
            y += 50
