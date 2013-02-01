import pygame
from pygame import key, transform

import characters

class State(object):

	def __init__(self, character):
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

	def start(self):
		self.character.set_animation('standing')

	def update(self, time):
		keys = key.get_pressed()

		if keys[pygame.K_UP]:
			self.character.set_state('jumping')
		elif keys[pygame.K_LEFT]:
			self.character.set_dir(characters.DIR_LEFT)
			self.character.set_state('running')
		elif keys[pygame.K_RIGHT]:
			self.character.set_dir(characters.DIR_RIGHT)
			self.character.set_state('running')

class RunningState(State):

	def start(self):
		self.character.set_animation('running')

	def update(self, time):
		keys = key.get_pressed()

		if keys[pygame.K_UP]:
			self.character.set_state('jumping')
		elif keys[pygame.K_LEFT]:
			self.character.set_dir(characters.DIR_LEFT)
			self.character.set_state('running')
		elif keys[pygame.K_RIGHT]:
			self.character.set_dir(characters.DIR_RIGHT)
			self.character.set_state('running')
		else:
			self.character.set_state('standing')

class JumpingState(State):

	def start(self):
		self.character.set_animation('jumping')

	def update(self, time):
		keys = key.get_pressed()

		if keys[pygame.K_LEFT]:
			self.character.set_dir(characters.DIR_LEFT)
		elif keys[pygame.K_RIGHT]:
			self.character.set_dir(characters.DIR_RIGHT)

	def message(self, msg):
		if msg == 'anim_done':
			self.character.set_state('standing')
