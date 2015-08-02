class Board:
	gameBoard=[[0 for i in range(0,4)]for j in range(0,4)]
        rowDirection=0;
        colDirection=0;
	def __init__(self):
                self.gameBoard[0][0]=2;
                self.gameBoard[0][3]=2;
                self.gameBoard[1][1]=4;
                self.gameBoard[1][3]=4;
		print 'Board initialised'

	def printBoard(self):
		for i in range(0,4):
			for j in range(0,4):
				print self.gameBoard[i][j],'|',
			print '\n________________'

	def updateBoard(self):
		pass

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

	def moveUp():
		pass

	def moveDown():
		pass

        def merge(self):
                for i in range(0,4):
                        if(self.colDirection==-1):
                                for j in range(0,4):
                                        if(j>0):
                                                if(self.gameBoard[i][j]==self.gameBoard[i+self.rowDirection][j+self.colDirection]):
                                                        self.gameBoard[i+self.rowDirection][j+self.colDirection]=self.gameBoard[i+self.rowDirection][j+self.colDirection]*2;
                                                        self.gameBoard[i][j]=0;
                        elif(self.colDirection==1):
                                for j in range(3,-1,-1):
                                        if(j<3):
                                                if(self.gameBoard[i][j]==self.gameBoard[i+self.rowDirection][j+self.colDirection]):
                                                        self.gameBoard[i+self.rowDirection][j+self.colDirection]=self.gameBoard[i+self.rowDirection][j+self.colDirection]*2;
                                                        self.gameBoard[i][j]=0;
                                        

g=Board();
g.printBoard();
r=input('Enter');
if(r==1):
        g.moveRight();
        g.merge();
g.printBoard();
