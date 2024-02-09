#!/usr/bin/python3


class Base:
    """base class to manage object IDs"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor
        Args:
            id (int): the id of the object. Defaults to None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
