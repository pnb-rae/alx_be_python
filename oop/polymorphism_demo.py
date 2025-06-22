# polymorphism_demo.py

import math

class Shape:
    def area(self):
        """Base method to compute area, meant to be overridden."""
        raise NotImplementedError("Subclasses must override area()")


class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Override to compute rectangle area."""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        """Initialize circle with radius."""
        self.radius = radius

    def area(self):
        """Override to compute circle area."""
        return math.pi * (self.radius ** 2)
