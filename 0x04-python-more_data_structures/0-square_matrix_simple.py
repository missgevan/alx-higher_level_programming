#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        result_matrix = [x**2 for x in row]
        new_matrix.append(result_matrix)
        return new_matrix
