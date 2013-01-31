#!/usr/bin/env python

import sys

import pygame
from pygame.locals import *

from characters import Megaman

def main():
	FPS = 60

	pygame.init()

	# The game clock
	clock = pygame.time.Clock()

	# The game screen
	screen = pygame.display.set_mode(
		(640, 480), 0, 32
	)
	pygame.display.set_caption('Hello, World!')

	running = True
	frames = 0
	count = 0
	time = 0

	mm = Megaman()

	bgimage = pygame.image.load('/home/pvergil/Pictures/webdesigns/scherf.jpg').convert()
	image = pygame.image.load('/home/pvergil/Desktop/PeterMissen/Images/PNGs/envelope.png').convert_alpha()

	mx, my = (0, 0)

	while running:
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					sys.exit()
			elif event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					mx, my = event.pos

		time = clock.tick(FPS)

		count += time
		frames += 1
		if count >= 1000:
			print '%d FPS' % frames
			count = 0
			frames = 0

		screen.blit(bgimage, (0, 0))

		mm.update(time)
		mm.draw(screen)

		# x, y = pygame.mouse.get_pos()
		# screen.blit(image, (x, y))

		if mx and my:
			screen.blit(image, (mx, my))

		pygame.display.update()

	pygame.quit()

if __name__ == '__main__':
	main()