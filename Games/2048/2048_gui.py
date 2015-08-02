import pygame, sys
from pygame.locals import *

pygame.init()
size = width, height = 330, 330
black = 0, 0, 0
tile_array = [[0 for i in range(0, 4)] for j in range(0,4)]
tile_array[0][0] = 2;
tile_array[0][1] = 4;
tile_array[0][2] = 8;
tile_array[0][3] = 16;
tile_array[1][0] = 32;
tile_array[1][1] = 64;
tile_array[1][2] = 128;
tile_array[1][3] = 256;
tile_array[2][0] = 512;
tile_array[2][1] = 1024;
tile_array[2][2] = 2048;
tile_array[2][3] = 4096;
tile_array[3][0] = 8192;
tile_array[3][1] = 16384;
tile_array[3][2] = 32768;
tile_array[3][3] = 65536;

screen = pygame.display.set_mode(size)

board = pygame.image.load("bg.png")
tile_2 = pygame.image.load("2.png")
tile_4 = pygame.image.load("4.png")
tile_8 = pygame.image.load("8.png")
tile_16 = pygame.image.load("16.png")
tile_32 = pygame.image.load("32.png")
tile_64 = pygame.image.load("64.png")
tile_128 = pygame.image.load("128.png")
tile_256 = pygame.image.load("256.png")
tile_512 = pygame.image.load("512.png")
tile_1024 = pygame.image.load("1024.png")
tile_2048 = pygame.image.load("2048.png")
tile_4096 = pygame.image.load("4096.png")
tile_8192 = pygame.image.load("8192.png")
tile_16384 = pygame.image.load("16384.png")
tile_32768 = pygame.image.load("32768.png")
tile_65536 = pygame.image.load("65536.png")
boardrect = board.get_rect()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		screen.fill(black)
		screen.blit(board, boardrect)
		for i in range(0, 4):
			for j in range(0, 4):
				if tile_array[i][j] != 0:
					if (tile_array[i][j] == 2):
						screen.blit(tile_2, (i*80 + 10, j*80 + 10))
					elif (tile_array[i][j] == 4):
						screen.blit(tile_4, (i*80 + 10, j*80 + 10))
					elif (tile_array[i][j] == 8):
						screen.blit(tile_8, (i*80 + 10, j*80 + 10))
					elif (tile_array[i][j] == 16):
						screen.blit(tile_16, (i*80 + 10, j*80 + 10))
					elif (tile_array[i][j] == 32):
						screen.blit(tile_32, (i*80 + 10, j*80 + 10))
					elif (tile_array[i][j] == 64):
						screen.blit(tile_64, (i*80 + 10, j*80 + 10))
					elif (tile_array[i][j] == 128):
						screen.blit(tile_128, (i*80 + 10, j*80 + 10))
					elif (tile_array[i][j] == 256):
						screen.blit(tile_256, (i*80 + 10, j*80 + 10))
					elif (tile_array[i][j] == 512):
						screen.blit(tile_512, (i*80 + 10, j*80 + 10))
					elif (tile_array[i][j] == 1024):
						screen.blit(tile_1024, (i*80 + 10, j*80 + 10))
					elif (tile_array[i][j] == 2048):
						screen.blit(tile_2048, (i*80 + 10, j*80 + 10))
					elif (tile_array[i][j] == 4096):
						screen.blit(tile_4096, (i*80 + 10, j*80 + 10))
					elif (tile_array[i][j] == 8192):
						screen.blit(tile_8192, (i*80 + 10, j*80 + 10))
					elif (tile_array[i][j] == 16384):
						screen.blit(tile_16384, (i*80 + 10, j*80 + 10))
					elif (tile_array[i][j] == 32768):
						screen.blit(tile_32768, (i*80 + 10, j*80 + 10))
					else:
						screen.blit(tile_65536, (i*80 + 10, j*80 + 10))
	pygame.display.flip()