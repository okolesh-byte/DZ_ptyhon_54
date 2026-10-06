import math

class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return math.pi * self.radius ** 2 * self.height

    def surface(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)