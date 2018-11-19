import pygame


class Player(pygame.Rect):
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]
        self.width = 50
        self.heidht = 50
        super().__init__((self.x, self.y), (self.width, self.heidht))

    def move(self, x=0, y=0):
        print('BEFORE:', (self.x, self.y))
        self.x += x
        self.y += y
        print('AFTER:', (self.x, self.y))

    def change_coords(self, coords):
        self.x = coords[0]
        self.y = coords[1]

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), [self.x, self.y, self.width, self.heidht])
