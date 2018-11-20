import pygame


class Target():
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]
        self.width = 50
        self.heidht = 50
        self.rect = pygame.Rect((self.x - 20, self.y - 20), (40, 40))
        self.status = False

    def get_rect(self):
        return self.rect

    def draw(self, screen):
        pygame.draw.circle(screen, (200, 40, 70), (self.x, self.y), 20)
