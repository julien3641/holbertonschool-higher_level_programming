#!/usr/bin/python3

"""Create a class named Myint that inherit from int """


class MyInt(int):

    """ Myint has the == and != inverted"""

    def __init__(self, other):
        self.__other = other

    def __eq__(self, other):
        return self.__other != self.__other

    def __ne__(self, other):
        return self.__other == self.__other
