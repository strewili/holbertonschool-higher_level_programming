#!/usr/bin/python3
"""Defines Fish, Bird, and the multiple inherited FlyingFish."""


class Fish:
    """Represent a fish."""

    def swim(self):
        """Print swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Print fish habitat."""
        print("The fish lives in water")


class Bird:
    """Represent a bird."""

    def fly(self):
        """Print flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Print bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represent a flying fish inheriting from Fish and Bird."""

    def fly(self):
        """Override fly."""
        print("The flying fish is soaring!")

    def swim(self):
        """Override swim."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Override habitat."""
        print("The flying fish lives both in water and the sky!")


# كود الفحص والاختبار (Test)
if __name__ == "__main__":
    ff = FlyingFish()
    ff.fly()
    ff.swim()
    ff.habitat()

    print("\n--- Method Resolution Order (MRO) ---")
    for cls in FlyingFish.mro():
        print(cls)