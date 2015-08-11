import random
import pygame, sys
from pygame.locals import *

class Board:
    gameBoard=[[0 for i in range(0,4)]for j in range(0,4)]
    rowDirection=0
    colDirection=0
    spawnList=[]
    score=0
    over=0
    moves=0
    black = 0, 0, 0
    white = 224,224,224
    fontObj = 0
    board = pygame.image.load("2048_assets/bg.png")
    boardrect = board.get_rect()
    tile_2 = pygame.image.load("2048_assets/2.png")
    tile_4 = pygame.image.load("2048_assets/4.png")
    tile_8 = pygame.image.load("2048_assets/8.png")
    tile_16 = pygame.image.load("2048_assets/16.png")
    tile_32 = pygame.image.load("2048_assets/32.png")
    tile_64 = pygame.image.load("2048_assets/64.png")
    tile_128 = pygame.image.load("2048_assets/128.png")
    tile_256 = pygame.image.load("2048_assets/256.png")
    tile_512 = pygame.image.load("2048_assets/512.png")
    tile_1024 = pygame.image.load("2048_assets/1024.png")
    tile_2048 = pygame.image.load("2048_assets/2048.png")
    tile_4096 = pygame.image.load("2048_assets/4096.png")
    tile_8192 = pygame.image.load("2048_assets/8192.png")
    tile_16384 = pygame.image.load("2048_assets/16384.png")
    tile_32768 = pygame.image.load("2048_assets/32768.png")
    tile_65536 = pygame.image.load("2048_assets/65536.png")
    size = width, height = (410, 470)
    screen = pygame.display.set_mode((410, 470))

    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        pygame.display.set_caption("2048")
        self.fontObj = pygame.font.Font('freesansbold.ttf', 36)
        boardList=[];
        for i in range(0,4):
            for j in range(0,4):
                boardList.append((i,j));
                     
        position=random.randrange(0,len(boardList));
        probability=random.random();
        if(probability>0.8):
            number=4
        else:
            number=2;
        self.gameBoard[boardList[position][0]][boardList[position][1]]=number;
        del boardList[position];

        position=random.randrange(0,len(boardList));
        probability=random.random();
        if(probability>0.8):
            number=4
        else:
            number=2;
        self.gameBoard[boardList[position][0]][boardList[position][1]]=number;
        del boardList[position];

    def printBoard(self):
        self.screen.fill(self.white)
        self.screen.blit(self.board, (self.boardrect[0]+40, self.boardrect[1]+40))
        textSurfaceObj = self.fontObj.render('Score: ' + str(self.score), True, self.black, self.white)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (185,420)
        self.screen.blit(textSurfaceObj, textRectObj)
        for i in range(0, 4):
            for j in range(0, 4):
                if self.gameBoard[i][j] != 0:
                    if (self.gameBoard[i][j] == 2):
                        self.screen.blit(self.tile_2, (i*80 + 50, j*80 + 50))
                    elif (self.gameBoard[i][j] == 4):
                        self.screen.blit(self.tile_4, (i*80 + 50, j*80 + 50))
                    elif (self.gameBoard[i][j] == 8):
                        self.screen.blit(self.tile_8, (i*80 + 50, j*80 + 50))
                    elif (self.gameBoard[i][j] == 16):
                        self.screen.blit(self.tile_16, (i*80 + 50, j*80 + 50))
                    elif (self.gameBoard[i][j] == 32):
                        self.screen.blit(self.tile_32, (i*80 + 50, j*80 + 50))
                    elif (self.gameBoard[i][j] == 64):
                        self.screen.blit(self.tile_64, (i*80 + 50, j*80 + 50))
                    elif (self.gameBoard[i][j] == 128):
                        self.screen.blit(self.tile_128, (i*80 + 50, j*80 + 50))
                    elif (self.gameBoard[i][j] == 256):
                        self.screen.blit(self.tile_256, (i*80 + 50, j*80 + 50))
                    elif (self.gameBoard[i][j] == 512):
                        self.screen.blit(self.tile_512, (i*80 + 50, j*80 + 50))
                    elif (self.gameBoard[i][j] == 1024):
                        self.screen.blit(self.tile_1024, (i*80 + 50, j*80 + 50))
                    elif (self.gameBoard[i][j] == 2048):
                        self.screen.blit(self.tile_2048, (i*80 + 50, j*80 + 50))
                    elif (self.gameBoard[i][j] == 4096):
                        self.screen.blit(self.tile_4096, (i*80 + 50, j*80 + 50))
                    elif (self.gameBoard[i][j] == 8192):
                        self.screen.blit(self.tile_8192, (i*80 + 50, j*80 + 50))
                    elif (self.gameBoard[i][j] == 16384):
                        self.screen.blit(self.tile_16384, (i*80 + 50, j*80 + 50))
                    elif (self.gameBoard[i][j] == 32768):
                        self.screen.blit(self.tile_32768, (i*80 + 50, j*80 + 50))
                    else:
                        self.screen.blit(self.tile_65536, (i*80 + 50, j*80 + 50))
        if self.over == 1:
            textStatus = self.fontObj.render('Game Over', True, self.black)
            textStatusRect = textStatus.get_rect()
            textStatusRect.center = (205,205)
            self.screen.blit(textStatus, textStatusRect)

    #To calculate the score which the sum of all numbers present on the board.
    def calculateScore(self):
        for i in range(0,4):
            for j in range(0,4):
                self.score=self.score+self.gameBoard[i][j];

    def spawnBoard(self):
        self.spawnList=[]
        for i in range(0,4):
            for j in range(0,4):
                if(self.gameBoard[i][j]==0):
                    self.spawnList.append((i,j));
        if(len(self.spawnList)>0):
            position=random.randrange(0,len(self.spawnList));
            probability=random.random();
            if(probability<0.8):
                self.gameBoard[self.spawnList[position][0]][self.spawnList[position][1]]=2;
            else:
                self.gameBoard[self.spawnList[position][0]][self.spawnList[position][1]]=4;

    def gameOver(self):
        self.over=1;
        for i in range(0,4):
            for j in range(0,4):
                if(self.gameBoard[i][j]==0):
                    self.over=0;
                elif(i<3 and j<3):
                    if(self.gameBoard[i][j]==self.gameBoard[i][j+1] or self.gameBoard[i][j]==self.gameBoard[i+1][j]):
                        self.over=0;
                elif(i==3 and j<3):
                    if(self.gameBoard[i][j]==self.gameBoard[i][j+1]):
                        self.over=0
                elif(j==3 and i<3):
                    if(self.gameBoard[i][j]==self.gameBoard[i+1][j]):
                        self.over=0

    def moveLeft(self):
        self.moves=0
        blankRowIndex=0;
        blankColIndex=0;
        blankList=[];
        self.rowDirection=0;
        self.colDirection=-1;
        for i in range(0,4):
            blankRowIndex=i;
            blankList=[];
            for j in range(0,4):
                if(self.gameBoard[i][j]==0):
                    blankList.append(j);
                else:
                    if(len(blankList)>0):
                        self.gameBoard[blankRowIndex][blankList[0]]=self.gameBoard[i][j];
                        self.gameBoard[i][j]=0;
                        del blankList[0];
                        blankList.append(j);
                        self.moves=1
        return self.moves

                                        
    def moveRight(self):
        self.moves=0
        blankRowIndex=0;
        blankColIndex=0;
        blankList=[];
        self.rowDirection=0;
        self.colDirection=1;
        for i in range(0,4):
            blankRowIndex=i;
            blankList=[];
            for j in range(3,-1,-1):
                if(self.gameBoard[i][j]==0):
                    blankList.append(j);
                else:
                    if(len(blankList)>0):
                        self.gameBoard[blankRowIndex][blankList[0]]=self.gameBoard[i][j];
                        self.gameBoard[i][j]=0;
                        del blankList[0];
                        blankList.append(j);
                        self.moves=1
        return self.moves

    def moveUp(self):
        self.moves=0
        blankRowIndex=0;
        blankColIndex=0;
        blankList=[];
        self.rowDirection=-1;
        self.colDirection=0;
        for i in range(0,4):
            blankColIndex=i;
            blankList=[];
            for j in range(0,4):
                if(self.gameBoard[j][i]==0):
                    blankList.append(j);
                else:
                    if(len(blankList)>0):
                        self.gameBoard[blankList[0]][blankColIndex]=self.gameBoard[j][i];
                        self.gameBoard[j][i]=0;
                        del blankList[0];
                        blankList.append(j);
                        self.moves=1
        return self.moves

    def moveDown(self):
        self.moves=0
        blankRowIndex=0;
        blankColIndex=0;
        blankList=[];
        self.rowDirection=1;
        self.colDirection=0;
        for i in range(0,4):
            blankColIndex=i;
            blankList=[];
            for j in range(3,-1,-1):
                if(self.gameBoard[j][i]==0):
                    blankList.append(j);
                else:
                    if(len(blankList)>0):
                        self.gameBoard[blankList[0]][blankColIndex]=self.gameBoard[j][i];
                        self.gameBoard[j][i]=0;
                        del blankList[0];
                        blankList.append(j);
                        self.moves=1
        return self.moves

    def merge(self):
        self.moves=0
        for i in range(0,4):
            if(self.colDirection==-1):
                for j in range(0,4):
                    if(j>0):
                        if(self.gameBoard[i][j]==self.gameBoard[i+self.rowDirection][j+self.colDirection]):
                            if self.gameBoard[i][j] != 0:
                                self.moves=1
                            self.gameBoard[i+self.rowDirection][j+self.colDirection]=self.gameBoard[i+self.rowDirection][j+self.colDirection]*2;
                            self.score=self.score+ self.gameBoard[i+self.rowDirection][j+self.colDirection]
                            self.gameBoard[i][j]=0;                                               
            elif(self.colDirection==1):
                for j in range(3,-1,-1):
                    if(j<3):
                        if(self.gameBoard[i][j]==self.gameBoard[i+self.rowDirection][j+self.colDirection]):
                            if self.gameBoard[i][j] != 0:
                                self.moves=1
                            self.gameBoard[i+self.rowDirection][j+self.colDirection]=self.gameBoard[i+self.rowDirection][j+self.colDirection]*2;
                            self.score=self.score+self.gameBoard[i+self.rowDirection][j+self.colDirection];
                            self.gameBoard[i][j]=0;
            elif(self.rowDirection==-1):
                for j in range(0,4):
                    if(j>0):
                        if(self.gameBoard[j][i]==self.gameBoard[j+self.rowDirection][i+self.colDirection]):
                            if self.gameBoard[j][i] != 0:
                                self.moves=1
                            self.gameBoard[j+self.rowDirection][i+self.colDirection]=self.gameBoard[j+self.rowDirection][i+self.colDirection]*2;
                            self.score=self.score+self.gameBoard[j+self.rowDirection][i+self.colDirection];
                            self.gameBoard[j][i]=0;
            elif(self.rowDirection==1):
                for j in range(3,-1,-1):
                    if(j<3):
                        if(self.gameBoard[j][i]==self.gameBoard[j+self.rowDirection][i+self.colDirection]):
                            if self.gameBoard[j][i] != 0:
                                self.moves=1
                            self.gameBoard[j+self.rowDirection][i+self.colDirection]=self.gameBoard[j+self.rowDirection][i+self.colDirection]*2;
                            self.score=self.score+self.gameBoard[j+self.rowDirection][i+self.colDirection];
                            self.gameBoard[j][i]=0;
        return self.moves
                                        

