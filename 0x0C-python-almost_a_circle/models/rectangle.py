#!/usr/bin/python3
"""
The module define the class Rectangle.
"""
from models.base import Base


class Rectangle(Base):
    """Create a class Rectangle that inherit from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize the Rectangle class"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        elif type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        elif type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        elif type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    def __str__(self):
        """override the with __str__ method a message"""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    @property
    def width(self):
        """public getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """create the setter method width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """public getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """create the setter method height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """public getter method"""
        return self.__x

    @x.setter
    def x(self, value):
        """create the setter method x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """public getter method"""
        return self.__y

    @y.setter
    def y(self, value):
        """create the setter method y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        """update the Rectangle class by adding a public method
        Print a stdout of the rectangle with #"""
        for k in range(self.__y):
            print()
        for column in range(self.__height):
            print(" ", end="")
            for i in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """add a public method update to assign an argument
        to each attribute"""
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            my_list = ["id", "width", "height", "x", "y"]
            for arg in range(len(args)):
                if arg != 5:
                    setattr(self, my_list[arg], args[arg])

    def to_dictionary(self):
        return {'x': self.__x, 'y': self.__y, 'id': self.id,
                'height': self.__height, 'width': self.__width}
