#!/usr/bin/python3
"""Module for Student class with filter."""


class Student:
    """Defines a student with optional attribute filtering."""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student.

        If attrs is a list of strings, only those attributes
        are returned. Otherwise all attributes are returned.
        """
        if isinstance(attrs, list):
            return {k: v for k, v in self.__dict__.items()
                    if k in attrs}
        return self.__dict__
