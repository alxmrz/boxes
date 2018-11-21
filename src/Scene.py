from src.levels import levels
from src.Player import Player
from src.Box import Box
from src.Wall import Wall
from src.Target import Target
from src.Button import Button
from src.Text import Text


class Scene:
    def __init__(self, game_state, game_objects, ui):
        self.game_state = game_state
        self.game_objects = game_objects
        self.ui = ui

    def init_start_menu(self):
        """
        Init start menu page
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
        """
        Init rules page
        :return: None
        """
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
        """
        If game is finished show relevant message
        :return:
        """
        self.game_objects.reset()
        self.game_objects.texts.append(
            Text(self.ui, "You win!\nCongratulations!", (450, 200))
        )
        self.game_objects.buttons.append(
            Button(self.ui, "New game", "new", (450, 300))
        )

    def start_new_game(self):
        """
        :return: None
        """
        self.game_state.current_level = 0
        self.game_state.game_started = True
        self.init_new_level()

    def init_new_level(self):
        """
        :return: None
        """
        self.game_objects.reset()
        self.game_objects.player = Player((400, 300))

        self._generate_level_objects(levels[self.game_state.current_level])
        self.game_objects.buttons.extend([
            Button(self.ui, "Restart", "restart", (10, 500)),
            Button(self.ui, "Exit", "exit", (200, 500))
            ]
        )

    def _generate_level_objects(self, level):
        """
        Generate objects of level from special string
        :param level: string
        :return:
        """
        level = level.strip().split('\n')
        y = 0
        for line in level:
            line = line.strip()
            x = 0
            for ch in line:
                if ch == 'W':
                    self.game_objects.walls.append(Wall((x, y)))
                elif ch == "P":
                    self.game_objects.player = Player((x, y))
                elif ch == "B":
                    self.game_objects.boxes.append(Box((x, y)))
                elif ch == "T":
                    self.game_objects.targets.append(Target((x+25, y+25)))
                x += 50
            y += 50
