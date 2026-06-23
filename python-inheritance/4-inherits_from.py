#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Returns True if object is an inherited instance (subclass) only."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
