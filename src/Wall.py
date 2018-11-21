import pygame


class Wall(pygame.Rect):
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]
        self.width = 50
        self.heidht = 50
        self.image = pygame.image.load("images/wall.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        super().__init__((self.x, self.y), (self.width, self.heidht))

    def move(self, x=0, y=0):
        self.x += x
        self.y += y

    def draw(self, screen):
        screen.blit(self.image, self)
        #pygame.draw.rect(screen, (0, 0, 255), [self.x, self.y, self.width, self.heidht])
