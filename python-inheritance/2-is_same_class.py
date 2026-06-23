#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Returns True if object is exactly an instance of the specified class."""
    return type(obj) == a_class