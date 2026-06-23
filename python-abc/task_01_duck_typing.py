#!/usr/bin/python3
"""Defines shapes interfaces and explores Duck Typing."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Represent an abstract shape blueprint."""

    @abstractmethod
    def area(self):
        """Calculate the area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter."""
        pass


class Circle(Shape):
    """Represent a circle."""

    def __init__(self, radius):
        """Initialize with radius."""
        self.radius = radius

    def area(self):
        """Return area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Represent a rectangle."""

    def __init__(self, width, height):
        """Initialize with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter relying on Duck Typing."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


# كود الفحص والاختبار (Test)
if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 7)

    print("--- Circle Info ---")
    shape_info(circle)

    print("\n--- Rectangle Info ---")
    shape_info(rectangle)