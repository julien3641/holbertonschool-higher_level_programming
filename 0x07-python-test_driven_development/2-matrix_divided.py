#!/usr/bin/python3

"""write a function that divide all the elements of a matrix
The result will be an integer
The objectif of this exercices is to learn about testing a function
So we create a function that divide to matrix
and create at least 5 tests to check the function"""


def matrix_divided(matrix, div):

    """write a function that divide all the elements of a matrix by a number
    if the number is not a float change it into an integer
    if the number is nor an integer or a float display the error message"""

    div_err = "div must be a number"
    mat_err = "matrix must be a matrix (list of lists) of integers/floats"
    row_err = "Each row of the matrix must have the same size"

    if type(div) is not int and type(div) is not float:
        raise TypeError(div_err)
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_mat = matrix.copy()
    for l in range(len(matrix)):
        new_mat[l] = matrix[l].copy()
        if l != 0:
            if len(matrix[l]) != len(matrix[l - 1]):
                raise TypeError(row_err)
        for c in range(len(matrix[l])):
            if type(matrix[l][c]) != int and type(matrix[l][c]) != float:
                raise TypeError(mat_err)
            new_mat[l][c] = round(matrix[l][c] / div, 2)
    return new_mat
