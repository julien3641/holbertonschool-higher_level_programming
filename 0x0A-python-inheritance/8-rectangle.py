#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry

    """ write a class Rectangle that inherits from BaseGeometry
     Within importing the module de la task 7"""

class Rectangle(BaseGeometry):

    """ write a class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """
        Arguments:
        @width: width size
        @height: height size
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
