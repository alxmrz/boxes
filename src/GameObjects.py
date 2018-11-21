class GameObjects:
    def __init__(self):
        self.targets = []
        self.boxes = []
        self.walls = []
        self.texts = []
        self.buttons = []
        self.player = None

    def all(self):
        all = []

        all.extend(self.targets)
        all.extend(self.boxes)
        all.extend(self.walls)
        all.extend(self.texts)
        all.extend(self.buttons)
        all.append(self.player)

        return all

    def reset(self):
        self.targets = []
        self.boxes = []
        self.walls = []
        self.texts = []
        self.buttons = []
        self.player = None
