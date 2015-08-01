class Board:
	gameBoard=[[0 for i in range(0,4)]for j in range(0,4)]
        
	def __init__(self):
                self.gameBoard[0][0]=2;
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
                blankList=[];
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
