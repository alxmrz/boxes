import pygame


class Target:
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]
        self.width = 40
        self.height = 40
        self.radius = 20
        self.rect = pygame.Rect((self.x - 20, self.y - 20), (self.width, self.height))
        self.status = False

    def get_rect(self):
        return self.rect

    def draw(self, screen):
        pygame.draw.circle(screen, (200, 40, 70), (self.x, self.y), self.radius)
