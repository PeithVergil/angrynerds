import math

import pygame
from pygame import key, transform

import characters

class State(object):

	def __init__(self, name, character):
		self.name = name
		self.character = character

	def message(self, msg):
		pass

	def update(self, time):
		pass

	def start(self):
		pass

	def stop(self):
		pass

class StandingState(State):

	def __init__(self, character):
		super(StandingState, self).__init__('standing', character)

	def start(self):
		self.character.set_animation('standing')

	def update(self, time):
		keys = key.get_pressed()

		if keys[pygame.K_UP]:
			self.character.set_state('jumping')
		elif keys[pygame.K_LEFT]:
			self.character.dir = characters.DIR_LEFT
			self.character.set_state('running')
		elif keys[pygame.K_RIGHT]:
			self.character.dir = characters.DIR_RIGHT
			self.character.set_state('running')
		elif keys[pygame.K_SPACE]:
			self.character.set_state('shooting')

class ShootingState(State):

	def __init__(self, character):
		super(ShootingState, self).__init__('shooting', character)

	def start(self):
		self.character.set_animation('shooting')

	def message(self, msg):
		if msg == 'anim_done':
			self.character.set_state('standing')

class RunningState(State):

	def __init__(self, character):
		super(RunningState, self).__init__('running', character)

	def start(self):
		self.character.set_animation('running')

	def update(self, time):
		keys = key.get_pressed()

		if keys[pygame.K_UP]:
			self.character.set_state('jumping')
		elif keys[pygame.K_LEFT]:
			self.character.left(time)
		elif keys[pygame.K_RIGHT]:
			self.character.right(time)
		else:
			self.character.set_state('standing')

class JumpingState(State):

	def __init__(self, character):
		super(JumpingState, self).__init__('jumping', character)

	def start(self):
		self.character.set_animation('jumping')

	def update(self, time):
		keys = key.get_pressed()

		if keys[pygame.K_LEFT]:
			self.character.dir = characters.DIR_LEFT
		elif keys[pygame.K_RIGHT]:
			self.character.dir = characters.DIR_RIGHT

	def message(self, msg):
		if msg == 'anim_done':
			self.character.set_state('falling')

class FallingState(State):

	def __init__(self, character):
		super(FallingState, self).__init__('falling', character)

	def start(self):
		self.character.set_animation('falling')

	def update(self, time):
		keys = key.get_pressed()

		if keys[pygame.K_LEFT]:
			self.character.left(time)
		elif keys[pygame.K_RIGHT]:
			self.character.right(time)