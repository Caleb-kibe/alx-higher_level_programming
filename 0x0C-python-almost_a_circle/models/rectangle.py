#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    """represents a rectangle with, height, x and y coordinates"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes a new rectangle
        Args:
            width (int): the width of the rectangle
            height (int): height of the rectangle
            x (int): x coordinate of the rectangle
            y (int): y coordinate of the rectangle
        """
        super().__init__(id)
        self.__width = width
        self.__height= height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle"""
        if isinstance(value, int) and value > 0:
            self.__width = value

    @property
    def height(self):
        """get the height of the rectangle"""
        return self.__width

    @height.setter
    def height(self, value):
        """set the height of the rectangle"""
        if isinstance(value, int) and value > 0:
            self.__height = value

    @property
    def x(self):
        """get the x coordiante of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value of x"""
        if isinstance(value, int) and value > 0:
            self.__x = x

    @property
    def y(self):
        """get the y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value of y"""
        if isinstance(value, int) and value > 0:
            self.__y = y
