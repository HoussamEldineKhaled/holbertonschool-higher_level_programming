#!/usr/bin/python3
"""
Module for matrices
Division
"""


def matrix_divided(matrix, div):
    """divide matrices

    Args:
    matrix: matrix to be divided
    div: divident
    Returns:
    new matrixs of quotients
    Raises:
    TypeError: many cases
    ZeroDivisionError: if div is zero
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(ele, (int, float)) for row in matrix for ele in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(el / div, 2) for el in row] for row in matrix]
