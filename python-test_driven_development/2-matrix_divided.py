#!/usr/bin/python3
"""This module provides a matrix division function."""


def matrix_divided(matrix, div):
    """Return a new matrix with every element divided by div."""
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(msg)

    row_size = None
    for row in matrix:
        if not isinstance(row, list) or row == []:
            raise TypeError(msg)
        if row_size is None:
            row_size = len(row)
        elif len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        for num in row:
            if type(num) not in [int, float]:
                raise TypeError(msg)

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
