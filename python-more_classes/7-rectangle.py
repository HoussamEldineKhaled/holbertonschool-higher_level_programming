#!/usr/bin/python3
"""Rectangle with area and parameter"""


class Rectangle:
    """Rectangle class creation"""

    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """create new rectangle

        Args:
           width (int): width of rectangle
           height (int): height of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """find area

        Return: area value
        """
        return self.__height * self.__width

    def perimeter(self):
        """find perimeter

        Returns: parameter value
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """string representation of rectangle

        Return: the rectangle or nothing
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        rectangle_arr = []
        for i in range(0, self.__height):
            rectangle_arr.append(str(self.print_symbol) * self.__width)
        return "\n".join(rectangle_arr)

    def __repr__(self):
        """representation of rectangle atributes

        Return: coordinates of the rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """message to be printed when deletion"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
