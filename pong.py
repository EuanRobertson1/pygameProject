from math import fabs
from paddleClass import Paddle
import pygame
pygame.init()

#colours used in game
BLACK = (0,0,0)
WHITE = (255,255,255)

#pygame window
size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PyPong")

#create paddles using paddleClass
p1Paddle = Paddle(WHITE,10, 100)#new paddle object
p1Paddle.rect.x = 20 #start pos x
p1Paddle.rect.y = 200 #start pos y

p2Paddle = Paddle(WHITE,10, 100)#new paddle object
p2Paddle.rect.x = 670 #start pos x
p2Paddle.rect.y = 200 #start pos y

#list of all sprites
spritesList = pygame.sprite.Group()

#add paddles to list
spritesList.add(p1Paddle)
spritesList.add(p2Paddle)

#loop boolean
keepRunning = True 

#game clock to control game update rate
gameClock = pygame.time.Clock()

#-----main loop for game-----
while keepRunning:
    #event loop
    for event in pygame.event.get(): #user did something
        if event.type == pygame.QUIT: #If use clicks close
            keepRunning = False #exit loop
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x:
                keepRunning=False


    #Moving paddles event handler
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        p1Paddle.moveUp(5)
    if keys[pygame.K_s]:
        p1Paddle.moveDown(5)
    if keys[pygame.K_UP]:
        p2Paddle.moveUp(5)
    if keys[pygame.K_DOWN]:
        p2Paddle.moveDown(5)
    
    #Game logic goes here
    spritesList.update()


    #Drawing code
    screen.fill(BLACK)#make the screen black
   
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)#draw white line in middle of screen

    #draw sprites
    spritesList.draw(screen)
    
    pygame.display.flip()#update the screen with drawing

    #limit game to 60fps
    gameClock.tick(60)


#exit game once out of loop
pygame.quit()
