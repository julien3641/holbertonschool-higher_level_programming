#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle

""" Write a class Square that inherits from Rectangle
(9-rectangle.py). (task based on 10-square.py).
Instantiation with size: def __init__(self, size)::
size must be private. No getter or setter
size must be a positive integer, validated by integer_validator
the area() method must be implemented
print() should print, and str() should return
the square description: [Square] <width>/<height>
"""


class Square(Rectangle):
    """ defined a square of size "size by size" """

    """__init__ method to initialize a new instance"""
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    """area method to compute the area of the rectangle"""

    def area(self):
        return self.__size ** 2

    """str method to print the rectangle size"""

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
