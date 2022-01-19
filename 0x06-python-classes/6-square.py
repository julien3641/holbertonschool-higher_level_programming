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

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    """bring the size of the square"""
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """add position to the object"""
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int and type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    """ return the area of the square"""
    def area(self):
        return self.__size ** 2

    """print a square of # and spaces """
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for line in range(self.position[1]):
                print()
            for i in range(self.size):
                print(" " * self.position[0], end="")
                print('#' * self.__size)
