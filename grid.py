import math
import pygame

from utils.image import load_frames

class Grid(object):

	def __init__(self, rows, cols, size):
		self.rows = rows
		self.cols = cols
		self.size = size

	def screen(self, x, y):
		'''Convert screen coordinates to grid coordinates'''
		return (
			int(math.floor(x / self.size)),
			int(math.floor(y / self.size)),
		)

	def grid(self, row, col):
		'''Convert grid coordinates to screen coordinates'''
		return (
			col * self.size,
			row * self.size,
			self.size,
			self.size,
		)

	def up(self, row, col):
		'''Get top neighbor'''
		return self.grid(row-1, col)

	def down(self, row, col):
		'''Get bottom neighbor'''
		return self.grid(row+1, col)

	def left(self, row, col):
		'''Get left neighbor'''
		return self.grid(row, col-1)

	def right(self, row, col):
		'''Get right neighbor'''
		return self.grid(row, col+1)

	def cells(self):
		for row in xrange(self.rows):
			for col in xrange(self.cols):
				yield self.grid(row, col)

	def width(self):
		return self.cols * self.size

	def height(self):
		return self.rows * self.size

	def __len__(self):
		return self.rows * self.cols

class GridMap(Grid):

    def __init__(self, world, size, gmap, imgs):
    	self.world = world

        # The list of images to look-up to
        self.imgs = imgs
        # The grid map look-up table
        self.gmap = gmap

        rows = len(gmap)
        cols = len(gmap[0])

        super(GridMap, self).__init__(rows, cols, size)

    def lookup(self, row, col):
        return self.imgs[self.gmap[row][col]]

    def draw(self, screen):
    	camera = self.world.camera

        for row in xrange(self.rows):
            for col in xrange(self.cols):
            	# Get tile coordinates
				pos = self.grid(row, col)

				# From world to screen coordinates
				x, y = camera.to_screen(pos[0], pos[1])

				tile = self.lookup(row, col)
				tile.rect.x = x
				tile.rect.y = y

				tile.draw(screen)

				# FOR DEBUGGING:
				# Draw the grid
				pygame.draw.rect(screen, (255,0,0), (
					x, y, self.size, self.size,
				), 1)

class Tile(pygame.sprite.Sprite):
	def __init__(self, image, rect, name=None):
		self.image = image
		self.rect = rect
		self.name = name

	def draw(self, screen):
		screen.blit(self.image, self.rect)

class SampleGridMap(GridMap):

	def __init__(self, world):
		images = load_frames('assets/images/gridmap', 4)

		tiles = [
			Tile(images[0], images[0].get_rect(), 'sky'),
			Tile(images[1], images[1].get_rect(), 'grass'),
			Tile(images[2], images[2].get_rect(), 'dirt'),
			Tile(images[3], images[3].get_rect(), 'brick'),
		]

		super(SampleGridMap, self).__init__(world, 64, (
            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3),
            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
            (0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,0),
            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
            (1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),
        ), tiles)