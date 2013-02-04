from utils.math import lerp
from utils.image import load_rgb

class Word(object):

	def __init__(self, camera, bgimage=None):
                self.camera = camera
		self.image = bgimage
		self.rect = bgimage.get_rect()

	def update(self, time):
                self.camera.update(time)

                if self.camera.pos.right > self.rect.right:
                        self.camera.pos.right = self.rect.right
                if self.camera.pos.left < self.rect.left:
                        self.camera.pos.left = self.rect.left

	def draw(self, screen, cam=None):
                if cam:
                        screen.blit(self.image, (
                                self.rect.left - cam.pos.left,
                                self.rect.top - cam.pos.top
                        ))
                else:
                        screen.blit(self.image, (
                                -self.rect.left,
                                -self.rect.top
                        ))

class SimpleWorld(Word):

	def __init__(self, camera):
		super(SimpleWorld, self).__init__(
                        camera, load_rgb('assets/images/world/simple/simple.png')
		)
