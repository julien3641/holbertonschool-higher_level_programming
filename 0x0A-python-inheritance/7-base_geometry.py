#!/usr/bin/python3

"""Write a class BaseGeometry with a public instance
that raises an Exception with the message area() is not implemented
Public instance method: def integer_validator(self, name, value):
that validates value:
you can assume name is always a string
if value is not an integer: raise a TypeError exception
with the message <name> must be an integer
if value is less or equal to 0: raise a ValueError exception
with the message <name> must be greater than 0
You are not allowed to import any module
"""


class BaseGeometry:

    def area(self):
        """def area that raise an exception message"""
        raise Exception('area() is not implemented')

    def integer_validator(name, value):
        """
        The method validator integer validate
        if the value is an int
        public instance method that validate the type of value
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
