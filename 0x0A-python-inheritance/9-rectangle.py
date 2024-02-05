#!/usr/bin/python3
"""defines a class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represents a rectangle using basegeometry parent class"""

    def __init__(self, width, height):
        """initializes a rectangle
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """return the area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """return the print() and str() represenation of the triangle"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
