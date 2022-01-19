#!/usr/bin/python3

"""
This function is about to create a class named Square
Where there will be a private instance attribute size

"""


class Square:
    """
    create a private instance attribute size
    The __init__ is called when an object is created from the class
    and it allow the class to initialize the attributes of a class.
    """
    def __init__(self, size):
        self.__size = size
