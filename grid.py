import math

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

	def get(self, row, col):
		'''Convert grid coordinates to screen coordinates'''
		return (
			col * self.size,
			row * self.size,
			self.size,
			self.size,
		)

	def up(self, row, col):
		'''Get top neighbor'''
		return self.get(row-1, col)

	def down(self, row, col):
		'''Get bottom neighbor'''
		return self.get(row+1, col)

	def left(self, row, col):
		'''Get left neighbor'''
		return self.get(row, col-1)

	def right(self, row, col):
		'''Get right neighbor'''
		return self.get(row, col+1)

	def cells(self):
		for row in xrange(self.rows):
			for col in xrange(self.cols):
				yield self.get(row, col)

	def __len__(self):
		return self.rows * self.cols