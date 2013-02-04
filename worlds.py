from utils.math import lerp
from utils.image import load_rgb

SCREEN_W = 640
SCREEN_H = 480

class Word(object):

	def __init__(self, character=None, bgimage=None):
		self.character = character
		self.bgimage = bgimage
		self.height = 480
		self.width = 1200

		self.posx = 0
		self.posy = 0

		self.maxx = self.width - SCREEN_W
		self.maxy = self.height - SCREEN_H

	def update(self, time):
		fx = self.character.posx / self.width
		fy = self.character.posy / self.height
		
		self.posx = lerp(0, self.width, fx)
		self.posy = lerp(0, self.height, fy)

		if self.posx >= self.maxx:
			self.posx = self.maxx
		if self.posx <= 0:
			self.posx = 0

	def draw(self, screen):
		screen.blit(self.bgimage, (-self.posx, -self.posy))

class SimpleWorld(Word):

	def __init__(self, character):
		super(SimpleWorld, self).__init__(
			character, load_rgb('assets/images/world/simple/simple.png')
		)