from pygame import Rect

from globals import SCREENSIZE

class Camera(object):
    def __init__(self, world, target=None):
        self.rect = Rect(
            (0, 0), SCREENSIZE
        )
        self.world = world
        self.target = target

    def update(self, time):
        if self.target:
            self.rect.center = self.target.rect.center

    	if self.rect.right > self.world.rect.right:
            self.rect.right = self.world.rect.right
        if self.rect.left < self.world.rect.left:
            self.rect.left = self.world.rect.left
		
        if self.rect.top < self.world.rect.top:
            self.rect.top = self.world.rect.top
        if self.rect.bottom > self.world.rect.bottom:
            self.rect.bottom = self.world.rect.bottom