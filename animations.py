from pygame import transform

from utils.image import load_frames

class Animation(object):

	def __init__(self, name, frames, maxtime, character=None):
		self.character = character
		self.interval = maxtime/len(frames)
		self.maxtime = maxtime
		self.frames = frames
		self.index = 0
		self.name = name
		self.time = 0

		self.flipx = False
		self.flipy = False

	def numframes(self):
		'''Get the total number of frames'''
		return len(self.frames)

	def currframe(self):
		'''Get the current frame'''
		return self.frames[self.index]

	def framerect(self):
		'''Get the rect object of the current frame'''
		return self.frames[self.index].get_rect()

	def next(self):
		'''Jump to next frame'''
		self.index += 1
		if self.index == self.numframes():
			if self.character:
				self.character.message('anim_done')

			self.index = 0

	def prev(self):
		'''Jump to previous frame'''
		self.index -= 1
		if self.index < 0:
			if self.character:
				self.character.message('anim_done')

			self.index = self.numframes() - 1

	def update(self, time):
		self.time += time

		if self.time >= self.interval:
			self.next()

			if self.character:
				self.character.message('anim_update')

			self.time = 0

	def draw(self, screen, pos=(0,0)):
		frame = transform.flip(
			self.currframe(),
			self.flipx,
			self.flipy
		)

		screen.blit(frame, pos)

class MegamanStandingAnimation(Animation):

	def __init__(self, character):
		super(MegamanStandingAnimation, self).__init__(
			'standing', load_frames('assets/images/actor/standing', 1), 700, character
		)
		

class MegamanRunningAnimation(Animation):

	def __init__(self, character):
		super(MegamanRunningAnimation, self).__init__(
			'running', load_frames('assets/images/actor/running', 14), 700, character
		)

class MegamanJumpingAnimation(Animation):

	def __init__(self, character):
		super(MegamanJumpingAnimation, self).__init__(
			'jumping', load_frames('assets/images/actor/jumping', 10), 400, character
		)

class MegamanFallingAnimation(Animation):

	def __init__(self, character):
		super(MegamanFallingAnimation, self).__init__(
			'falling', load_frames('assets/images/actor/falling', 1), 400, character
		)

class MegamanShootingAnimation(Animation):

	def __init__(self, character):
		super(MegamanShootingAnimation, self).__init__(
			'shooting', load_frames('assets/images/actor/shooting', 6), 500, character
		)