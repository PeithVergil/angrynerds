DIR_RIGHT = 1
DIR_LEFT = -1

class Character(object):

	def __init__(self, name):
		self.health = 200
		self.speed = 1.5
		self.anims = None
		self.anim = None
		self.name = name
		self.dir = DIR_RIGHT

class Megaman(Character):

	def __init__(self):
		super(Megaman, self).__init__('Megaman')