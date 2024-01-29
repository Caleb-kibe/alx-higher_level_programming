#!/usr/bin/python3
"""define a class rectangle"""


class Rectangle:
    """represent a rectangle
    attributes:
        number_of_instances: number of rectangle instances
        print_symbol: symbol used to represent a string
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialize a new rectangle
        Args:
            width: the width of the rectangle
            heingt: the height of the rectangle
        """
        type(self).number_of_instances += 1
        self.height = height
        self.width = width

    @property
    def height(self):
        """get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """return the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * (self.__height + self.__width))

    def __str__(self):
        """return a print of the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_str = []
        for i in range(self.__height):
            [rect_str.append(str(self.print_symbol))
                for j in range(self.__width)]
            if i != self.__height - 1:
                rect_str.append("\n")
        return ("".join(rect_str))

    def __repr__(self):
        """return a string representation of the rectangle"""
        rect_str = "Rectangle(" + str(self.__width)
        rect_str += ", " + str(self.__height) + ")"
        return (rect_str)

    def __del__(self):
        """prints a message when a triangle is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
