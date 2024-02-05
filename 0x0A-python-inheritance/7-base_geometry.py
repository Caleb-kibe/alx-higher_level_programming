#!/usr/bin/python3
"""defines a class BaseGeometry"""


class BaseGeometry:
    """represents a base geometry"""

    def area(self):
        """not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value as an iteger
        Args:
            name (str): the name of the parameter
            value (int): the parameter to be vlaidated
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
