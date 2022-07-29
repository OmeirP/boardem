import pygame
import random
import time


blue=(0,0,255)
gridBlu=(80, 101, 135) #for grid
red=(255,0,0)
purple=(154, 74, 224) #for player 1
greyBG=(48,48,48) #for background
sprngGrn=(0, 255, 149) #for player 2


pygame.init()
clock = pygame.time.Clock()


display_width = 1100
display_height = 1200

gameDisplay=pygame.display.set_mode((display_width,display_height))



#p1StrtCoords=(370,680)
#p2StrtCoords=(370,700)


p1Coords=(370,680)
p2Coords=(370,700)


def drawGrid():
    tileSize=60
    for x in range(340, (display_width-340), tileSize):
        for y in range(300, display_height-480, tileSize):
            rect = pygame.Rect(x, y, tileSize, tileSize)
            pygame.draw.rect(gameDisplay, gridBlu, rect, 1)
            
def drawCountrs():
    pygame.draw.circle(gameDisplay, purple, p1Coords, 10)
    pygame.draw.circle(gameDisplay, sprngGrn, p2Coords, 10)
    



def game_loop():


    gameExit = False
    

    cntrChange=60
    #counter diameter is 20
    
    
    
    
    
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
        gameDisplay.fill(greyBG)
        drawGrid()
        drawCountrs()
        
        
        pygame.display.update()
        clock.tick(60)

game_loop()
