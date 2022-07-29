import pygame
import random
import time


black=(0,0,0)
blue=(0,0,255)
gridBlu=(80, 101, 135) #for grid
red=(255,0,0)
purple=(154, 74, 224) #for player 1
greyBG=(48,48,48) #for background
sprngGrn=(0, 255, 149) #for player 2
whitish=(230, 230, 230)
drkWhitish=(209, 209, 209)

drkSageGrn=(121, 145, 129)
sageGrn=(154, 181, 163)

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
    
    
    
    
def text_colour(text,font):
    textSurface = font.render(text, True, black)     #True is for antialiasing.
    return textSurface, textSurface.get_rect()


def button(msg,x,y,w,h,ic,ac,action=None): #ic is inactive colour, ac is active colour (mouse rollover)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            if action == "roll":
                #fancy dice function
                pass
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))
    smallText = pygame.font.Font("freesansbold.ttf",46)
    textSurf, textRect = text_colour(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)



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
        button("Roll",450,(display_height-240),200,80,drkSageGrn,sageGrn,"roll")
        
        
        pygame.display.update()
        clock.tick(60)

game_loop()
