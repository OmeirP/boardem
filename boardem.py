import pygame
import random
import time


black=(0,0,0)
blue=(0,0,255)
gridBlu=(80, 101, 135) #for grid
textblu=(120, 120, 120)
darkerRed=(165,0,0)
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

p1spc=1
p2spc=1


turn="player1"

readyToMove=False


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
    global p1spc
    global p2spc
    global p1Coords
    global p2Coords
    
    st_p1Coords=(370,680)
    st_p2Coords=(370,700)
    
    
    #change y coord depending on what row they are on
    p1yDecrs=60*((p1spc-1)//7)
    p1Coords=list(st_p1Coords)
    p1Coords[1]-=p1yDecrs
    p1Coords=tuple(p1Coords)
    
    p2yDecrs=60*((p2spc-1)//7)
    p2Coords=list(st_p2Coords)
    p2Coords[1]-=p2yDecrs
    p2Coords=tuple(p2Coords)
    
    
    if p1spc < 8:
        p1xIncrs=60*(p1spc-1)
    elif p1spc < 15 and p1spc >= 7:
        p1xIncrs=60*(p1spc-8)
    elif p1spc < 22 and p1spc >= 14:
        p1xIncrs=60*(p1spc-15)
    elif p1spc < 29 and p1spc >= 21:
        p1xIncrs=60*(p1spc-22)
    elif p1spc < 36 and p1spc >= 28:
        p1xIncrs=60*(p1spc-29)
    elif p1spc < 43 and p1spc >= 35:
        p1xIncrs=60*(p1spc-36)
    
    
    p1Coords=list(p1Coords)
    p1Coords[0]+=p1xIncrs
    p1Coords=tuple(p1Coords)
    
    if p2spc < 8:
        p2xIncrs=60*(p2spc-1)
    elif p2spc < 15 and p2spc >= 7:
        p2xIncrs=60*(p2spc-8)
    elif p2spc < 22 and p2spc >= 14:
        p2xIncrs=60*(p2spc-15)
    elif p2spc < 29 and p2spc >= 21:
        p2xIncrs=60*(p2spc-22)
    elif p2spc < 36 and p2spc >= 28:
        p2xIncrs=60*(p2spc-29)
    elif p2spc < 43 and p2spc >= 35:
        p2xIncrs=60*(p2spc-36)
    
    
    p2Coords=list(p2Coords)
    p2Coords[0]+=p2xIncrs
    p2Coords=tuple(p2Coords)
    
    
    
    pygame.draw.circle(gameDisplay, purple, p1Coords, 10)
    pygame.draw.circle(gameDisplay, sprngGrn, p2Coords, 10)
        
    
    
    
def text_colour(text,font):
    textSurface = font.render(text, True, black)     #True is for antialiasing.
    return textSurface, textSurface.get_rect()


def dice():
    return random.randint(1,6)




def playerTurnBlit():
    global turn
    font = pygame.font.SysFont("harlowsolid", 58)
    if turn == "player1":
        turnTeller = font.render("Player 1's turn:", True, purple)
        gameDisplay.blit(turnTeller, (20,800,300,120))
    elif turn == "player2":
        turnTeller = font.render("Player 2's turn:", True, sprngGrn)
        gameDisplay.blit(turnTeller, (20,800,300,120))
    
    
    
    
        
def button(msg,x,y,w,h,ic,ac,ev,action=None): #ic is inactive colour, ac is active colour (mouse rollover)
    global dice1txt
    global dice2txt
    global d1num
    global d2num
    global turn
    global hideDice
    global readyToMove
    mouse = pygame.mouse.get_pos()
    if x+w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        for event in ev:
            if event.type ==pygame.MOUSEBUTTONDOWN and action != None:
                if action == "roll" and readyToMove==False:
                    hideDice=False
                    d1num=dice()
                    d2num=dice()
                    diceTotal=d1num+d2num
                    font = pygame.font.SysFont(None, 200)
                    dice1txt = font.render(str(d1num), True, black) #set-up for displaying dice roll in main loop
                    dice2txt = font.render(str(d2num), True, black)
                                            
                    readyToMove=True

                    print(movePointer())

            
                elif action == "move" and readyToMove==True:
                    #update player position here
                    hideDice=True
                    if turn == "player1":
                        turn = "player2"
                    elif turn == "player2":
                        turn = "player1"
                    readyToMove=False
                    
                    
                    
                    
                
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))
        
    bigText = pygame.font.Font("freesansbold.ttf",46)
    textSurf, textRect = text_colour(msg, bigText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)
    




def movePointer(): #function that gets location of where counter should go after a dice roll
    global p1spc
    global p2spc
    
    diceTotal=d1num+d2num
    if d1num==d2num:
        double=True
    else:
        double=False
    print("total:",d1num+d2num)
    print("is double:", double)
    if turn=="player1":
        if double == False:
            p1spc+=diceTotal
        elif double == True:
            if p1spc - diceTotal < 1:
                p1spc = 1
            else:
                p1spc -= diceTotal
        return p1spc
                
    elif turn == "player2":
        if double == False:
            p2spc+=diceTotal
        elif double == True:
            if p2spc - diceTotal < 1:
                p2spc = 1
            else:
                p2spc -= diceTotal
        return p2spc

    
    



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
        button("Roll",450,960,200,80,drkSageGrn,sageGrn,ev,"roll")
        button("Move",450,10,200,80,drkSageGrn,sageGrn,ev,"move")
        pygame.draw.rect(gameDisplay, darkerRed, (430,(display_height-420),120,120),5) #dice box
        pygame.draw.rect(gameDisplay, darkerRed, (550,(display_height-420),120,120),5)
        playerTurnBlit()
        try:
            if hideDice==False:
                gameDisplay.blit(dice1txt, (450,(display_height-425),120,120))
                gameDisplay.blit(dice2txt, (570,(display_height-425),120,120))
        except:
            pass
            



        

        
        pygame.display.update()
        clock.tick(60)
 
game_loop()
