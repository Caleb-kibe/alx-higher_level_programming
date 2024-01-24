#!/usr/bin/python3
"""define class Square"""


class Square:
     """represent a square"""
     def __init__(self, size=0):
        """ initialize new square
        Args:
            size (int): size of new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """return current area of the square"""
        return (self.__size * self.__size)

