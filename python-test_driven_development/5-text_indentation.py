#!/usr/bin/python3
"""This module provides a text indentation function."""


def text_indentation(text):
    """Print text with two new lines after ., ? and : characters."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    need_trim = False
    for char in text:
        if need_trim and char == " ":
            continue
        need_trim = False
        print(char, end="")
        if char in ".?:":
            print("\n")
            need_trim = True
