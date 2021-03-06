import math

def lerp(a, b, factor):
	return a + (b - a) * factor

def deg_to_rad(deg):
	return math.radians(deg)

def rad_to_deg(rad):
	return math.degrees(rad)

class Vector2(object):
	"""Represents a 2D vector."""

	def __init__(self, x=0.0, y=0.0):
		self.x = x
		self.y = y

	def __add__(self, rhs):
		return Vector2(self.x + rhs.x, self.y + rhs.y)

	def __sub__(self, rhs):
		return Vector2(self.x - rhs.x, self.y - rhs.y)

	def __mul__(self, scalar):
		return Vector2(self.x * scalar, self.y * scalar)

	def __div__(self, scalar):
		return Vector2(self.x / scalar, self.y / scalar)

	def __neg__(self):
		return Vector2(-self.x, -self.y)

	def magnitude(self):
		return math.sqrt(self.x**2 + self.y**2)

	def normalize(self):
		mag = self.magnitude()

		if mag != 0:
			self.x /= mag
			self.y /= mag

	def __str__(self):
		return '(%f, %f)' % (self.x, self.y)