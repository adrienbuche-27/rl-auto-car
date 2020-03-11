import pygame
from pygame.locals import *
from set_up import *
from player import *

"""
First steps learning things about pygame functionnalities

This file will contains multiple 'main' method, each one exploring the diverse
aspects that pygame package has to offer
"""

def main():
	""" Intro to keyboard interaction and screen changing colors """
	# For frame rate control
	clock = pygame.time.Clock()
	# Initialisation of the pygame window
	pygame.init()
	screen = pygame.display.set_mode((400, 400))

	# Params
	is_blue = False
	back_color = (0, 128, 255)

	# While loop to run the "application"
	while 1:

		for event in pygame.event.get():
			# Break out of the loop if "close"/esc is pressed
			if event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				return

			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				# space bar is pressed
				is_blue = not is_blue

		if is_blue: 
			back_color = (0, 128, 255)
		else: 
			back_color = (255, 100, 0)

		screen.fill(back_color)
		pygame.display.flip()
		clock.tick(30)

	pygame.quit()


def main_2():

	clock = pygame.time.Clock()

	pygame.init()

	gameDisplay = pygame.display.set_mode((800, 800))
	pygame.display.set_caption('Test')
	gameDisplay_limit = gameDisplay.get_rect()

	running = True

	player = Player(50,(500, 500))

	while running:
		gameDisplay.fill(colors['black'])

		for event in pygame.event.get():
			# Break out of the loop if "close"/esc is pressed
			if event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				running = False

		player.move_joystick()
		player.draw_player(gameDisplay)
		print(player.angle)
		player.draw_lines(gameDisplay)
		pygame.display.flip()
		clock.tick(30)

	pygame.quit()



if __name__ == '__main__':
	main_2()