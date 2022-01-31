#!/usr/bin/python3

"""Write a class MyList that inherits from list
Public instance method print_sorted(), that print the list
"""


class MyList(list):

    """ print the list but sorted in ascending sort"""

    def print_sorted(self):

        print("{}".format(sorted(self)))
