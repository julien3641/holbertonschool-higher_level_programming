#!/usr/bin/python3


"""

This function is about to create a class named Square
Where there will be a private instance attribute size
On an other hand the area of this square
and to finish the square in #

"""


class Square:
    """
    create a private instance attribute size
    The __init__ is called when an object is created from the class
    and it allow the class to initialize the attributes of a class.

    if the size is not a integer, a message occured "size must be an ingeger"
    if the size is less than 0, a message occured "size must be >=0"
    """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        """ return the area of the square"""
    def area(self):
        return self.__size ** 2
    """print a square of # the size of self.__size"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()
