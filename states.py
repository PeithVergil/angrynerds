class State(object):

	def __init__(self, character):
		self.character = character
		self.animation = None

	def update(self, time):
		self.animation.update(time)

	def draw(self, screen):
		self.animation.draw(screen)

	def start(self):
		pass

	def stop(self):
		pass

class StandingState(State):

	def start(self):
		self.animation = self.character.set_animation('standing')

class RunningState(State):

	def start(self):
		self.animation = self.character.set_animation('running')

class JumpingState(State):

	def start(self):
		self.animation = self.character.set_animation('jumping')
