#!/usr/bin/python3
"""geo base"""


class BaseGeometry:
    """base geo class"""

    def area(self):
        """raise an exception with the area
        Raise:
           Exception: if area was not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate integers
        Raises:
           TypeError: if value isn't an int
           ValueError: if value is less or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