##END of CLASS
flag=0;
g=Board();
g.printBoard();
gamepad = pygame.joystick.Joystick(0)
gamepad.init()
# right = str(chr(47))
# left = str(chr(143))
# up = str(chr(31))
# down = str(chr(79))
while(1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        if(flag==0):
            if(gamepad.get_button(2) == True):
                if g.moveRight() + g.merge() > 0:
                    g.moveRight()
                    g.spawnBoard();
                g.gameOver();
                g.printBoard();
                flag=2;
            if(gamepad.get_button(0) == True):
                if g.moveLeft() + g.merge() > 0:
                    g.moveLeft()
                    g.spawnBoard();
                g.gameOver();
                g.printBoard();
                flag=4;
            if(gamepad.get_button(3) == True):
                if g.moveUp() + g.merge() > 0:
                    g.moveUp()
                    g.spawnBoard();
                g.gameOver();
                g.printBoard();
                flag=3;
            if(gamepad.get_button(1) == True):
                if g.moveDown() + g.merge() > 0:
                    g.moveDown()
                    g.spawnBoard();
                g.gameOver();
                g.printBoard();
                flag=1;
        if((gamepad.get_button(0) == False and flag == 4) or (gamepad.get_button(1) == False and flag == 1) 
            or (gamepad.get_button(2) == False and flag == 2) or (gamepad.get_button(3) == False and flag == 3)):
            flag = 0;
        pygame.display.flip()            
        if(g.over==1 and gamepad.get_button(5) == True):
            g.score = 0
            g.over = 0
            for i in range(0,4):
                for j in range(0,4):
                    g.gameBoard[i][j] = 0
            g.__init__()
            g.printBoard()