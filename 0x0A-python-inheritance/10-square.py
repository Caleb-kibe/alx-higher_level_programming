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
