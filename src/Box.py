import pygame


class Box(pygame.Rect):
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]
        self.width = 50
        self.height = 50
        self.image = pygame.image.load("images/box.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        super().__init__((self.x, self.y), (self.width, self.height))

    def move(self, x=0, y=0):
        self.x += x
        self.y += y

    def draw(self, screen):
        screen.blit(self.image, self)
        #pygame.draw.rect(screen, (0, 255, 0), [self.x, self.y, self.width, self.height])
