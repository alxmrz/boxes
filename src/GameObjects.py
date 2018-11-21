class GameObjects:
    def __init__(self):
        self.targets = []
        self.boxes = []
        self.walls = []
        self.texts = []
        self.buttons = []
        self.player = None

    def all(self):
        """
        Get a list of all objects of the game
        :return: List
        """
        result = []

        result.extend(self.targets)
        result.extend(self.boxes)
        result.extend(self.walls)
        result.extend(self.texts)
        result.extend(self.buttons)
        result.append(self.player)

        return result

    def reset(self):
        """
        Delete game objects
        :return:
        """
        self.targets = []
        self.boxes = []
        self.walls = []
        self.texts = []
        self.buttons = []
        self.player = None
