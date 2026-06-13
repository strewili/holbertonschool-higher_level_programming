#!/usr/bin/python3
"""This module provides an integer addition function."""


def add_integer(a, b=98):
    """Return the integer addition of a and b."""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
