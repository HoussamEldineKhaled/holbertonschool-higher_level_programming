#!/usr/bin/python3
"""more detailed square"""


class Square:
    """making a more safe square"""
    
    def __init__(self, size=0):
        """initialize square

        Args:size of the square
        """
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
