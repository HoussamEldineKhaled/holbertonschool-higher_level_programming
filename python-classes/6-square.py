#!/usr/bin/python3
"""Square final exercise"""


class Square:
    """Square final method"""

    def __init__(self, size=0, position=(0, 0)):
        """Square creation

        Args:
           size (int): size of the square
           position: position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """get the size of the square

        Return:
           int: size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """set the size of square to a value

        Args:
           value (int):value of the square

        Raises:
           TypeError: if value is not an integer
           ValueError: if value is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """get the position coordinates

        Return:
           int: position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """set the tuple position

        Args:
           value (int): value of the position

        Raises:
           TypeError: if there is not tuple of positive ints
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """print area of square

        Return:
           int: area of square
        """
        return self.__size ** 2

    def my_print(self):
        """print square"""
        if self.__size == 0:
            print()
        print("\n" * self.__position[1], end="")
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
