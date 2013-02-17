from pygame import Rect

from grid import SimpleTileMap
from cameras import Camera

from characters import Megaman

class World(object):
    '''The base class of all world objects'''

    def __init__(self, tilemap, objects, camera):
        self.tilemap = tilemap
        if tilemap:
            self.rect = tilemap.bounds
        else:
            self.rect = None

        self.objects = objects
        self.camera = camera

    def update(self, time):
        self.tilemap.update(time)

        for obj in self.objects:
            obj.update(time)

        self.camera.update(time)

    def draw(self, screen):
        self.tilemap.draw(screen)

        for obj in self.objects:
            obj.draw(screen, self.camera.transform(obj))

class SimpleWorld(World):
    '''A world with simple Physics simulation'''

    def __init__(self, objects, camera, bgimage=None):
        super(SimpleWorld, self).__init__(objects, camera, bgimage)

        # Default world gravity
        self.gravity = (0, 0.5)

class SampleWorld(SimpleWorld):

    def __init__(self):
        # The character
        megaman = Megaman(self, (200,200))

         # The camera
        camera = Camera(self, megaman)

        super(SampleWorld, self).__init__(
            SimpleTileMap(self), [megaman], camera
        )