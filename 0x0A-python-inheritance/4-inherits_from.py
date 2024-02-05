#!/usr/bin/python3
"""defines a function that checks for class"""


def inherits_from(obj, a_class):
    """returns true if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class; otherwise false
    Args:
        abj (any): the object to chech
        a_class: the class to the check if the object is an instance of
    Return: True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class ; otherwise False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
