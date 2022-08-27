import pygame
import random


black=(0,0,0)
blue=(0,0,255)
gridBlu=(80, 101, 135) #for grid
textblu=(120, 120, 120)
veryblu=(0, 160, 209)
darkerRed=(165,0,0)
red=(255,0,0)
purple=(154, 74, 224) #for player 1
greyBG=(48,48,48) #for background
sprngGrn=(0, 255, 149) #for player 2
whitish=(230, 230, 230)
drkWhitish=(209, 209, 209)
orange=(255, 154, 23)
drkSageGrn=(121, 145, 129)
sageGrn=(154, 181, 163)
drkGrn=(68, 87, 67)
titlBlu=(0, 126, 176)
snakeGreen=(90, 166, 20)



msgFile=open("msgs.txt","r")
msg1=(msgFile.readline())
msg2=(msgFile.readline())
msg3=(msgFile.readline())
msgFile.close()



obstMvs=open("obstRules.txt","r")
snkChng=int(obstMvs.readline())
ladChng=int(obstMvs.readline())
obstMvs.close()



pygame.init()
clock = pygame.time.Clock()


display_width = 1100
display_height = 1200

gameDisplay=pygame.display.set_mode((display_width,display_height))

ev=pygame.event.get()







#p1StrtCoords=(370,680)
#p2StrtCoords=(370,700)





won=False

p1Coords=(370,680)
p2Coords=(370,700)

p1spc=1
p2spc=1




turn="player1"

readyToMove=False


def drawGrid():
    tileSize=60
    boxNum=0
    
    gridNums=[43,44,45,46,47,48,49,42,41,40,39,38,37,36,29,30,31,32,33,34,35,28,27,26,25,24,23,22,15,16,17,18,19,20,21,14,13,12,11,10,9,8,1,2,3,4,5,6,7]
    
    for y in range(300, display_height-480, tileSize):
        for x in range(340, (display_width-340), tileSize):
        
            rect = pygame.Rect(x, y, tileSize, tileSize)
            pygame.draw.rect(gameDisplay, gridBlu, rect, 1)
            font = pygame.font.SysFont(None, 26)
            spcNumTxt = font.render(str(gridNums[boxNum]), True, black)
            gameDisplay.blit(spcNumTxt, (pygame.Rect(x+3, y+3, tileSize, tileSize))) # slight offset of rect so doesn't appear over grid lines.
            boxNum+=1
            #spaceNum+=1 #start at 43, works from left to right, does top row first. after row done, decrease count by 14 to get back to start of row and go down another row (in terms of the count)
        #spaceNum-=14



