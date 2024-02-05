#!/usr/bin/python3
"""defines a rectangle SubClass Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represents a square"""

    def __init__(self, size):
        """initializes a new square
        Args:
            size (int): the size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """returns the area of the square"""
        return (self.__size ** 2)

    def __str__(self):
        """prints and returns the description of the square"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
