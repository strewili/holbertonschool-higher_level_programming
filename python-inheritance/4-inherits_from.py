#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Returns True if the object is an inherited instance (subclass) only."""
    return issubclass(type(obj), a_class) and type(obj) != a_class