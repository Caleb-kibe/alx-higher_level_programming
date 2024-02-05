#!/usr/bin/python3
"""defines a function that checks for type"""


def is_kind_of_class(obj, a_class):
    """checks if an object is an instance of a class that it inherits form
    Args:
        obj (any): the object to check.
        a_class (type): the class which to math the object to
    Returns: True if the object is an instance of, or if the object
        is an instance of a class that inherited from, the specified class ;
        otherwise False
    """
    if isinstance(obj, a_class):
        return True
    return False
