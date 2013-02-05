from pygame import Rect

from globals import SCREENSIZE

class Camera(object):
    def __init__(self, character=None):
        self.rect = Rect((0, 0), SCREENSIZE)
        self.char = character

        # self.char.rect.centerx = self.rect.centerx
        # self.char.rect.centery = self.rect.centery

    def update(self, time):
        self.rect.center = (
            self.char.rect.centerx,
            self.char.rect.centery
        )
