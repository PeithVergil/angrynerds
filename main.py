#!/usr/bin/env python

import pygame
from pygame.locals import *

from worlds import SimpleWorld
from characters import Megaman

SCREEN_W = 640
SCREEN_H = 480

def main():
	FPS = 60

	pygame.init()

	# The game clock
	clock = pygame.time.Clock()

	# The game screen
	screen = pygame.display.set_mode(
		(SCREEN_W, SCREEN_H), 0, 32
	)
	pygame.display.set_caption('Hello, World!')

	running = True
	frames = 0
	count = 0
	time = 0

	mm = Megaman()
	sw = SimpleWorld(mm)

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

		time = clock.tick(FPS)

		count += time
		frames += 1
		if count >= 1000:
			# print '%d FPS' % frames
			count = 0
			frames = 0
			
		screen.fill((0,0,0))

		sw.update(time)
		sw.draw(screen)

		mm.update(time)
		mm.draw(screen)

		pygame.display.update()

	pygame.quit()

if __name__ == '__main__':
	main()