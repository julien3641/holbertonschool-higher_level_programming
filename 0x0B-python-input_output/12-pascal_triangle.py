#!/usr/bin/python3
"""Create a function def pascal_triangle(n):
that returns a list of lists of integers representing
the Pascal’s triangle of n:
Returns an empty list if n <= 0
You can assume n will be always an integer
You are not allowed to import any module
"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle """
    if n <= 0:
        return []
    tgl = [[]]
    a = 0
    for i in range(n):
        add1 = 0
        add2 = 0
        tgl[i].append(1)
        if i >= 2:
            for j in range(a):
                tgl[i].append(tgl[i - 1][add1] + tgl[i - 1][add2 + 1])
                add1 += 1
                add2 += 1
        if i >= 1:
            tgl[i].append(1)
            a += 1
        if i != n-1:
            tgl.append([])
    return tgl
