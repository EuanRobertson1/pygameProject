from turtle import width
import pygame
BLACK = (0,0,0)

class Paddle(pygame.sprite.Sprite):
    #Class which represents a paddle (Derived from Sprite class)
        
        def __init__(self, color, width, height) :
                #call parent class constructor
            super().__iniit__()

            #pass colour,width and height of paddle
            self.image = pygame.Surface([width, height])
            self.image.fill(BLACK)#
            self.image.set_colorkey(BLACK)

            #draw the paddle i.e. a rectangle
            pygame.draw.rect(self.image, color, [0,0, width, height])

            #fetch rectangle object
            self.rect = self.image.get_rect()