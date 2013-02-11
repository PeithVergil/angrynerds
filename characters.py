import pygame
import pymunk
from pymunk.pygame_util import from_pygame, to_pygame

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

	def __init__(self, world, states, anims, pos=(0,0)):
		# The world object
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

		self.initialize()

		if self.anim:
			self.rect = self.anim.framerect()

			# Initial position
			self.rect.x = pos[0]
			self.rect.y = pos[1]
		else:
			self.rect = None

	def initialize(self):
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

	def draw(self, screen):
		if self.anim:
			cam = self.world.camera

			self.anim.draw(screen, (
				self.rect.left - cam.rect.left,
				self.rect.top - cam.rect.top
			))
			# FOR DEBUGGING:
			# Draw the objects bounding box
			# pygame.draw.rect(screen, (255,0,0), (
			# 	self.rect.left - cam.rect.left, self.rect.top - cam.rect.top, self.rect.width, self.rect.height
			# ), 1)

class SimpleCharacter(Character):

	def __init__(self, world, states, anims, pos=(0,0), mass=10):
		super(SimpleCharacter, self).__init__(world, states, anims, pos)

		self.mass = mass

		# Initialize Physics attributes
		self.setup()

	def setup(self):
		inertia = pymunk.moment_for_circle(
			self.mass, 0, self.rect.width
		)

		self.body = pymunk.Body(self.mass, inertia)

		if self.rect:
			# Convert from pygame to pymunk coordinates
			pos = from_pygame(
				(self.rect.x, self.rect.y), pygame.display.get_surface()
			)

			self.body.position.x = pos[0]
			self.body.position.y = pos[1]

		self.shape = pymunk.Circle(self.body, self.rect.width)

	def update(self, time):
		# Convert from pymunk to pygame coordinates
		pos = to_pygame(self.body.position, pygame.display.get_surface())

		self.rect.x = pos[0]
		self.rect.y = pos[1]

		super(SimpleCharacter, self).update(time)

class Megaman(SimpleCharacter):

	def __init__(self, world, pos=(0,0)):
		states = [
			StandingState(self),
			ShootingState(self),
			RunningState(self),
			JumpingState(self),
		]
		anims = [
			MegamanStandingAnimation(self),
			MegamanShootingAnimation(self),
			MegamanJumpingAnimation(self),
			MegamanRunningAnimation(self),
		]
		super(Megaman, self).__init__(world, states, anims, pos)

		self.name = 'Megaman'