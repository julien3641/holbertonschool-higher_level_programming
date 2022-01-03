#!/usr/bin/python3
def tuple_check(tuple_t=()):
    if len(tuple_t) > 2:
        tuple_t = (tuple_t[0], tuple_t[1])
    elif len(tuple_t) <= 1:
        if len(tuple_t) == 0:
            tuple_t = (0, 0)
        if len(tuple_t) == 1:
            tuple_t = (tuple_t[0], 0)
    return tuple_t


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_check(tuple_a)
    tuple_b = tuple_check(tuple_b)
    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return result
