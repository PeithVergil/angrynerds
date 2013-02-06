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
        self.camera.update(time)

        for obj in self.objects:
            obj.update(time)

    def draw(self, screen):
        screen.blit(self.image, (
            self.rect.left - self.camera.rect.left,
            self.rect.top - self.camera.rect.top
        ))

        for obj in self.objects:
            obj.draw(screen, self.camera)

class SimpleWorld(Word):

    def __init__(self):
        megaman1 = Megaman()
        megaman2 = Megaman()
        megaman3 = Megaman()

        megaman1.rect.left = 0
        megaman1.rect.top = 100

        megaman2.rect.left = 100
        megaman2.rect.top = 200

        megaman3.rect.left = 200
        megaman3.rect.top = 300

        super(SimpleWorld, self).__init__(
            [megaman1, megaman2, megaman3], Camera(self, megaman2), load_rgb('assets/images/world/simple/simple.png')
        )
