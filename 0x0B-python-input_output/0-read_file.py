#!/usr/bin/python3
"""defines a function that reads a file"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to sdtout"""
    with open(filename, encoding="utf-8") as fil:
        print(fil.read(), end="")
