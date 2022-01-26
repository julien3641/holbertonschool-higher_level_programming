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

        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif isinstance(position, tuple) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    """bring the size of the square"""
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    """add position to the object"""
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(position, tuple) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    """ return the area of the square"""
    def area(self):
        return self.__size ** 2

    """print a square of # and spaces """
    def my_print(self):
        if self.__size == 0:
            print("")
        elif self.__position[1] > 0:
            for pos_1 in range(self.__position[1]):
                print("")
        for row in range(self.__size):
            for pos_0 in range(self.__position[0]):
                print(" ", end="")
            for column in range(self.__size):
                    print("#", end="")
            print("")
