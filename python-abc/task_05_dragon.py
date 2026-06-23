#!/usr/bin/python3
"""Defines Mixins for behaviors and a Dragon class."""


class SwimMixin:
    """Provides swimming functionality."""

    def swim(self):
        """Print swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Provides flying functionality."""

    def fly(self):
        """Print flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represent a mythical Dragon combining capabilities."""

    def roar(self):
        """Print dragon roar."""
        print("The dragon roars!")


# كود الفحص والاختبار (Test)
if __name__ == "__main__":
    draco = Dragon()
    draco.swim()
    draco.fly()
    draco.roar()