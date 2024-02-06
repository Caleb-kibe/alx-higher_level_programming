#!/usr/bin/python3
"""defines a function that reads a file"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to sdtout"""
    with open("filename", encoding="utd-8") as my_file:
        print(my_file.read(), end="")
