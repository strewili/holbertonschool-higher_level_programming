#!/usr/bin/python3
"""Defines an abstract Animal class and its concrete subclasses."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Represent an abstract animal blueprint."""

    @abstractmethod
    def sound(self):
        """Abstract method for animal sound."""
        pass


class Dog(Animal):
    """Represent a dog."""

    def sound(self):
        """Return the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """Represent a cat."""

    def sound(self):
        """Return the sound of a cat."""
        return "Meow"


# كود الفحص والاختبار (Test)
if __name__ == "__main__":
    dog = Dog()
    cat = Cat()
    print(f"Dog says: {dog.sound()}")
    print(f"Cat says: {cat.sound()}")

    try:
        # محاولة استنتاج كائن من الفئة المجردة مباشرة (ستفشل)
        animal = Animal()
    except TypeError as e:
        print(f"Caught expected error: {e}")