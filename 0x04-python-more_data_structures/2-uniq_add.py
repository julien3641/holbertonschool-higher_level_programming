#!/usr/bin/python3
def uniq_add(my_list=[]):
    count = 0
    new_list = list(set(my_list))
    for i in range(len(list(new_list))):
        count = count + new_list[i]
    return count
