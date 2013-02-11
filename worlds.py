from pymunk import Segment, Space, Vec2d
from pymunk.pygame_util import draw_space

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
            obj.draw(screen)

class SimpleWorld(Word):

    def __init__(self, objects, camera, bgimage=None):
        super(SimpleWorld, self).__init__(objects, camera, bgimage)

        # Physics space
        self.space = Space()
        # Default gravity values
        self.space.gravity = Vec2d(0.0, -900.0)

        for obj in self.objects:
            self.space.add(obj.body, obj.shape)

    def update(self, time):
        # Update Physics simulation
        self.space.step(1.0/60.0)
        # Update the rest of the world
        super(SimpleWorld, self).update(time)

    def draw(self, screen):
        super(SimpleWorld, self).draw(screen)
        # FOR DEBUGGING:
        # Draw the physics space
        draw_space(screen, self.space)

class SampleWorld(SimpleWorld):

    def __init__(self):
        megaman1 = Megaman(self, (100,100))
        megaman2 = Megaman(self, (200,200))
        megaman3 = Megaman(self, (300,300))

        super(SampleWorld, self).__init__(
            [megaman1, megaman2, megaman3], Camera(self, megaman2), load_rgb('assets/images/world/simple/simple.png')
        )

        # Ground static object
        self.space.add(Segment(self.space.static_body, (0, 50), (640, 50), 5))