from utils.image import load_frames

class Animation(object):

	def __init__(self, frames, maxtime):
		self.interval = maxtime/len(frames)
		self.maxtime = maxtime
		self.frames = frames
		self.index = 0
		self.time = 0

	def numframes(self):
		'''Get the total number of frames'''
		return len(self.frames)

	def currframe(self):
		'''Get the current frame'''
		return self.frames[self.index]

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

	def draw(self, screen, loc=(0,0)):
		screen.blit(self.currframe(), loc)

class MegamanStandingAnimation(Animation):

	def __init__(self):
		super(MegamanStandingAnimation, self).__init__(
			load_frames('assets/images/actor/standing', 1), 700
		)
		

class MegamanRunningAnimation(Animation):

	def __init__(self):
		super(MegamanRunningAnimation, self).__init__(
			load_frames('assets/images/actor/running', 14), 700
		)

class MegamanJumpingAnimation(Animation):

	def __init__(self):
		super(MegamanJumpingAnimation, self).__init__(
			load_frames('assets/images/actor/jumping', 20), 600
		)
		