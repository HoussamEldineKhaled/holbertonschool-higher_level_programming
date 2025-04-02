#!/usr/bin/python3
"""Square with area"""


class Square:
    """this is the square class"""

    def __init__(self, size=0):
        """initialise square with area

        Args: 
           size (int): size of the square
        """
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    def area(self):
        """find area

        Returns:
             int: square area
        """
        return self.__size * self.__size
