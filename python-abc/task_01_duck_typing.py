#!/usr/bin/python3
"""Defines shape interfaces and explores duck typing."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Represent an abstract shape."""

    @abstractmethod
    def area(self):
        """Return the shape area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the shape perimeter."""
        pass


class Circle(Shape):
    """Represent a circle."""

    def __init__(self, radius):
        """Initialize a circle with a radius."""
        self.radius = abs(radius)

    def area(self):
        """Return the circle area."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return the circle perimeter."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Represent a rectangle."""

    def __init__(self, width, height):
        """Initialize a rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Return the rectangle perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a shape."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 7)

    print("--- Circle Info ---")
    shape_info(circle)

    print("\n--- Rectangle Info ---")
    shape_info(rectangle)
