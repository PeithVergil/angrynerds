class Grid(object):

	def __init__(self, rows, cols, size):
		self.rows = rows
		self.cols = cols
		self.size = size

	def get(self, row, col):
		return (
			col * self.size,
			row * self.size,
			self.size,
			self.size,
		)

	def up(self, row, col):
		return self.get(row-1, col)

	def down(self, row, col):
		return self.get(row+1, col)

	def left(self, row, col):
		'''Get left neighbor'''
		return self.get(row, col-1)

	def right(self, row, col):
		'''Get right neighbor'''
		return self.get(row, col+1)

	def blocks(self):
		for row in xrange(self.rows):
			for col in xrange(self.cols):
				yield self.get(row, col)