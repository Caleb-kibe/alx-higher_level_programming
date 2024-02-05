#!/usr/bin/python3
"""defines a lookup function that looks up object attributes"""


def lookup(obj):
    """returns the list of available attributes and methods of an object"""
    return dir(obj)
