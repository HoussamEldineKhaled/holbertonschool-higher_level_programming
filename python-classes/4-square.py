#!/usr/bin/python3
"""getter and setter implementation for a square"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """initialize the square

        Args:
          size (int): size of square side
        """
        self.size = size

    @property
    def size(self):
        """set square size

        Returns: 
             int: size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """

        Args:
           value (int): value of the size
        Raises:
           TypeError: If value is not an integer
           ValueError: If value is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return square area

        Returns:
           int: area of square
        """
        return self.__size ** 2