class snakeClass:
    def __init__(self,snkChng):
        #self.headX=headX
        #self.headY=headY
        #self.tailX=tailX
        #self.tailY=tailY
        self.snkChng=snkChng
        self.headSpc=random.randint(19,48)
        self.tailSpc=self.headSpc+snkChng
        
        
    def snakeDraw(self):
        

        if self.headSpc < 19 and self.headSpc >= 8:
            headXChange=60*(self.headSpc-8)
            row="even"
        elif self.headSpc < 22 and self.headSpc >= 15:
            headXChange=60*(self.headSpc-15)
            row="odd"
        elif self.headSpc < 29 and self.headSpc >= 22:
            headXChange=60*(self.headSpc-22)
            row="even"
        elif self.headSpc < 36 and self.headSpc >= 29:
            headXChange=60*(self.headSpc-29)
            row="odd"
        elif self.headSpc < 43 and self.headSpc >= 36:
            headXChange=60*(self.headSpc-36)
            row="even"
        elif self.headSpc >= 43:
            headXChange=60*(self.headSpc-43)
            row="odd"    
        
        if row == "even":
            headX=730-headXChange
        elif row == "odd":
            headX=370+headXChange

        headYChange=60*((self.headSpc-1)//7)
        headY=690-headYChange
        
        headPos=(headX,headY)
        
        
        ###################################################
        
        if self.tailSpc < 8:
            tailXChange=60*(self.tailSpc-1)
            row="odd"
        elif self.tailSpc < 15 and self.tailSpc >= 8:
            tailXChange=60*(self.tailSpc-8)
            row="even"
        elif self.tailSpc < 22 and self.tailSpc >= 15:
            tailXChange=60*(self.tailSpc-15)
            row="odd"
        elif self.tailSpc < 29 and self.tailSpc >= 22:
            tailXChange=60*(self.tailSpc-22)
            row="even"
        elif self.tailSpc < 36 and self.tailSpc >= 29:
            tailXChange=60*(self.tailSpc-29)
            row="odd"
        elif self.tailSpc < 43 and self.tailSpc >= 36:
            tailXChange=60*(self.tailSpc-36)
            row="even"
        elif self.tailSpc >= 43:
            tailXChange=60*(self.tailSpc-43)
            row="odd"    
        
        if row == "even":
            tailX=730-tailXChange
        elif row == "odd":
            tailX=370+tailXChange
        
        tailYChange=60*((self.tailSpc-1)//7)
        tailY=690-tailYChange
        
        
        tailPos=(tailX,tailY)    
            
        #print(headSpc,tailSpc,headPos,tailPos)
        #print(tailPos, tailX, tailXChange)
        
        pygame.draw.line(gameDisplay, snakeGreen, headPos, tailPos, 12)
        

snk1=snakeClass(snkChng)

def calcCntPos():
    
    
    global p1spc
    global p2spc
    global p1Coords
    global p2Coords
    
    st_p1Coords=(370,680)
    st_p2Coords=(370,700)
    
    
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
        row="odd"
    elif p1spc < 15 and p1spc >= 8:
        p1xIncrs=60*(p1spc-8)
        row="even"
    elif p1spc < 22 and p1spc >= 15:
        p1xIncrs=60*(p1spc-15)
        row="odd"
    elif p1spc < 29 and p1spc >= 22:
        p1xIncrs=60*(p1spc-22)
        row="even"
    elif p1spc < 36 and p1spc >= 29:
        p1xIncrs=60*(p1spc-29)
        row="odd"
    elif p1spc < 43 and p1spc >= 36:
        p1xIncrs=60*(p1spc-36)
        row="even"
    elif p1spc >= 43:
        p1xIncrs=60*(p1spc-43)
        row="odd"    
        
    
    if row=="odd":
        p1Coords=list(p1Coords)
        p1Coords[0]+=p1xIncrs
        p1Coords=tuple(p1Coords)
    elif row == "even":
        p1Coords=list(p1Coords)
        p1Coords[0]= 730-p1xIncrs
        p1Coords=tuple(p1Coords)
        
    
    if p2spc < 8:
        p2xIncrs=60*(p2spc-1)
        row="odd"
    elif p2spc < 15 and p2spc >= 8:
        p2xIncrs=60*(p2spc-8)
        row="even"
    elif p2spc < 22 and p2spc >= 15:
        p2xIncrs=60*(p2spc-15)
        row="odd"
    elif p2spc < 29 and p2spc >= 22:
        p2xIncrs=60*(p2spc-22)
        row="even"
    elif p2spc < 36 and p2spc >= 29:
        p2xIncrs=60*(p2spc-29)
        row="odd"
    elif p2spc < 43 and p2spc >= 36:
        p2xIncrs=60*(p2spc-36)
        row="even"
    elif p2spc >= 43:
        p2xIncrs=60*(p2spc-43)
        row="odd"

    
    if row=="odd":
        p2Coords=list(p2Coords)
        p2Coords[0]+=p2xIncrs   
        p2Coords=tuple(p2Coords)
    elif row == "even":
        p2Coords=list(p2Coords)
        p2Coords[0]= 730-p2xIncrs
        p2Coords=tuple(p2Coords)
            
def drawCountrs():

    
    try:
        if hideDice:
            calcCntPos()
    except NameError:
        calcCntPos()
    
    #change y coord depending on what row they are on


    



    pygame.draw.circle(gameDisplay, purple, p1Coords, 10)
    pygame.draw.circle(gameDisplay, sprngGrn, p2Coords, 10)
        
    
    
    
def text_colour(text,font,colour):
    textSurface = font.render(text, True, colour)     #True is for antialiasing.
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
    
    
    
    
        
def button(bttnTxt,bttnCol,x,y,w,h,ic,ac,ev,action=None): #ic is inactive colour, ac is active colour (mouse rollover)
    global dice1txt
    global dice2txt
    global d1num
    global d2num
    global turn
    global hideDice
    global readyToMove
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    
    if x+w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        
        for event in ev:
            if event.type ==pygame.MOUSEBUTTONDOWN and action != None:
                if action == "roll" and readyToMove==False:
                    hideDice=False
                    d1num=dice()
                    d2num=dice()
                    font = pygame.font.SysFont(None, 200)
                    dice1txt = font.render(str(d1num), True, black) #set-up for displaying dice roll in main loop
                    dice2txt = font.render(str(d2num), True, black)
                                            
                    readyToMove=True

                    print(movePointer(msg2))
            
            
                elif action == "move" and readyToMove==True:
                    #update player position here
                    hideDice=True
                    if turn == "player1":
                        turn = "player2"
                    elif turn == "player2":
                        turn = "player1"
                    readyToMove=False
                    
        
            if click[0] == 1 and action != None:
            
                if action == "play":
                    game_loop()
                elif action == "quit":
                    pygame.quit()
                    quit()                    
                       
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))
        
        
    bigText = pygame.font.Font("freesansbold.ttf",46)
    textSurf, textRect = text_colour(bttnTxt, bigText,bttnCol)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)
    




