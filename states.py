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
			self.character.dir = characters.DIR_LEFT

			# print self.character.rect.left, ' + ', self.character.dir * self.character.speed * time
			self.character.rect.left += self.character.dir * self.character.speed * time
			# print self.character.rect.left
		elif keys[pygame.K_RIGHT]:
			self.character.dir = characters.DIR_RIGHT

			# print self.character.rect.right, ' + ', self.character.dir * self.character.speed * time
			self.character.rect.right += math.ceil(self.character.dir * self.character.speed * time)
			# print self.character.rect.right
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
			self.character.set_state('standing')
