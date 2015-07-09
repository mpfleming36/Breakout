'''
CS 391
Mike Fleming
Lab 2: Breakout

'''
import pygame
import sys
import random

from Box import *
from Colors import *
pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
UIBoard = pygame.font.SysFont("monospace", 30)
score = 0
lives = 3
gameState = 0

paddleYDefault = SCREEN_HEIGHT-40
paddleXDefault = SCREEN_WIDTH/2-25
ballXDefault = paddleXDefault+20
ballYDefault = paddleYDefault-20

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
start = False
scoreSound = pygame.mixer.Sound("scoreSound.ogg")


boxList = []
boxList.append(Box(paddleXDefault, paddleYDefault, 50, 10, 0, 0, Color.magenta,"paddle",0))
boxList.append(Box(ballXDefault,ballYDefault,10,10,0,0,Color.cyan,"ball",0)) #ball change #paddle change
boxList.append(Box(0,0,200,40,0,0,Color.green,"brick",3))
boxList.append(Box(200,0,200,40,0,0,Color.green,"brick",3))
boxList.append(Box(400,0,200,40,0,0,Color.green,"brick",3))
boxList.append(Box(600,0,200,40,0,0,Color.green,"brick",3))
boxList.append(Box(0,40,200,40,0,0,Color.green,"brick",2))
boxList.append(Box(200,40,200,40,0,0,Color.green,"brick",2))
boxList.append(Box(400,40,200,40,0,0,Color.green,"brick",2))
boxList.append(Box(600,40,200,40,0,0,Color.green,"brick",2))
boxList.append(Box(0,80,200,40,0,0,Color.green,"brick",1))
boxList.append(Box(200,80,200,40,0,0,Color.green,"brick",1))
boxList.append(Box(400,80,200,40,0,0,Color.green,"brick",1))
boxList.append(Box(600,80,200,40,0,0,Color.green,"brick",1))

#Assigning Box objects to their proper names
ball = boxList[1]
paddle = boxList[0]

#starts new round
def newround():
    global lives
    global start
    ball.x = ballXDefault
    ball.y = ballYDefault
    ball.vx = 0
    ball.vy = 0
    paddle.x = paddleXDefault
    paddle.y = paddleYDefault
    start = False
    lives -= 1

#prints score and asks to play again. 
def gameOver():
    global gameState
    gameState= 1
    totScore = score + lives
    screen.fill(Color.black)
    endGameLabel = UIBoard.render(str("Game Over You Scored:"),1,Color.white)
    screen.blit(endGameLabel, (SCREEN_WIDTH/4, 200))
    endScoreLabel = UIBoard.render(str(totScore),1,Color.white)
    screen.blit(endScoreLabel, (SCREEN_WIDTH/2-10, SCREEN_HEIGHT/2+20))
    resetGameLabel = UIBoard.render(str("Press 'R' To Restart"),1,Color.white)
    screen.blit(resetGameLabel, (SCREEN_WIDTH/4, SCREEN_HEIGHT-50))

#restarts game from the beginning after gameover
def restart ():
    newround()
    global score
    score = 0
    global lives
    lives = 3
    global gameState
    gameState = 0
    boxList[2]=Box(0,0,200,40,0,0,Color.green,"brick",3)
    boxList[3]=Box(200,0,200,40,0,0,Color.green,"brick",3)
    boxList[4]=Box(400,0,200,40,0,0,Color.green,"brick",3)
    boxList[5]=Box(600,0,200,40,0,0,Color.green,"brick",3)
    boxList[6]=Box(0,40,200,40,0,0,Color.green,"brick",2)
    boxList[7]=Box(200,40,200,40,0,0,Color.green,"brick",2)
    boxList[8]=Box(400,40,200,40,0,0,Color.green,"brick",2)
    boxList[9]=Box(600,40,200,40,0,0,Color.green,"brick",2)
    boxList[10]=Box(0,80,200,40,0,0,Color.green,"brick",1)
    boxList[11]=Box(200,80,200,40,0,0,Color.green,"brick",1)
    boxList[12]=Box(400,80,200,40,0,0,Color.green,"brick",1)
    boxList[13]=Box(600,80,200,40,0,0,Color.green,"brick",1)
    
def controls():
    global start
    
    if (paddle.y>paddleYDefault-24):
        if(keyboard[pygame.K_w] or keyboard[pygame.K_UP]):
            paddle.y -=2
            if (start == False):
                ball.y += -2
    if (paddle.y<paddleYDefault):
        if(keyboard[pygame.K_s] or keyboard[pygame.K_DOWN]):
            paddle.y +=2
            if(start == False):
                ball.y += 2
    
    if(keyboard[pygame.K_a] or keyboard[pygame.K_LEFT]):
        paddle.x -=6
        if (start == False):
            ball.x += -6
    if(keyboard[pygame.K_d] or keyboard[pygame.K_RIGHT]):
        paddle.x +=6
        if(start == False):
            ball.x += 6
    if(start == False):
        if(keyboard[pygame.K_SPACE]):
            start = True
            ball.vy = -4
            ball.vx = -4
while(True):
    screen.fill(Color.black)
    keyboard = pygame.key.get_pressed()
    
    #checks game state to start the game
    if(gameState ==0):
        
    #controls for paddle
        controls()
        #prints score and lives
        scoreLabel = UIBoard.render(str(score), 1, Color.white)
        screen.blit(scoreLabel, (SCREEN_WIDTH-50, SCREEN_HEIGHT-25))
        livesLabel = UIBoard.render(str(lives), 1, Color.white)
        screen.blit(livesLabel, (25, SCREEN_HEIGHT-25))
    
        #starts new round if ball goes out of bounds
        if (ball.y > paddleYDefault+5):
            newround()
            
        #changes box health
        for i in range(2,len(boxList)):
            if(boxList[i].health == 2):
                boxList[i].color = Color.yellow
            elif (boxList[i].health == 1):
                boxList[i].color = Color.red
            if((boxList[i].boxType=="brick") and (boxList[i].health==0)):
                boxList[i] = Box(0,0,0,0,0,0,Color.black,"brick",-1)
                score+=1
                scoreSound.play()
    
    #updates for ball, paddle, and boxes
        for i in range(0,len(boxList)):
            boxList[i].update(screen, SCREEN_WIDTH, SCREEN_HEIGHT,boxList)
            
    #checks if the game is over by lives or brick score.
    if ((score == 12) or (lives==0)):
        gameOver()
        if (keyboard[pygame.K_r]):
            restart()

    msElapsed = clock.tick(30) #SYNC RATE 30 FPS

    pygame.display.update() #SYNC 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit();