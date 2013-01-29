class StateMachine(object):

	def __init__(self, start, states):
		super(StateMachine, self).__init__()
		self.states = states
		self.state = start

	def update(self):
		for state, action in self.states:
			if state == self.state:
				action()
