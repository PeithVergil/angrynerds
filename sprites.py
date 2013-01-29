from pygame.image import load
from pygame.sprite import Sprite

from states import StateMachine

class ImageSet(object):

	def __init__(self, images, maxtime=5000):
		self.interval = maxtime/len(images)
		self.maxtime = maxtime
		self.images = images
		self.index = 0
		self.time = 0

	def numframes(self):
		'''Get the total number of frames'''
		return len(self.images)

	def currframe(self):
		'''Get the current frame'''
		return self.images[self.index]

	def next(self):
		'''Jump to next frame'''
		self.index += 1
		if self.index == self.numframes():
			self.index = 0

	def prev(self):
		'''Jump to previous frame'''
		self.index -= 1
		if self.index < 0:
			self.index = self.numframes() - 1

	def update(self, time):
		self.time += time

		if self.time >= self.interval:
			self.time = 0
			self.next()

	def draw(self, screen):
		screen.blit(self.currframe(), (0, 0))

class AnimatedSprite(Sprite):

	def __init__(self):
		super(AnimatedSprite, self).__init__()
		
		self.image = load('assets/images/ball.png').convert_alpha()
		self.area = self.image.get_rect()
		self.rect = self.image.get_rect()

class Megaman(Sprite):

	def __init__(self):
		super(Megaman, self).__init__()

		self.states = StateMachine((
			('neutral', self.neutral),
		))

		images = []
		for i in xrange(14):
			images.append(load('assets/images/actor/running/%d.png' % (i+1)).convert_alpha())

	def neutral(self):
		pass


imageset = None

def init():
	global imageset

	images = []
	for i in xrange(14):
		images.append(load('assets/images/actor/running/%d.png' % (i+1)).convert_alpha())

	imageset = ImageSet(images, 900)