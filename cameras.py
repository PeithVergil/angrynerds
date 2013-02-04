from pygame import Rect

from globals import SCREENSIZE

class Camera(object):
        def __init__(self, character=None):
                self.char = character
                self.pos = Rect((0, 0), SCREENSIZE)

                self.char.posx = self.pos.centerx
                self.char.posy = self.pos.centery

        def update(self, time):
		self.pos.center = (
                        self.char.posx,
                        self.char.posy
                )