def movePointer(msg2): #function that gets location of where counter should go after a dice roll
    global p1spc
    global p2spc
    global doubleTxt
    global double

    
    diceTotal=d1num+d2num
    if d1num==d2num:
        double=True
    else:
        double=False
    print("total:",d1num+d2num)
    print("is double:", double)
    
    
    if turn=="player1":
        if double == False:
            if (p1spc+diceTotal) > 49:
                pass
            elif (p1spc+diceTotal) == 49:
                p1spc+=diceTotal
                win("Player 1")
            elif (p1spc+diceTotal) < 49:
                if (p1spc+diceTotal) == snk1.headSpc:
                    p1spc=(p1spc+diceTotal)-18
                elif (p1spc+diceTotal) != snk1.headSpc:
                    p1spc+=diceTotal
        elif double == True:
            font = pygame.font.SysFont("magneto", 58)
            doubleTxt = font.render(msg2, True, veryblu)
            gameDisplay.blit(doubleTxt, (700,800,300,120))
            if p1spc - diceTotal < 1:
                p1spc = 1
            else:
                if (p1spc - diceTotal) != snk1.headSpc:
                    p1spc -= diceTotal
                elif (p1spc - diceTotal) == snk1.headSpc:
                    p1spc=(p1spc-diceTotal)+snkChng
                    
        return p1spc
                
                
    elif turn == "player2":
        if double == False:
            if (p2spc+diceTotal) > 49:
                pass
            elif (p2spc+diceTotal) == 49:
                p2spc+=diceTotal
                win("Player 2") 
            elif (p2spc+diceTotal) < 49:
                if (p2spc+diceTotal) == snk1.headSpc:
                    p2spc=(p2spc+diceTotal)-18
                elif (p2spc+diceTotal) != snk1.headSpc:
                    p2spc+=diceTotal
        elif double == True:
            font = pygame.font.SysFont("magneto", 58)
            doubleTxt = font.render(msg2, True, veryblu)
            gameDisplay.blit(doubleTxt, (700,800,300,120))
            if p2spc - diceTotal < 1:
                p2spc = 1
            else:
                if (p2spc - diceTotal) != snk1.headSpc:
                    p2spc -= diceTotal
                elif (p2spc - diceTotal) == snk1.headSpc:
                    p2spc=(p2spc-diceTotal)+snkChng
        return p2spc

    
    
    
def win(winner):
    global won
    global winTxt
    font = pygame.font.SysFont("magneto", 48)
    winTxt = font.render((winner+msg3), True, orange)
    won=True




def game_intro(msg1):
    
    intro=True
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
                
        gameDisplay.fill(drkGrn)
        
        
        
        
        bigText = pygame.font.SysFont("magneto",58)
        textSurf, textRect = text_colour((msg1[:-1]), bigText,titlBlu)
        textRect.center = (550, 400)
        gameDisplay.blit(textSurf, textRect)
        
        
        button("Start",black,450,780,200,80,darkerRed,red,ev,"play")
        pygame.display.update()
        clock.tick(15)




def game_loop():
    
    gameExit = False

    
    #counter diameter is 20
    


    
    while not gameExit:
        
        ev=pygame.event.get()

        
        
        for event in ev:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            
        
        gameDisplay.fill(greyBG)
        drawGrid()
        
        
        
        
        snk1.snakeDraw()
        
        
        
        drawCountrs()
        
        if won==False:
            button("Roll",black,450,960,200,80,drkSageGrn,sageGrn,ev,"roll")
            playerTurnBlit()
            
            
        button("Move",black,450,10,200,80,drkSageGrn,sageGrn,ev,"move")
        pygame.draw.rect(gameDisplay, darkerRed, (430,(display_height-420),120,120),5) #dice box
        pygame.draw.rect(gameDisplay, darkerRed, (550,(display_height-420),120,120),5)
        
        
        
        try:
            if hideDice==False:
                gameDisplay.blit(dice1txt, (450,(display_height-425),120,120))
                gameDisplay.blit(dice2txt, (570,(display_height-425),120,120))
        except:
            pass
        try:
            if double:
                gameDisplay.blit(doubleTxt, (700,800,300,120))
            elif won and hideDice and readyToMove==False:
                gameDisplay.blit(winTxt, (700,800,300,120))
                button("Quit",black,100,100,200,80,drkWhitish,whitish,ev,"quit")


        except:
            pass
        


        

        
        pygame.display.update()
        clock.tick(60)
        firstRun=False
 
 
game_intro(msg1)
game_loop()
pygame.quit()
quit()