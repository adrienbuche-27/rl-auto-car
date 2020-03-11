import pandas as pd
import numpy as np
import pygame
from PIL import Image, ImageOps
from set_up import *
from player import *

def main():

	clock = pygame.time.Clock()

	pygame.init()

	img, img_size = load_image_invert('circuits/first_try01.png')
	# search_start(img)
	
	gameDisplay = pygame.display.set_mode((img_size[1], img_size[0]))
	pygame.display.set_caption('Reinforcement Learning : Circuit')
	gameDisplay_limit = gameDisplay.get_rect()
	surf = pygame.surfarray.make_surface(img)

	running = True
	player = Player(50,(500, 500))

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		# pressed = pygame.key.get_pressed()
		# if sum(pressed) != 0:
		# 	player.move_arrows(pressed)	

		gameDisplay.blit(surf, (0, 0))
		# player.move_arrows()
		player.move_joystick()
		player.draw_player(gameDisplay)
		# print(player.x,player.y)
		player.draw_lines(gameDisplay)
		pygame.display.flip()
		clock.tick(30)

	pygame.quit()

if __name__ == '__main__':
	main()
