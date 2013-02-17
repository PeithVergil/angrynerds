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

		# Define the object's rect
		self.init_rect()

		# Initial position
		self.rect.x = pos[0]
		self.rect.y = pos[1]

	def init_state(self):
		self.set_state('standing')

	def init_rect(self):
		# For now, use the rect from one of the animation frames.
		self.rect = self.anim.framerect()

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

	def jump(self, time):
		self.rect.top -= 0.9 * time

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
			# Draw the character's bounding box
			# pygame.draw.rect(screen, (255,0,0), (
			# 	pos[0], pos[1], self.rect.width, self.rect.height
			# ), 1)

class SimpleCharacter(Character):

	def sensor_top(self):
		tilemap = self.world.tilemap

		x, y = self.rect.center
		r, c = tilemap.screen(x, y)
		tile = tilemap.lookup(r, c)

		if tile.solid:
			return (True, (x, y), (r, c))
		else:
			return False

	def sensor_bot(self):
		tilemap = self.world.tilemap

		x, y = self.rect.midbottom
		r, c = tilemap.screen(x, y)
		tile = tilemap.lookup(r, c)

		if tile.solid:
			return (True, (x, y), (r, c))
		else:
			return False

	def update(self, time):
		tilemap = self.world.tilemap

		# Simulate the effects of gravity
		self.rect.x += self.world.gravity[0] * time
		self.rect.y += self.world.gravity[1] * time

		bot = self.sensor_bot()
		if bot:
			b_active, b_xy, b_rc = bot

			top = self.sensor_top()
			if not top:
				x, y, w, h = tilemap.grid(b_rc[0], b_rc[1])

				self.rect.bottom = y

				self.message('char_grounded')
		else:
			self.message('falling')

		super(SimpleCharacter, self).update(time)

	def draw(self, screen, pos):
		super(SimpleCharacter, self).draw(screen, pos)

		# FOR DEBUGGING:
		camera = self.world.camera

		# Draw the character's bottom center point
		x, y = self.rect.midbottom
		x, y = camera.to_screen(x, y)
		pygame.draw.rect(screen, (0,0,255), (
			x-2, y-2, 4, 4
		))

		x, y = self.rect.center
		x, y = camera.to_screen(x, y)
		pygame.draw.rect(screen, (0,0,255), (
			x-2, y-2, 4, 4
		))

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