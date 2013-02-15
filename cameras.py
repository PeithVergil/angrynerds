from pygame import Rect

from globals import SCREENSIZE

class Camera(object):
    def __init__(self, world, target=None):
        self.rect = Rect(
            (0, 0), SCREENSIZE
        )
        self.world = world
        self.target = target
        
    def transform(self, obj):
        return (
            obj.rect.x - self.rect.x,
            obj.rect.y - self.rect.y,
        )

    def to_screen(self, x, y):
        return (
            x - self.rect.x,
            y - self.rect.y,
        )

    def to_world(self, x, y):
        return (
            x + self.rect.x,
            y + self.rect.y,
        )

    def update(self, time):
        if self.target:
            self.rect.center = self.target.rect.center

        # Don't go beyond the left or right boundaries
    	if self.rect.right > self.world.rect.right:
            self.rect.right = self.world.rect.right
        if self.rect.left < self.world.rect.left:
            self.rect.left = self.world.rect.left
		# Don't go beyond the top or bottom boundaries
        if self.rect.top < self.world.rect.top:
            self.rect.top = self.world.rect.top
        if self.rect.bottom > self.world.rect.bottom:
            self.rect.bottom = self.world.rect.bottom