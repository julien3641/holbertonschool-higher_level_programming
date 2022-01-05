#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for i in range(len(matrix)):
        new_matrix[i] = matrix[i].copy()
        for j in range(len(matrix[i])):
            new_matrix[i][j] = matrix[i][j] * matrix[i][j]
    return new_matrix
