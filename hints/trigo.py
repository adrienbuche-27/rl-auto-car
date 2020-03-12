import math
import numpy as np
import pygame
from pygame.locals import *

colors = {'black':(0,0,0),
        'white':(255,255,255),
        'gray':(128,128,128),
        'aqua':(0,128,128),
        'navy blue':(0,0,128),
        'green':(0,255,0),
        'orange':(255,165,0),
        'yellow':(255,255,0),
        'red':(255,0,0),
        'blue':(0,0,255)}

def in_circle(center, r, pos, thresh):
	if sum((pos - center)**2) <= (r+thresh)**2 and sum((pos - center)**2) >= (r-thresh)**2:
		return True
	else:
		return False

def distance_point_to_line(P0, P1, P2):
	x0, y0 = P0
	x1, y1 = P1
	x2, y2 = P2
	return ((y2-y1)*x0 - (x2-x1)*y0 + x2*y1 - x1*y2)/(math.sqrt((y2-y1)**2 + (x2-x1)**2))

def full_circle_degree(dv, dh):
	if dv >= 0 and dh > 0: # Q1
		return "Q1" , (math.atan(dv/dh)*180)/math.pi
	elif dh == 0:
		if dv < 0 :
			return "Q3", 270
		else:
			return "Q1", 90
	elif dv <= 0 and dh <= 0: # Q3
		return "Q3" , (math.atan(dv/dh) + math.pi)*180/math.pi
	elif dh <= 0 and dv > 0: # Q2
		return "Q2" , (180 + ((math.atan(dv/dh)*180)/math.pi))
	else: # Q4
		return "Q4" , (360 + (math.atan(dv/dh)*180/math.pi))

def metrics(dangle, r):
	rangle = dangle*math.pi/180
	return np.round(np.array((math.cos(rangle), math.sin(rangle)))*r)


def main():
	""" Intro to keyboard interaction and screen changing colors """
	# For frame rate control
	clock = pygame.time.Clock()
	# Initialisation of the pygame window
	pygame.init()
	screen = pygame.display.set_mode((400, 400))
	center = np.array([200,200])
	x0, y0 = center
	r = 150
	last_pos = None
	last_angle = 0
	cs = np.array([0,0])

	font = pygame.font.Font('freesansbold.ttf', 20)  
	text = font.render('Trigonometric Circle', True, colors['white']) 
	textRect = text.get_rect()  
	textRect.center = (200, 25)
	Pi = math.pi

	flag = False
	# While loop to run the "application"
	while 1:

		screen.fill((0,0,0))
		if not flag:
			pygame.draw.circle(screen, colors['blue'], center, r, 6)
			for x in range(0,360,15):
				adj = math.cos(x*Pi/180) * r
				opp = math.sin(x*Pi/180) * r
				pygame.draw.line(screen, colors['green'], (x0, y0), (x0+adj, y0+opp), 2)
		else:
			pygame.draw.circle(screen, colors['blue'], center, r, 6)
			pygame.draw.line(screen, colors['orange'], (x0-r, y0), (x0+r, y0), 2)
			pygame.draw.line(screen, colors['orange'], (x0, y0-r), (x0, y0+r), 2)
			# pygame.draw.rect(screen, colors['yellow'], [100,100,200,200], 2)

		screen.blit(text, textRect)

		for event in pygame.event.get():
			# Break out of the loop if "close"/esc is pressed
			if event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				return
			if flag:
				if event.type == pygame.MOUSEMOTION and event.buttons == (1, 0, 0):
					if in_circle(center, r, event.pos, 5):
						last_pos = event.pos
						dv = distance_point_to_line(last_pos, (x0-r, y0), (x0+r, y0))
						dh = distance_point_to_line(last_pos, (x0, y0-r), (x0, y0+r))
						quadrant, last_angle = full_circle_degree(dv,dh)
						cs = metrics(last_angle, r)
						text_angle = font.render('Theta : {}'.format(np.round(last_angle, 2)), True, colors['white']) 
						textRect_angle = text_angle.get_rect()  
						textRect_angle.center = (200, 375) 
		if flag:
			if last_pos is not None:
				pygame.draw.circle(screen, colors['red'], last_pos, 5)
				pygame.draw.circle(screen, colors['green'], (x0, y0-cs[1]), 2)
				pygame.draw.circle(screen, colors['aqua'], (x0+cs[0],y0), 2)
				pygame.draw.line(screen, colors['green'], (x0, y0-cs[1]), last_pos, 2)
				pygame.draw.line(screen, colors['aqua'], (x0+cs[0],y0), last_pos, 2)
				pygame.draw.line(screen, colors['red'], center, last_pos, 2)
				screen.blit(text_angle, textRect_angle)
				pygame.draw.arc(screen, colors['yellow'], [100,100,200,200], 0, last_angle*math.pi/180, 2)

		pygame.display.flip()
		clock.tick(30)

	pygame.quit()

if __name__ == '__main__':
	main()