from pygame.image import load
from pygame.sprite import Sprite

from utils import Vector2

class AnimatedSprite(Sprite):

	ID = 1

	def __init__(self):
		super(AnimatedSprite, self).__init__()
		
		self.image = load('assets/images/ball.png').convert_alpha()
		self.name = 'Unnamed_%d' % self.ID
		self.rect = self.image.get_rect()
		self.ID += 1