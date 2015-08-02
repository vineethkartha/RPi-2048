import random
class Board:
	gameBoard=[[0 for i in range(0,4)]for j in range(0,4)]
        rowDirection=0;
        colDirection=0;
        spawnList=[];
        score=0;
	def __init__(self):
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
                
		print 'Board initialised'

	def printBoard(self):
		for i in range(0,4):
			for j in range(0,4):
				print self.gameBoard[i][j],'|',
			print '\n---------------'
                print 'score:  ',self.score;

        #To calculate the score which the sum of all numbers present on the board.
        def calculateScore(self):
                for i in range(0,4):
                        for j in range(0,4):
                                self.score=self.score+self.gameBoard[i][j];

                                
	def spawnBoard(self):
                self.spawnList=[];
                for i in range(0,4):
                        for j in range(0,4):
                                if(self.gameBoard[i][j]==0):
                                        self.spawnList.append((i,j));

                position=random.randrange(0,len(self.spawnList));
		probability=random.random();
                if(probability<0.8):
                        self.gameBoard[self.spawnList[position][0]][self.spawnList[position][1]]=2;
                else:
                        self.gameBoard[self.spawnList[position][0]][self.spawnList[position][1]]=4;

	def moveLeft(self):
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
                                        
	def moveRight(self):
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

	def moveUp(self):
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

	def moveDown(self):
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

        def merge(self):
                for i in range(0,4):
                        if(self.colDirection==-1):
                                for j in range(0,4):
                                        if(j>0):
                                                if(self.gameBoard[i][j]==self.gameBoard[i+self.rowDirection][j+self.colDirection]):
                                                        self.gameBoard[i+self.rowDirection][j+self.colDirection]=self.gameBoard[i+self.rowDirection][j+self.colDirection]*2;
                                                        self.score=self.score+ self.gameBoard[i+self.rowDirection][j+self.colDirection]
                                                        self.gameBoard[i][j]=0;
                                                        
                        elif(self.colDirection==1):
                                for j in range(3,-1,-1):
                                        if(j<3):
                                                if(self.gameBoard[i][j]==self.gameBoard[i+self.rowDirection][j+self.colDirection]):
                                                        self.gameBoard[i+self.rowDirection][j+self.colDirection]=self.gameBoard[i+self.rowDirection][j+self.colDirection]*2;
                                                        self.score=self.score+self.gameBoard[i+self.rowDirection][j+self.colDirection];
                                                        self.gameBoard[i][j]=0;
                        elif(self.rowDirection==-1):
                                for j in range(0,4):
                                        if(j>0):
                                                if(self.gameBoard[j][i]==self.gameBoard[j+self.rowDirection][i+self.colDirection]):
                                                        self.gameBoard[j+self.rowDirection][i+self.colDirection]=self.gameBoard[j+self.rowDirection][i+self.colDirection]*2;
                                                        self.score=self.score+self.gameBoard[j+self.rowDirection][i+self.colDirection];
                                                        self.gameBoard[j][i]=0;
                        elif(self.rowDirection==1):
                                for j in range(3,-1,-1):
                                        if(j<3):
                                                if(self.gameBoard[j][i]==self.gameBoard[j+self.rowDirection][i+self.colDirection]):
                                                        self.gameBoard[j+self.rowDirection][i+self.colDirection]=self.gameBoard[j+self.rowDirection][i+self.colDirection]*2;
                                                        self.score=self.score+self.gameBoard[j+self.rowDirection][i+self.colDirection];
                                                        self.gameBoard[j][i]=0;
                                        



g=Board();
g.printBoard();
#r=input('Enter');
while(1):
        r=input('Enter');
        if(r==1):
                g.moveRight();
                g.merge();
                g.moveRight();
                g.spawnBoard();
        if(r==2):
                g.moveLeft();
                g.merge();
                g.moveLeft();
                g.spawnBoard();
        if(r==3):
                g.moveUp();
                g.merge();
                g.moveUp();
                g.spawnBoard();
        if(r==4):
                g.moveDown();
                g.merge();
                g.moveDown();
                g.spawnBoard();
        if(r==0):
                break;
        g.printBoard();
