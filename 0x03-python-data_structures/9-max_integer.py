#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return
    largest = sorted(my_list)[-1]
    return largest
