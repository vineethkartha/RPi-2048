class Board:
	gameBoard=[[0 for i in range(0,4)]for j in range(0,4)]
	def __init__(self):
		print 'Board initialised'

	def printBoard(self):
		for i in range(0,4):
			for j in range(0,4):
				print self.gameBoard[i][j]

			print '\n'

	def updateBoard(self):
		pass

	def moveLeft():
		pass

	def moveRight():
		pass

	def moveUp():
		pass

	def moveDown():
		pass


g=Board();
g.printBoard();