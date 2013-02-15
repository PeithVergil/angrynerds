import pygame

from grid import Grid, SampleGridMap
from cameras import Camera
from utils.image import load_rgb

from characters import Megaman

class World(object):
    '''The base class of all world objects'''

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
        for obj in self.objects:
            obj.draw(screen, self.camera.transform(obj))

class SimpleWorld(World):
    '''A world with simple Physics simulation'''

    def __init__(self, objects, camera, bgimage=None):
        super(SimpleWorld, self).__init__(objects, camera, bgimage)

        # Default world gravity
        self.gravity = (0, 0)
        # self.gravity = (0, 0.5)

class SampleWorld(SimpleWorld):

    def __init__(self):
        # The character
        megaman = Megaman(self, (200,200))

         # The camera
        camera = Camera(self, megaman)

        super(SampleWorld, self).__init__(
            [megaman], camera, load_rgb('assets/images/world/simple/simple.png')
        )

        self.gmap = SampleGridMap(self)

    def update(self, time):
        super(SampleWorld, self).update(time)

        mpos = pygame.mouse.get_pos()
        # Convert mouse position from
        # screen space to world space
        grid = self.gmap.screen(
            mpos[0] + self.camera.rect.x,
            mpos[1] + self.camera.rect.y,
        )

        self.cpos = self.gmap.grid(grid[1], grid[0])

    def draw(self, screen):
        self.gmap.draw(screen)

        pygame.draw.rect(screen, (0,255,0), (
            self.cpos[0] - self.camera.rect.x,
            self.cpos[1] - self.camera.rect.y,
            self.cpos[2],
            self.cpos[3],
        ))

        super(SampleWorld, self).draw(screen)