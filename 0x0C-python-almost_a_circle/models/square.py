#!/usr/bin/python3
"""Write the class Square that inherits from Rectangle:

    In the file models/square.py
    Class Square inherits from Rectangle
    Class constructor: def __init__(self, size, x=0, y=0, id=None)::
        Call the super class with id, x, y, width and height
        this super call will use the logic of
        the __init__ of the Rectangle class.
        The width and height must be assigned to the value of size
        You must not create new attributes for this class,
        use all attributes of Rectangle - As reminder:
        a Square is a Rectangle with the same width and height
        All width, height, x and y validation must inherit from Rectangle
        same behavior in case of wrong data
    The overloading __str__ method should return [Square] (<id>) <x>/<y>
    <size> - in our case, width or height

As you know, a Square is a special Rectangle,
so it makes sense this class Square
inherits from Rectangle. Now you have
a Square class who has the same attributes and same methods."""

from models.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        """initialize the square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """override the with __str__ method a message"""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """public getter method"""
        return self.width

    @size.setter
    def size(self, value):
        """create the size setter method with width anb height
        respectively"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """add a public method that update
        to assign an argument to each attribute"""
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            my_list = ["id", "size", "x", "y"]
            for arg in range(len(args)):
                setattr(self, my_list[arg], args[arg])

    def to_dictionary(self):
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
