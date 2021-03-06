from src.Window import Window
from src.GameState import GameState


class Application:
    def __init__(self):
        self.running = True
        self.window = Window(self, 900, 600, 'Boxes')
        self.game_state = GameState(self)

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
