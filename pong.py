from math import fabs
from paddleClass import Paddle
from ballClass import Ball
import pygame
pygame.init()

#colours used in game
BLACK = (0,0,0)
NEON = (57,255,20)

#pygame window
size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PyPong")

#create paddles using paddleClass
p1Paddle = Paddle(NEON,10, 100)#new paddle object
p1Paddle.rect.x = 20 #start pos x
p1Paddle.rect.y = 200 #start pos y

p2Paddle = Paddle(NEON,10, 100)#new paddle object
p2Paddle.rect.x = 670 #start pos x
p2Paddle.rect.y = 200 #start pos y

#create ball using ballClass
ball = Ball(NEON,10,10)

#list of all sprites
spritesList = pygame.sprite.Group()

#add paddles to list
spritesList.add(p1Paddle)
spritesList.add(p2Paddle)

#add ball to list
spritesList.add(ball)

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
        p1Paddle.moveUp(6)
    if keys[pygame.K_s]:
        p1Paddle.moveDown(6)
    if keys[pygame.K_UP]:
        p2Paddle.moveUp(6)
    if keys[pygame.K_DOWN]:
        p2Paddle.moveDown(6)
    
    #Game logic goes here
    spritesList.update()

    #check is ball is bouncing against any walls
    if ball.rect.x>=690:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1]

    #detect collision between ball and paddles
    if pygame.sprite.collide_mask(ball,p1Paddle) or pygame.sprite.collide_mask(ball,p2Paddle):
        ball.bounce()

    #Drawing code
    screen.fill(BLACK)#make the screen black
   
    pygame.draw.line(screen, NEON, [349, 0], [349, 500], 5)#draw white line in middle of screen

    #draw sprites
    spritesList.draw(screen)
    
    pygame.display.flip()#update the screen with drawing

    #limit game to 60fps
    gameClock.tick(60)


#exit game once out of loop
pygame.quit()
