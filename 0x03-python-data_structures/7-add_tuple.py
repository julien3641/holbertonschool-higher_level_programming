#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) <= 1 and len(tuple_b) <= 1:
        tuple_a = (tuple_a[0], 0)
        tuple_b = (tuple_b[0], 0)
        result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    elif len(tuple_a) > 2 and len(tuple_b) > 2:
        tuple_a = (tuple_a[0], tuple_a[1])
        tuple_b = (tuple_b[0], tuple_b[1])
        result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    else:
        tuple_a = tuple_a + (0, 0)
        tuple_b = tuple_b + (0, 0)
        result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return result
