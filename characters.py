from animations import MegamanRunningAnimation

DIR_RIGHT = 1
DIR_LEFT = -1

class Character(object):

	def __init__(self, name):
		self.health = 200
		self.states = None
		self.state = None
		self.speed = 1.5
		self.anims = None
		self.anim = None
		self.name = name
		self.dir = DIR_RIGHT

	def update(self, time):
		self.anims[self.anim].update(time)

	def draw(self, screen):
		self.anims[self.anim].draw(screen)

class Megaman(Character):

	def __init__(self):
		super(Megaman, self).__init__('Megaman')

		self.anims = {
			'running': MegamanRunningAnimation()
		}
		self.anim = 'running'

