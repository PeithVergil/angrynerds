from animations import (
	MegamanStandingAnimation, MegamanRunningAnimation, MegamanJumpingAnimation
)

from states import (
	StandingState, RunningState, JumpingState
)

DIR_RIGHT = 1
DIR_LEFT = -1

class Character(object):

	def __init__(self, name):
		self.health = 200
		self.states = None
		self.state = 'standing'
		self.speed = 1.5
		self.anims = None
		self.anim = 'standing'
		self.name = name
		self.dir = DIR_RIGHT

	# def set_dir(self, direction):
		# animation = self.get_animation()

		# if direction == DIR_LEFT:
			# animation.flipx = True
		# else:
			# animation.flipx = False

		# self.dir = direction

	def get_state(self, name=None):
		if not name:
			return self.states[self.state]
		else:
			return self.states[name]

	def set_state(self, name):
		cur_state = self.get_state()
		if ( cur_state ):
			cur_state.stop()

		new_state = self.get_state(name)
		if ( new_state ):
			new_state.start()

		self.state = name

		return new_state

	def get_animation(self, name=None):
		if not name:
			return self.anims[self.anim]
		else:
			return self.anims[name]

	def set_animation(self, name):
		self.anim = name
		return  self.get_animation(name)

	def message(self, msg):
		stat = self.get_state()
		if stat:
			stat.message(msg)

	def update(self, time):
		anim = self.get_animation()
		if anim:
			if self.dir == DIR_LEFT:
				anim.flipx = True
			else:
				anim.flipx = False
				
			anim.update(time)

		stat = self.get_state()
		if stat:
			stat.update(time)

	def draw(self, screen):
		anim = self.get_animation()
		if anim:
			anim.draw(screen)

class Megaman(Character):

	def __init__(self):
		super(Megaman, self).__init__('Megaman')

		self.anims = {
			'standing': MegamanStandingAnimation(self),
			'jumping': MegamanJumpingAnimation(self),
			'running': MegamanRunningAnimation(self),
		}

		self.states = {
			'standing': StandingState(self),
			'running': RunningState(self),
			'jumping': JumpingState(self),
		}

		self.set_state('standing')