#!/usr/bin/env python

import pygame
from pygame.locals import *

from globals import MAXFPS, SCREENSIZE

from worlds import SimpleWorld
from cameras import Camera
from characters import Megaman

def main():
	pygame.init()

	# The game clock
	clock = pygame.time.Clock()

	# The game screen
	screen = pygame.display.set_mode(
		SCREENSIZE, 0, 32
	)
	pygame.display.set_caption('Hello, World!')

	running = True
	frames = 0
	count = 0
	time = 0

	mm = Megaman()
	cm = Camera(mm)
	sw = SimpleWorld(cm)

	while running:
		for event in pygame.event.get():
			if event.type == QUIT:
				running = False
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					running = False
			elif event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					mx, my = event.pos

		time = clock.tick(MAXFPS)
		
		count += time
		frames += 1
		if count >= 1000:
##                        print '%d (%d) FPS' % (clock.get_fps(), frames)
			count = 0
			frames = 0
			
		screen.fill((0,0,0))

		sw.update(time)
		sw.draw(screen, cm)

		mm.update(time)
		mm.draw(screen, cm)

		pygame.display.update()

	pygame.quit()

if __name__ == '__main__':
	main()
