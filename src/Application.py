from src.Window import *
from src.GameState import *


class Application:
    def __init__(self):
        self.running = True
        self.game_state = GameState(self)
        self.window = Window(self, 900, 600, 'Arkanoid')

    def run(self):
        """
        Main function of the game
        :return: None
        """
        self.window.init()
        self.game_state.preupdate()

        while self.running:
            self.game_state.update()
            self.window.display()



