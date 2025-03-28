#!/usr/bin/python3
"""
print a square
"""


def print_square(size):
    """
    
    Args:
    size: size of matrix

    Raises:
    ValueError: value less than zero
    TypeError: size not compatible
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
