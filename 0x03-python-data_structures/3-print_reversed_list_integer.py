#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for a in range(len(my_list)):
        new_list = my_list[::-1]
        print("{}".format(new_list[a]), end="\n")
