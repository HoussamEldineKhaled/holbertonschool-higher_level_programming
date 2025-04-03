#!/usr/bin/python3
"""more sophisticated rectangle class"""


class Rectangle:
    """create a rectangle"""

    def __init__(self, width=0, height=0):
        """create rectangle

        Args:
           width (int): width of the rectangle
           height (int): height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get the rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of rectangle

        Args:
           value (int): value of int

        Raise:
           TypeError: if value is not an int
           ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the height value

        Returns: height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """find the height

        Args:
           value (int): value of the height

        Raises:
           TypeError: if height is not int
           ValueError: if height is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
