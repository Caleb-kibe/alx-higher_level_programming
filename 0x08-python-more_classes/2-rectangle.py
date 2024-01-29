#!/usr/bin/python3
"""defines a class rectangle"""


class Rectangle:
    """represent a rectangle"""
    def __init__(self, width=0, height=0):
        """
        Args:
            width: the width of the rectangle
            height: the height of the rectangle
        """
        self.height = value
        self.width = value

    @property
    def height(self):
        """fetch the height of the rectangle"""
        self.__height = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        """fetches the width of the rectangle"""
        self.__width = value

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must >= 0")
