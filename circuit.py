import pandas as pd
import numpy as np
import pygame
from PIL import Image, ImageOps
from set_up import *
from player import *

def main():

	clock = pygame.time.Clock()

	pygame.init()

	# for i in range(1,6):
	# 	img, img_np, _ = load_image('circuits/first_try0{}.png'.format(i))
	img, img_np, _ = load_image('circuits/first_try06.png')
	img_inv, img_inv_np, img_size = invert_image(img)
	center, dims = find_start_ind(img)
	sl , middle = find_start(img_inv_np, center, dims)

	gameDisplay = pygame.display.set_mode((img_size[1], img_size[0]))
	pygame.display.set_caption('Reinforcement Learning : Circuit')
	gameDisplay_limit = gameDisplay.get_rect()
	surf = pygame.surfarray.make_surface(img_inv_np)
	
	running = True
	player = Player(50, middle[1], 90, gameDisplay_limit)

	while running:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				running = False

		gameDisplay.blit(surf, (0, 0))

		# player.move_arrows()
		player.move_joystick()
		player.draw_player(gameDisplay)
		# print("Surf :" , surf.get_at((int(player.x), int(player.y))))
		player.draw_lines(gameDisplay)
		pygame.display.flip()
		clock.tick(30)
		if player.out_of_boundaries():
			running = False

	pygame.quit()

if __name__ == '__main__':
	main()
