#!/usr/bin/python3
""" Math integer adding module
Basic addition
"""
def add_integer(a, b=98):
    """
    Add integers

    Args:
    a: first int
    b: second int

    Returns:
       Sum of a and b

    Raises:
       TypeError: if both a and b are not numbers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
