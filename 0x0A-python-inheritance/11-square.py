#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle

""" create a class square of inheritance from Rectangle"""


class Square(Rectangle):
    """ defined a square of size "size by size" """

    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
