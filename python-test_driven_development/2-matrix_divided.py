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
    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(ele, (int, float)) for row in matrix for ele in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if any(len(row) == 0 for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(el / div, 2) for el in row] for row in matrix]
