#!/usr/bin/python3
"""defines a class mylist that inherits from list"""


class MyList(list):
    """implemetents a sorted printing for the class list"""

    def print_sorted(self):
        """prints a list in ascending order"""
        sorted_list = sorted(self)
        print (sorted_list)
