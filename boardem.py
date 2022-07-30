import pygame
import random
import time


black=(0,0,0)
blue=(0,0,255)
gridBlu=(80, 101, 135) #for grid
textblu=(120, 120, 120)
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
    spaceNum=43
    for y in range(300, display_height-480, tileSize):
        for x in range(340, (display_width-340), tileSize):
        
            rect = pygame.Rect(x, y, tileSize, tileSize)
            pygame.draw.rect(gameDisplay, gridBlu, rect, 1)
            font = pygame.font.SysFont(None, 26)
            spcNumTxt = font.render(str(spaceNum), True, black)
            gameDisplay.blit(spcNumTxt, (pygame.Rect(x+3, y+3, tileSize, tileSize))) # slight offset of rect so doesn't appear over grid lines.
            spaceNum+=1 #start at 43, works from left to right, does top row first. after row done, decrease count by 14 to get back to start of row and go down another row (in terms of the count)
        spaceNum-=14
            
            
            
def drawCountrs():
    pygame.draw.circle(gameDisplay, purple, p1Coords, 10)
    pygame.draw.circle(gameDisplay, sprngGrn, p2Coords, 10)
    
    
    
    
def text_colour(text,font):
    textSurface = font.render(text, True, black)     #True is for antialiasing.
    return textSurface, textSurface.get_rect()


def dice():
    dnum=random.randint(1,6)
    return dnum
    
    
    
        
def button(msg,x,y,w,h,ic,ac,ev,action=None): #ic is inactive colour, ac is active colour (mouse rollover)
    global msg2
    global dnum
    mouse = pygame.mouse.get_pos()
    if x+w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        for event in ev:
            if event.type ==pygame.MOUSEBUTTONDOWN and action != None:
                if action == "roll":
                    dnum=dice()
                    font = pygame.font.SysFont(None, 200)
                    msg2 = font.render(str(dnum), True, black)
                    gameDisplay.blit(msg2, (510,(display_height-425),120,120))
                
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))
    bigText = pygame.font.Font("freesansbold.ttf",46)
    textSurf, textRect = text_colour(msg, bigText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)
    

def movePointer(): #function that gets location of where counter should go after a dice roll
    print(dnum)
    pass



"""
def diceNumBlit(diceNum):
    font = pygame.font.SysFont(None, 200)
    msg2 = font.render(str(diceNum), True, black)
    gameDisplay.blit(msg2, (510,(display_height-425),120,120))"""




def game_loop():
    gameExit = False
    

    cntrChange=60
    #counter diameter is 20
    
    
    
    
    while not gameExit:
        
        
        ev=pygame.event.get()
        
        for event in ev:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            

                    
        gameDisplay.fill(greyBG)
        drawGrid()
        drawCountrs()
        button("Roll",450,(display_height-240),200,80,drkSageGrn,sageGrn,ev,"roll")
        pygame.draw.rect(gameDisplay, red, (490,(display_height-420),120,120),5) #dice box
        try:
            gameDisplay.blit(msg2, (510,(display_height-425),120,120))
        except:
            pass
        try:
            movePointer()
        except:
            pass #no value for dnum yet
        


        

        
        pygame.display.update()
        clock.tick(60)
 
game_loop()
