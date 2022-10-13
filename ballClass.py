import pygame
from random import randint
BLACK = (0,0,0)

class Ball(pygame.sprite.Sprite):
    #ball class derived from sprite class

    def __init__(self, color, width, height):
        
        #calling parent class constructor
        super().__init__()

        #pass ball colour, height, and width
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        #draw ball
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [randint(4,8),randint(-8,8)]

        # Fetch rectangle object
        self.rect = self.image.get_rect()

    #gets called every frame to make ball move
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
    
    #makes ball bounce in a random new direction
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)
