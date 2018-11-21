import pygame


class Player(pygame.Rect):
    width = 50
    height = 50

    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]
        self.direction = 'UP'
        self.frames = {
            'UP':[
                (22, 0, 70, 50),
                (22, 65, 70, 50),
                (22, 132, 70, 50),
                (22, 196, 70, 50),
                (22, 260, 70, 50)
            ],
            'DOWN': [
                (336, 0, 386, 50),
                (336, 65, 386, 50),
                (336, 132, 386, 50),
                (336, 196, 386, 50),
                (336, 260, 386, 50)
            ],
            'LEFT': [
                (22, 0, 70, 50),
                (22, 65, 70, 50),
                (22, 132, 70, 50),
                (22, 196, 70, 50),
                (22, 260, 70, 50)
            ],
            'RIGHT': [
                (195, 0, 50, 50),
                (195, 65, 50, 50),
                (195, 132, 50, 50),
                (195, 196, 50, 50),
                (195, 260, 50, 50)
            ]
        }
        self.current_frame = 0
        self.image = pygame.image.load("images/man.png")
        self.animation_time = 0.1
        self.current_time = 0
        super().__init__((self.x, self.y), (self.width, self.height))

    def move(self, direction, x=0, y=0):
        self.direction = direction
        self.x += x
        self.y += y

    def change_coords(self, coords):
        self.x = coords[0]
        self.y = coords[1]

    def draw(self, screen, dt):
        self.current_time += dt
        screen.blit(self.image, self, self.frames[self.direction][self.current_frame])

        if self.current_time >= self.animation_time:
            self.current_time = 0

            if self.current_frame >= len(self.frames)-1:
                self.current_frame = 0
            else:
                self.current_frame += 1
