#!/usr/bin/python3
"""
The module define the class Base.
"""
import json
import os.path


class Base:
    """ This class is the base class
    This class represent the base of rectangle and square"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the private class attribute _nb_objects
        build the class with id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """create list dictionary"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save a list of dictionary into a file called
        with the name of the class end with .json"""
        filename = cls.__name__ + '.json'
        with open(filename, "w", encoding='utf-8') as f:
            if list_objs is None:
                return f.write(cls.to_json_string(None))
            else:
                mylist = []
                for i in list_objs:
                    mylist.append(i.to_dictionary())
                return f.write(cls.to_json_string(mylist))

    @staticmethod
    def from_json_string(json_string):
        """return the list of the json string representing
        a list of dictionaries"""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """return an instance with all attribute already set"""
        if cls.__name__ == "Square":
            dummy = cls(2)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """return a list of instances"""
        filename = cls.__name__ + ".json"
        if os.path.exists(filename) is False:
            return []
        else:
            with open(filename, "r", encoding='utf-8') as f:
                list = cls.from_json_string(f.read())
                newlist = []
                for i in range(len(list)):
                    dummy = cls.create(**list[i])
                    newlist.append(dummy)
                return newlist

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ this function open a window and draws all the rectangle
        and squares in the main function"""
