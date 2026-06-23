#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Returns True if object is an instance or inherited instance."""
    return isinstance(obj, a_class)
