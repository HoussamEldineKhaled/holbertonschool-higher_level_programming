#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Args:
    a: first int
    b: second int
    Returns:
       Sume of a and b
    Raises:
       TypeError: if both a and b are not numbers

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
