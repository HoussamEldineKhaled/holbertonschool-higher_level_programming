#!/usr/bin/python3
"""printing a square"""


class Square:
    """the class which will create the square and all its functionality"""

    def __init__(self, size):
        """Create the new square

        Args:
           size (int): size of square side
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square

        Returns:
           int: the square size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """set the size to new value

        Args:
           value (int): value of the size

        Raises:
           TypeError: size is greater than zero
           ValueError: size is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculate area of square

        Return:
           int: area of square
        """
        return self.__size ** 2

    def my_print(self):
        """print the square itself"""
        if self.__size == 0:
            print()
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("{}".format('#'), end='')
            print()
