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
