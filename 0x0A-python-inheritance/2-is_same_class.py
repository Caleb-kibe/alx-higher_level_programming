#!/usr/bin/python3
"""defines a function that checks a class"""


def is_same_class(obj, a_class):
    """returns true if an object is an instance of a specified class
    Args:
        obj: the object to check
        a_class: the class that to be matched with the type of the object
        Return: True if the object is an insatnce of the class, otherwise False
    """
    if type(obj) == a_class:
        return True
