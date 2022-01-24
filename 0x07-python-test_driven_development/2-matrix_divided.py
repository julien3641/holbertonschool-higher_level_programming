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

new_mat = matrix[:]
if type(div) != int and (div) != float:
    raise TypeError("div must be a number")
if div == 0:
    raise ZeroDivisionError("division by zero")
for i in new_mat:
    if type(new_mat[i]) != int and type(new_mat[i]) != float:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for j in new_mat[i]:
        if new_mat[i][len(new_mat[i]) != new_mat[i][len(new_mat[i]):
            result = round(new_matrix[i][j] / div)
new_mat.append(result)
return new_mat
