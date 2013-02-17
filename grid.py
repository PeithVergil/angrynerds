import math
import pygame
from pygame import Rect

from utils.image import load_frames

class Grid(object):

	def __init__(self, rows, cols, size):
		self.rows = rows
		self.cols = cols
		self.size = size

	def screen(self, x, y):
		'''Convert screen coordinates to grid coordinates'''
		return (
			int(math.floor(y / self.size)),
			int(math.floor(x / self.size)),
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

	def select(self, x1, y1, x2, y2):
		'''Get all cells inside the rectangle'''
		row1, col1 = self.screen(x1, y1)
		row2, col2 = self.screen(x2, y2)

		for row in xrange(row1, row2+1):
			for col in xrange(col1, col2+1):
				yield (row, col)

	@property
	def width(self):
		return self.cols * self.size

	@property
	def height(self):
		return self.rows * self.size

	@property
	def bounds(self):
		return Rect(
			0, 0, self.width, self.height
		)

	def __len__(self):
		return self.rows * self.cols

class Tile(pygame.sprite.Sprite):
	def __init__(self, image, rect, name=None, solid=False):
		self.solid = solid # If true, perform collision detection
		self.image = image
		self.rect = rect
		self.name = name

	def draw(self, screen, pos):
		screen.blit(self.image, pos)

class TileMap(Grid):

	def __init__(self, world, tiles, gmap):
		self.world = world

		# The list of tiles to look-up to
		self.tiles = tiles
		# The grid map look-up table
		self.gmap = gmap

		rows = len(gmap)
		try:
			cols = len(gmap[0])
		except IndexError:
			cols = 0

		try:
			size = tiles[0].rect.width
		except IndexError:
			size = 0

		super(TileMap, self).__init__(rows, cols, size)

	def lookup(self, row, col):
		try:
			tile = self.tiles[self.gmap[row][col]]
		except IndexError:
			return None
		else:
			return tile

	def get_tile(self, x, y):
		r, c = self.screen(x, y)
		tile = self.lookup(r, c)

		return tile

	def update(self, time):
		camera = self.world.camera

		x, y = pygame.mouse.get_pos()
		# Convert mouse position from
		# screen space to world space
		x, y = self.screen(
			x + camera.rect.x,
			y + camera.rect.y,
		)

		self.cpos = self.grid(x, y)

	def draw(self, screen):
		camera = self.world.camera

		# Get all tiles inside the camera's bounding box
		for row, col in self.select(camera.rect.x, camera.rect.y, camera.rect.right, camera.rect.bottom):
			# Convert grid coordinates to world coordinates
			x, y, w, h = self.grid(row, col)

			tile = self.lookup(row, col)
			if tile:
				# Convert world coordinates to screen coordinates
				tile.draw(screen, camera.to_screen(x, y))

			# FOR DEBUGGING:
			#
			x, y = camera.to_screen(x, y)

			# Draw the grid
			# pygame.draw.rect(screen, (255,0,0), (x, y, w, h), 1)

		# Draw the mouse cursor
		pygame.draw.rect(screen, (0,255,0), (
	        self.cpos[0] - camera.rect.x,
	        self.cpos[1] - camera.rect.y,
	        self.cpos[2],
	        self.cpos[3],
	    ))

class SimpleTileMap(TileMap):

	def __init__(self, world):
		images = load_frames('assets/images/gridmap', 4)

		super(SimpleTileMap, self).__init__(world,
			[
				Tile(images[0], images[0].get_rect(), 'sky',),
				Tile(images[1], images[1].get_rect(), 'grass', True),
				Tile(images[2], images[2].get_rect(), 'dirt', True),
				Tile(images[3], images[3].get_rect(), 'brick', True),
			],
			(
	            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
	            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
	            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
	            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,0,0,0),
	            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
	            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3),
	            (0,0,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
	            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,0),
	            (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
	            (3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
	            (1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),
        	)
		)