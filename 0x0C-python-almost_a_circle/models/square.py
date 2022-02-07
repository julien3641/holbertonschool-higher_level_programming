#!/usr/bin/python3
"""
The module define the class Square.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class inherits for rectangle and represent a square"""

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
                if arg != 5:
                    setattr(self, my_list[arg], args[arg])

    def to_dictionary(self):
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
