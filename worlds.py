from cameras import Camera
from utils.math import lerp
from utils.image import load_rgb

from characters import Megaman

class Word(object):

    def __init__(self, objects, camera, bgimage=None):
        self.objects = objects
        self.camera = camera
        self.image = bgimage
        self.rect = bgimage.get_rect()

    def update(self, time):
        for obj in self.objects:
            obj.update(time)

        self.camera.update(time)

    def draw(self, screen):
        screen.blit(self.image, self.camera.transform(self))

        for obj in self.objects:
            obj.draw(screen, self.camera.transform(obj))

class SimpleWorld(Word):

    def __init__(self, objects, camera, bgimage=None):
        super(SimpleWorld, self).__init__(objects, camera, bgimage)

        # Default world gravity
        self.gravity = (0, 0.5)

class SampleWorld(SimpleWorld):

    def __init__(self):
        megaman1 = Megaman(self, (100,100))
        megaman2 = Megaman(self, (200,200))
        megaman3 = Megaman(self, (300,300))

        super(SampleWorld, self).__init__(
            [megaman1, megaman2, megaman3], Camera(self, megaman2), load_rgb('assets/images/world/simple/simple.png')
        )