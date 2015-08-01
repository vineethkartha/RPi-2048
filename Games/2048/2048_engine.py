class Board:
	gameBoard=[[0 for i in range(0,4)]for j in range(0,4)]
        
	def __init__(self):
                self.gameBoard[0][2]=2;
                self.gameBoard[0][3]=2;
                self.gameBoard[1][1]=4;
                self.gameBoard[1][3]=4;
		print 'Board initialised'

	def printBoard(self):
		for i in range(0,4):
			for j in range(0,4):
				print self.gameBoard[i][j],

			print '\n'

	def updateBoard(self):
		pass

	def moveLeft(self):
                blankRowIndex=0;
                blankColIndex=0;
                isMarked=0;
		for i in range(0,4):
                        blankRowIndex=i;
                        isMarked=0;
                        for j in range(0,4):
                                if(self.gameBoard[blankRowIndex][blankColIndex]==0 and isMarked==0):
                                        isMarked=1;
                                else:
                                        self.gameBoard[blankRowIndex][blankColIndex]=self.gameBoard[i][j];
                                        self.gameBoard[i][j]=0;
                                        blankRowIndex=i;
                                        while(blankColIndex<4):
                                                if(self.gameBoard[blankRowIndex][blankColIndex]!=0):
                                                        blankColIndex=blankColIndex+1;
                                                else:
                                                        break;
	def moveRight():
		pass

	def moveUp():
		pass

	def moveDown():
		pass


g=Board();
g.printBoard();
r=input('Enter');
if(r==1):
        g.moveLeft();
g.printBoard();
