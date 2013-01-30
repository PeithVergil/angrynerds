class State(object):

	def __init__(self, char):
		self.char = char

	def update(self, time):
		pass

	def start(self):
		pass

	def end(self):
		pass

class StandingState(State):
	def start(self):
		self.char.animation = 'standing'

	def update(self, time):
		pass

class RunningState(State):
	def start(self):
		self.char.animation = 'running'

	def update(self, time):
		pass