#!/usr/bin/python3
"""adds two integers"""


def add_integer(a, b=98):
    """returns the sum of a and b
    float arguments are typecasted to integers before the operation is performed
    Args:
        a: first integer
        b: second integer
    Raises:
        TypeError: if either a or b is not an integer or a float        
    """
    if ((not isinstance(a, int)) and (not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int)) and (not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
