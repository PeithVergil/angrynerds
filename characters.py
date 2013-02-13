import math
import pygame

from animations import (
	MegamanStandingAnimation, MegamanRunningAnimation, MegamanJumpingAnimation, MegamanFallingAnimation, MegamanShootingAnimation
)

from states import (
	StandingState, ShootingState, RunningState, JumpingState, FallingState
)

DIR_RIGHT = 1
DIR_LEFT = -1
DIR_DOWN = 1
DIR_UP = -1

class Character(object):

	def __init__(self, world, states, anims, pos=(0,0)):
		# World object
		self.world = world

		# Character states
		self.states = states
		self.state = None

		# Character animations
		self.anims = anims
		self.anim = None

		# Other character settings
		self.health = 200
		self.speed = 0.1
		self.name = 'Unnamed'
		self.dir = DIR_RIGHT

		# Set the default state
		self.init_state()

		# For now, use the rect from one of the animation frames.
		self.rect = self.anim.framerect()

		# Initial position
		self.rect.x = pos[0]
		self.rect.y = pos[1]

	def init_state(self):
		self.set_state('standing')

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

	def right(self, time):
		# Right direction
		self.dir = DIR_RIGHT
		# Move to right
		self.rect.right += math.ceil(self.dir * self.speed * time)

	def left(self, time):
		# Left direction
		self.dir = DIR_LEFT
		# Move to left
		self.rect.left += self.dir * self.speed * time

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

	def draw(self, screen, pos):
		if self.anim:
			self.anim.draw(screen, pos)

			# FOR DEBUGGING:
			# Draw the objects bounding box
			pygame.draw.rect(screen, (255,0,0), (
				pos[0], pos[1], self.rect.width, self.rect.height
			), 1)

class SimpleCharacter(Character):

	def update(self, time):
		# Simulate the effects of gravity
		self.rect.x += self.world.gravity[0] * time
		self.rect.y += self.world.gravity[1] * time

		super(SimpleCharacter, self).update(time)

class Megaman(SimpleCharacter):

	def __init__(self, world, pos=(0,0)):
		states = [
			StandingState(self),
			ShootingState(self),
			RunningState(self),
			JumpingState(self),
			FallingState(self),
		]
		anims = [
			MegamanStandingAnimation(self),
			MegamanShootingAnimation(self),
			MegamanJumpingAnimation(self),
			MegamanFallingAnimation(self),
			MegamanRunningAnimation(self),
		]
		super(Megaman, self).__init__(world, states, anims, pos)

		self.name = 'Megaman'