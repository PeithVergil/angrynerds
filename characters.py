# import pygame
import pymunk

from animations import (
	MegamanStandingAnimation, MegamanRunningAnimation, MegamanJumpingAnimation, MegamanShootingAnimation
)

from states import (
	StandingState, ShootingState, RunningState, JumpingState
)

DIR_RIGHT = 1
DIR_LEFT = -1
DIR_DOWN = 1
DIR_UP = -1

class Character(object):

	def __init__(self, name, states, anims, pos=(0,0)):
		self.name = name

		# Character states
		self.states = states
		self.state = None

		# Character animations
		self.anims = anims
		self.anim = None

		self.health = 200
		self.speed = 0.1
		self.dir = DIR_RIGHT

		self.set_state('standing')

		if self.anim:
			self.rect = self.anim.framerect()

			# Initial position
			self.rect.x = pos[0]
			self.rect.y = pos[1]
		else:
			self.rect = None

	def get_state(self, name=None):
		for state in self.states:
			if state.name == name:
				return state
		return None

	def set_state(self, name):
		if ( self.state ):
			self.state.stop()

		self.state = self.get_state(name)
		if ( self.state ):
			self.state.start()

	def get_animation(self, name=None):
		for anim in self.anims:
			if anim.name == name:
				return anim
		return None

	def set_animation(self, name):
		self.anim = self.get_animation(name)

	def message(self, msg):
		if self.state:
			self.state.message(msg)

	def update(self, time):
		if self.anim:
			if self.dir == DIR_LEFT:
				self.anim.flipx = True
			else:
				self.anim.flipx = False

			self.anim.update(time)

		if self.state:
			self.state.update(time)

	def draw(self, screen, cam=None):
		if self.anim:
			if cam:
				self.anim.draw(screen, (
					self.rect.left - cam.rect.left,
					self.rect.top - cam.rect.top
				))
				# FOR TESTING:
				# Draw the objects bounding box
				# pygame.draw.rect(screen, (255,0,0), (
				# 	self.rect.left - cam.rect.left, self.rect.top - cam.rect.top, self.rect.width, self.rect.height
				# ), 1)
			else:
				self.anim.draw(screen, (
					self.rect.left,
					self.rect.top
				))

class SimpleCharacter(Character):

	def __init__(self, name, states, anims, pos=(0,0), mass=10):
		super(SimpleCharacter, self).__init__(name, states, anims, pos)

		self.mass = mass

		# Initialize Physics attributes
		self.initialize()

	def initialize(self):
		inertia = pymunk.moment_for_circle(
			self.mass, 0, self.rect.width
		)

		self.body = pymunk.Body(self.mass, inertia)

		if self.rect:
			self.body.position.x = self.rect.x
			self.body.position.y = self.rect.y

		self.shape = pymunk.Circle(self.body, self.rect.width)

	def update(self, time):
		super(SimpleCharacter, self).update(time)

		self.rect.x = self.body.position.x
		self.rect.y = -self.body.position.y

class Megaman(SimpleCharacter):

	def __init__(self, pos=(0,0)):
		super(Megaman, self).__init__(
			'Megaman',
			[
				StandingState(self),
				ShootingState(self),
				RunningState(self),
				JumpingState(self),
			],
			[
				MegamanStandingAnimation(self),
				MegamanShootingAnimation(self),
				MegamanJumpingAnimation(self),
				MegamanRunningAnimation(self),
			],
			pos
		)