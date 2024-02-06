#!/usr/bin/python3
"""defines a function that writes a file"""


def write_file(filename="", text=""):
    """writes a string to a UTF-8 text file
    Args:
        filename: the name of the file
        text: string to write into the file
    Return:
        the number of characters written
    """
    with open("filename", "w", encoding="utf-8") as my_file:
        return my_file.write(text)
