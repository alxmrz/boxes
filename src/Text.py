class Text:
    def __init__(self, ui, text, coords):
        self.text = text
        self.ui = ui
        self.x = coords[0]
        self.y = coords[1]

    def draw(self, screen):
        lines = self.text.strip().split('\n')
        y = self.y
        for line in lines:
            self.ui.show_text(line, (self.x, y), 30)
            y += 32
