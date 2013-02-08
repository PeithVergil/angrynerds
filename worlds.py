from pymunk import Space, Vec2d

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

    def __init__(self, objects, camera, bgimage=None):
        super(SimpleWorld, self).__init__(objects, camera, bgimage)

        # Physics space
        self.space = Space()
        # Default gravity values
        self.space.gravity = Vec2d(0.0, -900.0)

        for obj in self.objects:
            self.add(obj)

    def add(self, obj):
        '''Add an object to the Physics simulation'''
        self.space.add(obj.body, obj.shape)

    def update(self, time):
        # Update Physics simulation
        self.space.step(1.0/60.0)
        # Update the rest of the world
        super(SimpleWorld, self).update(time)

class SampleWorld(SimpleWorld):

    def __init__(self):
        megaman1 = Megaman((100,100))
        megaman2 = Megaman((200,200))
        megaman3 = Megaman((300,300))

        # megaman1.rect.x = 0
        # megaman1.rect.y = 100

        # megaman2.rect.x = 100
        # megaman2.rect.y = 200

        # megaman3.rect.x = 200
        # megaman3.rect.y = 300

        super(SampleWorld, self).__init__(
            [megaman1, megaman2, megaman3], Camera(self, megaman2), load_rgb('assets/images/world/simple/simple.png')
        )